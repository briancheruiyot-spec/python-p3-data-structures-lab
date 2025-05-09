# The list of spicy foods provided.
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

# 1. Define a function get_names() that returns a list of food names
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# 2. Define a function get_spiciest_foods() that returns foods with heat_level > 5
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# 3. Define a function print_spicy_foods() that prints food info with a heat level in "🌶"
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

# 4. Define a function get_spicy_food_by_cuisine() that returns a food by cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # If no match is found

# 5. Define a function print_spiciest_foods() that prints foods with heat level > 5
def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    for food in spiciest:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

# 6. Define a function get_average_heat_level() that returns the average heat level
def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)  # Integer division

# 7. Define a function create_spicy_food() that adds a new spicy food to the list
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
