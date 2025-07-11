from flask.views import MethodView
from flask_smorest import Blueprint
from flask import request
import requests
import os
import json
from marshmallow import Schema, fields, ValidationError

from openai import OpenAI
from models.store import StoreModel
from models.item import ItemModel
from models.item_type import ItemType

# Setup
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
blp = Blueprint("recipes", "recipes", description="Recipe tools")


# === SCHEMAS ===
class ExtractRecipeSchema(Schema):
    url = fields.String(required=True)


class RecipeAIResponseSchema(Schema):
    title = fields.String(required=True)
    ingredients = fields.List(fields.String(), required=True)
    instructions = fields.List(fields.String(), required=True)


# === HELPERS ===
def extract_json_from_openai_response(text):
    """
    Trims OpenAI code block wrappers and attempts to load JSON.
    """
    try:
        if text.startswith("```"):
            text = text.strip("`").strip()
            if text.lower().startswith("json"):
                text = text[4:].strip()
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse OpenAI response: {e}")


# === ROUTES ===
@blp.route("/extract-recipe")
class ExtractRecipe(MethodView):
    @blp.arguments(ExtractRecipeSchema)
    def post(self, parsed_json):
        url = parsed_json["url"]

        # Step 1: Fetch HTML
        try:
            html = requests.get(url, timeout=10).text
        except Exception as e:
            return {"error": f"Failed to fetch URL: {e}"}, 500

        # Step 2: Prompt OpenAI
        prompt = (
            "You are a recipe extraction tool.\n"
            "Given raw HTML of a recipe page, extract ONLY:\n"
            "- title\n- ingredients (list)\n- instructions (list)\n\n"
            "Return in JSON format:\n"
            "{\n"
            "  \"title\": \"...\",\n"
            "  \"ingredients\": [\"...\"],\n"
            "  \"instructions\": [\"...\"]\n"
            "}\n\n"
            "HTML:\n" + html[:10000]
        )

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                temperature=0
            )
            raw = response.choices[0].message.content
            print("=== RAW AI RESPONSE ===\n", raw)

            parsed = extract_json_from_openai_response(raw)

            # Optional: Validate structure
            # Validate structure
            try:
                validated = RecipeAIResponseSchema().load(parsed)
            except ValidationError as ve:
                return {"error": f"Invalid recipe structure: {ve.messages}"}, 400
            
            # Guard against blank data
            if not validated["title"].strip() or not validated["ingredients"] or not validated["instructions"]:
                return {"error": "Extracted recipe is missing title, ingredients, or instructions."}, 400

        except Exception as e:
            return {
                "error": f"OpenAI failed: {e}",
                "raw_response": response.choices[0].message.content if 'response' in locals() else ''
            }, 500

        # Step 3: Save to DB
        try:
            recipe, created = StoreModel.get_or_create(name=parsed["title"])
            ingredient_type = ItemType.get(ItemType.name == "ingredient")
            instruction_type = ItemType.get(ItemType.name == "instruction")

            for ing in parsed["ingredients"]:
                ItemModel.get_or_create(name=ing, store=recipe, type=ingredient_type)
            for step in parsed["instructions"]:
                ItemModel.get_or_create(name=step, store=recipe, type=instruction_type)

        except Exception as e:
            return {"error": f"DB save failed: {e}"}, 500

        return {"message": "Recipe extracted and saved", "recipe_id": recipe.id}


@blp.route("/recipes/<int:recipe_id>")
class GetRecipeDetail(MethodView):
    def get(self, recipe_id):
        store = StoreModel.get_or_none(StoreModel.id == recipe_id)
        if not store:
            return {"error": "Recipe not found"}, 404

        items = ItemModel.select().where(ItemModel.store == store)
        ingredients = [item.name for item in items if item.type.name == "ingredient"]
        instructions = [item.name for item in items if item.type.name == "instruction"]

        return {
            "id": store.id,
            "name": store.name,
            "ingredients": ingredients,
            "instructions": instructions
        }

@blp.route("/recipes/<int:recipe_id>")
class DeleteRecipe(MethodView):
    def delete(self, recipe_id):
        store = StoreModel.get_or_none(StoreModel.id == recipe_id)
        if not store:
            return {"error": "Recipe not found"}, 404

        # Delete associated items first
        ItemModel.delete().where(ItemModel.store == store).execute()

        # Then delete the store/recipe itself
        store.delete_instance()

        return {"message": "Recipe deleted successfully."}

class ExtractFromTextSchema(Schema):
    text = fields.String(required=True)

@blp.route("/extract-text-recipe")
class ExtractFromText(MethodView):
    @blp.arguments(ExtractFromTextSchema)
    def post(self, parsed_json):
        text = parsed_json["text"]

        prompt = (
            "You are a recipe parsing tool.\n"
            "Given a plain text recipe including the title, ingredients, and instructions,\n"
            "extract ONLY this information in strict JSON format like:\n"
            "{\n"
            "  \"title\": \"...\",\n"
            "  \"ingredients\": [\"...\"],\n"
            "  \"instructions\": [\"...\"]\n"
            "}\n\n"
            "TEXT:\n" + text[:4000]  # limit to avoid token overload
        )

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                temperature=0
            )
            raw = response.choices[0].message.content
            parsed = extract_json_from_openai_response(raw)

            validated = RecipeAIResponseSchema().load(parsed)

            if not validated["title"].strip() or not validated["ingredients"] or not validated["instructions"]:
                return {"error": "Missing title, ingredients, or instructions."}, 400

            recipe, _ = StoreModel.get_or_create(name=validated["title"])
            ingredient_type = ItemType.get(ItemType.name == "ingredient")
            instruction_type = ItemType.get(ItemType.name == "instruction")

            for ing in validated["ingredients"]:
                ItemModel.get_or_create(name=ing, store=recipe, type=ingredient_type)
            for step in validated["instructions"]:
                ItemModel.get_or_create(name=step, store=recipe, type=instruction_type)

            return {"message": "Recipe extracted and saved", "recipe_id": recipe.id}

        except Exception as e:
            return {"error": f"OpenAI failed: {e}"}, 500
