import random

def pick_random_item(items):
    item_name = random.choice(list(items.keys()))
    return item_name, items[item_name]