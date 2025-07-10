from flask.views import MethodView
from flask_smorest import Blueprint, abort
from peewee import DoesNotExist

from models.item import ItemModel
from schemas import ItemSchema

# Create a Blueprint for item-related endpoints
blp = Blueprint("Items", "items", description="Operations on items")

# Endpoint for individual item operations: GET, PUT, DELETE
@blp.route("/item/<int:item_id>")
class Item(MethodView):
    
    # GET /item/<item_id> - Retrieve a single item by ID
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return ItemModel.get_by_id(item_id)
        except DoesNotExist:
            abort(404, message="Item not found.")

    # DELETE /item/<item_id> - Remove an item by ID
    def delete(self, item_id):
        try:
            item = ItemModel.get_by_id(item_id)
            item.delete_instance()
            return {"message": "Item deleted."}
        except DoesNotExist:
            abort(404, message="Item not found.")

    # PUT /item/<item_id> - Fully update an existing item
    @blp.arguments(ItemSchema)           # Parses and validates input using schema
    @blp.response(200, ItemSchema)       # Serializes response using schema
    def put(self, item_data, item_id):
        try:
            item = ItemModel.get_by_id(item_id)
        except DoesNotExist:
            abort(404, message="Item not found.")

        # Update fields manually from validated request data
        item.part_name = item_data["part_name"]
        item.part_number = item_data["part_number"]
        item.quantity = item_data["quantity"]
        item.store = item_data["store_id"]

        item.save()
        return item

# Endpoint for collection-level operations: GET all items, POST new item
@blp.route("/item")
class ItemList(MethodView):

    # GET /item - List all items
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return list(ItemModel.select())

    # POST /item - Create a new item
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel.create(**item_data)
        return item
