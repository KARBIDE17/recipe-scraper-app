from flask.views import MethodView
from flask_smorest import Blueprint, abort
from peewee import DoesNotExist

from models.store import StoreModel
from models.item import ItemModel
from schemas import ItemSchema
from schemas import StoreSchema

# Blueprint for all store-related routes
blp = Blueprint("Stores", "stores", description="Operations on stores")


# -----------------------------
# Endpoint: /store/<store_id>
# Handles GET and DELETE for a single store
# -----------------------------
@blp.route("/store/<int:store_id>")
class Store(MethodView):

    # GET /store/<store_id> - Fetch one store by ID
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return StoreModel.get_by_id(store_id)
        except DoesNotExist:
            abort(404, message="Store not found.")

    # DELETE /store/<store_id> - Delete a store
    def delete(self, store_id):
        try:
            store = StoreModel.get_by_id(store_id)
            store.delete_instance()
            return {"message": "Store deleted."}
        except DoesNotExist:
            abort(404, message="Store not found.")


# -----------------------------
# Endpoint: /store
# Handles GET all and POST new store
# -----------------------------
@blp.route("/store")
class StoreList(MethodView):

    # GET /store - List all stores
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return list(StoreModel.select())

    # POST /store - Create a new store
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store = StoreModel.create(**store_data)
        return store


# -----------------------------
# Endpoint: /store/<store_id>/items
# Returns all items in a specific store
# -----------------------------
@blp.route("/store/<int:store_id>/items")
class StoreItems(MethodView):

    # GET /store/<store_id>/items - List items belonging to this store
    @blp.response(200, ItemSchema(many=True))
    def get(self, store_id):
        try:
            store = StoreModel.get_by_id(store_id)
            return list(store.items)  # Uses the 'backref' on ForeignKeyField in ItemModel
        except DoesNotExist:
            abort(404, message="Store not found.")
