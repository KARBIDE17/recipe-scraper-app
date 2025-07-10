from peewee import Model, CharField
from database import db

# BaseModel defines a shared base for all models using the same Peewee database connection
class BaseModel(Model):
    class Meta:
        database = db  # Link all subclasses of BaseModel to the shared DB instance

# StoreModel represents a physical or virtual store/warehouse in the system
class StoreModel(BaseModel):
    # Unique store name, e.g., "Main Warehouse"
    name = CharField(unique=True, max_length=80)
