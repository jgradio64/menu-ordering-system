# order_text = order_input("Please enter an order: \t")
from src.order import Order


# Get the user order_input
def print_menu():
    text = input("Please enter an order: \t")
    return text


order_input = "Lunch"
new_order = Order()

print(new_order.build_order(order_input))
