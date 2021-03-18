# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Order:
    def __init__(self, mealtype, *items):
        self.meal = mealtype
        try:
            self.items = dict(items)
        except TypeError:
            # Change this to be more specific as it progresses
            raise Exception("One or more of the item ID's is not valid")
