from queue import PriorityQueue
# Runs only with the dot in front of the file name
from .meal_class import Meal


# This class holds the oder information
class Order:
    def __init__(self, meal_type, ids):
        self.mealType = meal_type.lower()
        self.meal = Meal()
        self.item_queue = PriorityQueue()
        for item_id in ids:
            self.item_queue.put(item_id)
        self.num_of_items = {}

    # Make sure the number of items for a dish is permitted
    def validate_order(self):
        # For key in meals dictionary
        for dish in self.meal.meals:
            print("Dish name: {0} \n Number of times ordered {1}"
                  .format(self.meal.meals[dish].dish_name, self.num_of_items[dish]))

    # So get the number of items here
    # Have to validate with the number of items that can be ordered.
    def print_menu(self):
        # Gets the item id and records the number of times it appears in the input
        for menu_item in self.item_queue.queue:
            i = int(menu_item)
            if i in self.num_of_items:
                # If the item is in the dictionary, it updates the number of items
                self.num_of_items[i] = self.num_of_items[i] + 1
            else:
                # Sets the number of items if no in the dictionary
                self.num_of_items[i] = 1

    # Runs a function based upon the mealType variable
    def build_meal(self):
        if self.mealType == "breakfast":
            self.build_breakfast()
        elif self.mealType == "lunch":
            self.build_lunch()
        elif self.mealType == "dinner":
            self.build_dinner()

    def print_order(self):
        try:
            # For key in meals dictionary
            for dish in self.meal.meals:
                print(self.meal.meals[dish].dish_name)
        except TypeError:
            raise Exception("Dish number not working")

    def build_breakfast(self):
        self.meal.add_dish("Eggs", 1, "Main", False, True)
        self.meal.add_dish("Toast", 2, "Side", False, True)
        self.meal.add_dish("Coffee", 3, "Drink", True, False)

    def build_lunch(self):
        self.meal.add_dish("Sandwich", 1, "Main",  False, True)
        self.meal.add_dish("Chips", 2, "Side", True, True)
        self.meal.add_dish("Soda", 3, "Drink", False, True)

    def build_dinner(self):
        self.meal.add_dish("Steak", 1, "Main", False, True)
        self.meal.add_dish("Potatoes", 2, "Side", False, True)
        self.meal.add_dish("Wine", 3, "Drink", False, False)
        self.meal.add_dish("Cake", 4, "Desert", False, True)
