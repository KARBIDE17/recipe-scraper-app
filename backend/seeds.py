from models.item_type import ItemType

def seed_item_types():
    for name in ["ingredient", "instruction"]:
        ItemType.get_or_create(name=name)
