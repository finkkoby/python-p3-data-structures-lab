spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [dict.get("name") for dict in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [dict for dict in spicy_foods if dict.get("heat_level") > 5]

def print_spicy_foods(spicy_foods):
    new_labels = [[value for key, value in food.items()] for food in spicy_foods]
    [print(f"{label[0]} ({label[1]}) | Heat Level: {'🌶' * label[2]}") for label in new_labels]

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [food for food in spicy_foods if (food.get("cuisine") == cuisine)][0]

def print_spiciest_foods(spicy_foods):
    new_labels = [[value for key, value in food.items()] for food in spicy_foods]
    [print(f"{label[0]} ({label[1]}) | Heat Level: {'🌶' * label[2]}") for label in new_labels if label[2] > 5]

def get_average_heat_level(spicy_foods):
    heat_levels = [food.get("heat_level") for food in spicy_foods]
    total = 0
    for i in range(len(heat_levels)):
        total += heat_levels[i]
    return total / len(heat_levels)

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]
