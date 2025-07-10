from peewee import Model, CharField, FloatField, IntegerField, ForeignKeyField
from database import db
from models.store import StoreModel, BaseModel  # Import shared base model and related Store model

# The ItemModel represents an inventory item in the database
class ItemModel(BaseModel):
    # Human-readable part name, e.g., "Premier Mounts UMB-DBT"
    part_name = CharField(unique=True, max_length=80)
    
    # Internal or catalog part number (used for searches or tracking)
    part_number = CharField(unique=True, max_length=50)

    # Current stock quantity available for this part
    quantity = IntegerField(default=0)

    # Foreign key linking the item to a store (e.g., Main Warehouse)
    # backref='items' allows you to access all items from a store using store.items
    # on_delete='CASCADE' ensures all items are deleted if the parent store is removed
    store_id = ForeignKeyField(StoreModel, backref='items', on_delete='CASCADE')
    
    @property
    def store_name(self):
        return self.store_id.name if self.store_id else None
