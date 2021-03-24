# order_text = order_input("Please enter an order: \t")
from src.order import Order

done = False


# Get the user order_input
def print_menu():
    text = input("Please enter an order: \t")
    return text


while not done:
    order_input = print_menu()
    new_order = Order()

    print(new_order.build_order(order_input))
