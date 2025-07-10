from peewee import CharField
from database import db

class ItemType(db.Model):
    name = CharField(unique=True)

    class Meta:
        table_name = "itemtype"
        database = db
