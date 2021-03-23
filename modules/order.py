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
        self.num_ordered = {}

    # Make sure the number of items for a dish is permitted
    def validate_order(self):
        # For key in meals dictionary
        for key in self.meal.meals:
            dish = self.meal.meals[key]
            flag = True

            # Check to see if the dish is required
            if dish.is_required():
                if self.num_ordered[key] == 0:
                    print("Unable to process: {0} is missing".format(dish.course))
                    # Breaks the current order, exits validation method after printing error message
                    flag = False

            # Checks to see if a dish is repeatable
            if dish.is_repeatable():
                continue
            elif self.num_ordered[key] != 1:
                raise Error("Unable to process: {0} can only be ordered once".format(dish.dish_name))
                # Breaks the current order, exits validation method after printing error message
                flag = False

        return flag

    # So get the number of items here
    # Have to validate with the number of items that can be ordered.
    def record_num_dishes(self):
        # Gets the item id and records the number of times it appears in the input
        for menu_item in self.item_queue.queue:
            i = int(menu_item)
            if i in self.num_ordered:
                # If the item is in the dictionary, it updates the number of items
                self.num_ordered[i] = self.num_ordered[i] + 1
            else:
                # Sets the number of items if no in the dictionary
                self.num_ordered[i] = 1
        for key in self.meal.meals:
            if key in self.num_ordered:
                continue
            else:
                self.num_ordered[key] = 0

    # Runs a function based upon the mealType variable
    def build_meal(self):
        if self.mealType == "breakfast":
            self.build_breakfast()
            self.record_num_dishes()
            self.print_order()
        elif self.mealType == "lunch":
            self.build_lunch()
            self.record_num_dishes()
            self.print_order()
        elif self.mealType == "dinner":
            self.build_dinner()
            self.record_num_dishes()
            self.print_order()
        else:
            print("Please enter a valid meal type")

    def print_order(self):
        # See if the order is valid
        if self.validate_order():
            # Prints the final output to the user
            print(self.build_order_string())

    def build_dish_string(self, dish, key):
        if self.num_ordered[key] > 1:
            return "{0}({1})".format(dish.dish_name, self.num_ordered[key])
        else:
            return "{0}".format(dish.dish_name)

    def build_order_string(self):
        output_string = ""
        # For key in meals dictionary
        for key in self.meal.meals:
            dish = self.meal.meals[key]
            # If the string is initially empty
            if output_string == "":
                dish_string = self.build_dish_string(dish, key)
                output_string += "{0}".format(dish_string)
            # If a dish is already in the string
            else:
                dish_string = self.build_dish_string(dish, key)
                output_string += ", {0}".format(dish_string)
        return output_string

    # Builds the Breakfast menu
    def build_breakfast(self):
        # Adds the Meal's Dish objects
        self.meal.add_dish("Eggs", 1, "Main", False, True)
        self.meal.add_dish("Toast", 2, "Side", False, True)
        self.meal.add_dish("Coffee", 3, "Drink", True, False)

    # Builds the Lunch menu
    def build_lunch(self):
        # Adds the Meal's Dish objects
        self.meal.add_dish("Sandwich", 1, "Main", False, True)
        self.meal.add_dish("Chips", 2, "Side", True, True)
        self.meal.add_dish("Soda", 3, "Drink", False, True)

    # Builds the Dinner menu
    def build_dinner(self):
        # Adds the Meal's Dish objects
        self.meal.add_dish("Steak", 1, "Main", False, True)
        self.meal.add_dish("Potatoes", 2, "Side", False, True)
        self.meal.add_dish("Wine", 3, "Drink", False, False)
        self.meal.add_dish("Cake", 4, "Desert", False, True)
