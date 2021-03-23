# order_text = order_input("Please enter an order: \t")
from src.order import Order


# Get the user order_input
def print_menu():
    text = input("Please enter an order: \t")
    return text


# Extract information from the user
def extract_info(text):
    order = text.split(" ")
    meal_info = order[0].lower()
    food_info = order[1].split(",")
    return meal_info, food_info


order_input = "Lunch 1,2,2,2,2,2"
# meal, foods = extract_info(order_input)
new_order = Order()

print(new_order.build_order(order_input))

