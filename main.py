# Imports
from src.order import Order

done = False


# Get the user order_input
def print_menu():
    text = input("Please enter an order: \t")
    return text


print("To exit input 'Done'")

while not done:
    order_input = print_menu()
    if order_input.lower() == "done":
        break
    new_order = Order()
    print(new_order.build_order(order_input))
