from marshmallow import Schema, fields

# -----------------------------
# Schema: ItemSchema
# Defines serialization/deserialization rules for ItemModel
# -----------------------------
class ItemSchema(Schema):
    id = fields.Int(dump_only=True)  # Auto-generated ID, only shown when returning data
    part_name = fields.Str(required=True)  # Required part name string
    part_number = fields.Str(required=True)  # Required part number string
    quantity = fields.Int(required=True)  # Required item quantity
    store_id = fields.Int(attribute="store_id_id", required=True)  # Required FK input; hidden in output
    store_name = fields.Str(dump_only=True)  # Optional: returned for convenience, not stored directly

# -----------------------------
# Schema: StoreSchema
# Defines serialization/deserialization rules for StoreModel
# -----------------------------
class StoreSchema(Schema):
    id = fields.Int(dump_only=True)  # Auto-generated ID
    name = fields.Str(required=True)  # Required store name

    # List of items in this store, nested and excluding the 'store_id' field for cleanliness
    items = fields.List(
        fields.Nested(ItemSchema(exclude=("store_id",))), 
        dump_only=True
    )
