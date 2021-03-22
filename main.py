# order_text = input("Please enter an order: \t")
from modules.order import Order


def print_menu():
    text = input("Please enter an order: \t")
    return text


def extract_info(text):
    order = text.split(" ")
    meal_info = order[0].lower()
    food_info = order[1].split(",")
    return meal_info, food_info


order_input = "Breakfast 1,2,3,3,3"
meal, foods = extract_info(order_input)
new_order = Order(meal, foods)

new_order.build_meal()
new_order.print_order()
new_order.print_menu()
new_order.validate_order()
