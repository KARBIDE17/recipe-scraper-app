from flask.views import MethodView
from flask_smorest import Blueprint
from flask import request
import requests
import os
import json
from marshmallow import Schema, fields

from openai import OpenAI
from models.store import StoreModel
from models.item import ItemModel
from models.item_type import ItemType

# OpenAI client setup
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Flask-Smorest Blueprint
blp = Blueprint("recipes", "recipes", description="Recipe tools")

# Marshmallow schema for request body
class ExtractRecipeSchema(Schema):
    url = fields.String(required=True)

@blp.route("/extract-recipe")
class ExtractRecipe(MethodView):

    @blp.arguments(ExtractRecipeSchema)
    def post(self, parsed_json):
        url = parsed_json.get("url")

        if not url:
            return {"error": "URL is required"}, 400

        # Step 1: Fetch the HTML
        try:
            html = requests.get(url, timeout=10).text
        except Exception as e:
            return {"error": f"Failed to fetch URL: {e}"}, 500

        # Step 2: Ask OpenAI to extract recipe data
        prompt = (
            "You are a recipe extraction tool.\n"
            "Given raw HTML of a recipe page, extract ONLY:\n"
            "- title\n- ingredients (list)\n- instructions (list)\n\n"
            "Return it in JSON format. Example:\n"
            "{\n"
            "  \"title\": \"Recipe Title\",\n"
            "  \"ingredients\": [\"ingredient 1\", \"ingredient 2\"],\n"
            "  \"instructions\": [\"Step 1\", \"Step 2\"]\n"
            "}\n\n"
            "HTML:\n" + html[:10000]  # avoid token limit
        )

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0
            )

            # Safely parse OpenAI's response
            response_text = response.choices[0].message.content.strip()

            if response_text.startswith("```"):
                response_text = response_text.strip("`").strip()
                if response_text.startswith("json"):
                    response_text = response_text[4:].strip()

            parsed = json.loads(response_text)

        except Exception as e:
            return {"error": f"OpenAI failed: {e}", "raw_response": response.choices[0].message.content}, 500

        # Step 3: Save to DB
        recipe = StoreModel.create(name=parsed["title"])
        ingredient_type = ItemType.get(ItemType.name == "ingredient")
        instruction_type = ItemType.get(ItemType.name == "instruction")

        for ing in parsed["ingredients"]:
            ItemModel.create(name=ing, store=recipe, type=ingredient_type)
        for step in parsed["instructions"]:
            ItemModel.create(name=step, store=recipe, type=instruction_type)

        return {"message": "Recipe extracted and saved", "recipe_id": recipe.id}
