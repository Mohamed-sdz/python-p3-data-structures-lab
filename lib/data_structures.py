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
    names = []
    for food in spicy_foods:
        names.append(food['name'])
    return names


def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food.get('heat_level', 0) > 5:
            spiciest_foods.append(food)
    return spiciest_foods


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get('name', '')
        cuisine = food.get('cuisine', '')
        heat_level = food.get('heat_level', 0)
        heat_level_emoji = '🌶' * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_level_emoji}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get('cuisine') == cuisine:
            return food
    return None


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)


print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num_foods = len(spicy_foods)
    if num_foods == 0:
        return 0

    for food in spicy_foods:
        heat_level = food.get('heat_level', 0)
        total_heat_level += heat_level

    average_heat_level = total_heat_level / num_foods
    return average_heat_level


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

