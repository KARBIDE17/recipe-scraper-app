from peewee import Model, CharField, ForeignKeyField
from database import db
from models.store import StoreModel, BaseModel  # Import shared base model and related Store model
from models.item_type import ItemType


# The ItemModel represents an inventory item in the database
class ItemModel(db.Model):
    name = CharField()
    type = ForeignKeyField(ItemType, backref="items")  # 👈 Add this

    store = ForeignKeyField(StoreModel, backref="items")

    class Meta:
        table_name = "item"
        database = db

