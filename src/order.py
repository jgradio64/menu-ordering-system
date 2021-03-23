from queue import PriorityQueue
from src.meal_class import Meal


# This class holds the oder information
class Order:
    def __init__(self):
        self.mealType = ""  # meal_type.lower()
        self.meal = Meal()
        self.item_queue = PriorityQueue()
        self.items_ordered = []
        self.num_ordered = {}
        self.errors = []
        self.error_message = ""

    # Builds the Breakfast menu
    def build_breakfast(self):
        # Adds the Meal's Dish objects
        self.meal.add_dish("Eggs", "Main", False, True)
        self.meal.add_dish("Toast", "Side", False, True)
        self.meal.add_dish("Coffee", "Drink", True, False)

    # Builds the Lunch menu
    def build_lunch(self):
        # Adds the Meal's Dish objects
        self.meal.add_dish("Sandwich", "Main", False, True)
        self.meal.add_dish("Chips", "Side", True, True)
        self.meal.add_dish("Soda", "Drink", False, False)

    # Builds the Dinner menu
    def build_dinner(self):
        # Adds the Meal's Dish objects
        self.meal.add_dish("Steak", "Main", False, True)
        self.meal.add_dish("Potatoes", "Side", False, True)
        self.meal.add_dish("Wine", "Drink", False, False)
        self.meal.add_dish("Cake", "Desert", False, True)

    # Make sure the number of items for a dish is permitted
    def validate_order(self):
        # For key in meals dictionary
        flag = True
        for key in self.meal.meals:
            print(key)
            dish = self.meal.meals[key]

            # Check to see if the dish is required
            if dish.is_required():
                # If it is required and not ordered
                if self.num_ordered[key] == 0:
                    # Generate an error and add it to the error list
                    self.errors.append("{0} is missing".format(dish.course))
                    flag = False

            # Checks to see if a dish is repeatable
            if dish.is_repeatable():
                # If so continue
                continue
            # If not repeatable and ordered more than once
            elif self.num_ordered[key] > 1:
                # Generate an error and add it to the error list
                self.errors.append("{0} cannot be ordered more than once".format(dish.dish_name))
                flag = False

            # Check to see if a drink was ordered
            array = self.items_ordered
            add_water = False
            if self.mealType == "Dinner":
                if not array.count("Water"):
                    position = array.count("Side") + array.count("Main") + array.count("Drink")
                    array.insert(position, "Water")
                    add_water = True
            elif array.count("Drink") == 0:
                if array.count("Water") == 0:
                    position = array.count("Side") + array.count("Main")
                    array.insert(position, "Water")
                    add_water = True
            print(array)

        if add_water:
            self.meal.add_dish("Water", "Water", False, False)
        return flag

    # So get the number of items here
    # Have to validate with the number of items that can be ordered.
    def record_num_dishes(self):
        # Gets the item id and records the number of times it appears in the order_input
        for menu_item in self.items_ordered:
            if menu_item in self.num_ordered:
                # If the item is in the dictionary, it updates the number of items
                self.num_ordered[menu_item] = self.num_ordered[menu_item] + 1
            else:
                # Sets the number of items if no in the dictionary
                self.num_ordered[menu_item] = 1
        for key in self.meal.meals:
            if key in self.num_ordered:
                continue
            else:
                self.num_ordered[key] = 0
        print(self.num_ordered)

    def record_items(self):
        for menu_item in self.item_queue.queue:
            i = int(menu_item)
            if i == 1:
                self.items_ordered.append('Main')
            elif i == 2:
                self.items_ordered.append('Side')
            elif i == 3:
                self.items_ordered.append('Drink')
            elif i == 4:
                self.items_ordered.append('Desert')

    # This creates the string for an item based upon how many of that item a user ordered
    def build_dish_string(self, dish):
        # If multiple were ordered
        if self.items_ordered.count(dish) > 1:
            return "{0}({1})".format(self.meal.meals[dish].dish_name, self.items_ordered.count(dish))
        # If none were ordered
        elif self.items_ordered.count(dish) < 1:
            return ""
        # If one was ordered
        else:
            return "{0}".format(self.meal.meals[dish].dish_name)

    def build_order_string(self):
        output_string = ""
        # For key in meals dictionary
        for dish in self.items_ordered:
            # self.meal.meals[dish].dish_name
            # If the string is initially empty
            if output_string == "":
                dish_string = self.build_dish_string(dish)
                output_string += "{0}".format(dish_string)
            # If a dish is already in the string
            else:
                dish_string = self.build_dish_string(dish)
                if dish_string != "":
                    output_string += ", {0}".format(dish_string)
        return output_string

    def error_output_builder(self):
        for error in self.errors:
            if len(self.error_message) == 0:
                self.error_message += "{0}".format(error)
            else:
                self.error_message += ", {0}".format(error)
        return "Unable to process: {0}".format(self.error_message.capitalize())

    def print_order(self):
        # See if the order is valid
        if self.validate_order():
            # Prints the final output to the user
            return self.build_order_string()
        # If there are errors
        else:
            return self.error_output_builder()

    # Runs a function based upon the mealType variable
    def build_order(self, input):
        self.extract_meal_type(input)

        if self.mealType == "breakfast":
            self.build_breakfast()
            self.extract_items(input)
            self.record_num_dishes()
            return self.print_order()
        elif self.mealType == "lunch":
            self.build_lunch()
            self.extract_items(input)
            self.record_num_dishes()
            return self.print_order()
        elif self.mealType == "dinner":
            self.build_dinner()
            self.extract_items(input)
            self.record_num_dishes()
            return self.print_order()
        else:
            print("Please enter a valid meal dish_type")

    def extract_items(self, order_input):
        order = order_input.split(" ")
        ids = []
        if len(order) == 1:
            # Indicates that none of the items were ordered
            # Fills the IDs with 0's
            for key in self.meal.meals:
                ids.append(0)
        else:
            # Splits the items and puts them in a queue
            ids = order[1].split(",")
            for item_id in ids:
                self.item_queue.put(item_id)
        self.record_items()

    def extract_meal_type(self, order_input):
        order = order_input.split(" ")
        meal_info = order[0].lower()
        self.mealType = meal_info
