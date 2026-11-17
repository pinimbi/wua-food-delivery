"""Sample cafeteria menus and browse helpers. Prices are in USD for demo purposes."""
MENUS = {
    "Main Cafeteria": [
        {"id":"rice-chicken","name":"Chicken and rice","price":4.50,"category":"Meals"},
        {"id":"veg-wrap","name":"Vegetable wrap","price":3.25,"category":"Meals"},
        {"id":"beef-stew","name":"Beef stew","price":5.00,"category":"Meals"},
        {"id":"fruit-cup","name":"Seasonal fruit cup","price":1.75,"category":"Snacks"},
        {"id":"water","name":"Bottled water","price":0.75,"category":"Drinks"},
    ],
    "Library Cafe": [
        {"id":"cheese-toastie","name":"Cheese toastie","price":2.50,"category":"Snacks"},
        {"id":"coffee","name":"Coffee","price":1.50,"category":"Drinks"},
        {"id":"muffin","name":"Blueberry muffin","price":1.25,"category":"Snacks"},
    ],
}

def get_menu(cafeteria_name: str) -> list[dict]:
    """Return a copy of a cafeteria menu, or an empty list for an unknown cafe."""
    return [item.copy() for item in MENUS.get(cafeteria_name, [])]