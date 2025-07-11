from database import db
from models.item_type import ItemType

def seed_item_types():
    for name in ["ingredient", "instruction"]:
        ItemType.get_or_create(name=name)

if __name__ == "__main__":
    db.connect()
    seed_item_types()
    db.close()
