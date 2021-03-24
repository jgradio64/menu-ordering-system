from queue import PriorityQueue
from meal_class import Meal


# This class holds the oder information
class Order:
    def __init__(self):
        self.meal_type = ""  # meal_type.lower()
        self.meal = Meal()
        self.item_queue = PriorityQueue()
        self.items_ordered = []
        self.errors = []
        self.error_message = ""

    # Builds the Breakfast menu
    def build_breakfast(self):
        # Adds the Meal's Dish objects
        self.meal.add_dish("Eggs", "Main", False, True)
        self.meal.add_dish("Toast", "Side", False, True)
        self.meal.add_dish("Coffee", "Drink", True, False)
        self.meal.add_dish("Water", "Water", False, False)

    # Builds the Lunch menu
    def build_lunch(self):
        # Adds the Meal's Dish objects
        self.meal.add_dish("Sandwich", "Main", False, True)
        self.meal.add_dish("Chips", "Side", True, True)
        self.meal.add_dish("Soda", "Drink", False, False)
        self.meal.add_dish("Water", "Water", False, False)

    # Builds the Dinner menu
    def build_dinner(self):
        # Adds the Meal's Dish objects
        self.meal.add_dish("Steak", "Main", False, True)
        self.meal.add_dish("Potatoes", "Side", False, True)
        self.meal.add_dish("Wine", "Drink", False, False)
        self.meal.add_dish("Water", "Water", False, False)
        self.meal.add_dish("Cake", "Dessert", False, True)

    # Make sure the number of items for a dish is permitted
    def validate_order(self):
        flag = True
        # Iterates through all the meal options and checks if they have been ordered
        for key in self.meal.dishes:
            dish = self.meal.dishes[key]
            num_dish = self.items_ordered.count(key)

            # Check to see if the dish is required
            if dish.is_required():
                # If it is required and not ordered
                if num_dish == 0:
                    # Generate an error and add it to the error list
                    self.errors.append("{0} is missing".format(dish.course))
                    flag = False

            # Checks to see if a dish is repeatable
            if dish.is_repeatable():
                # If so continue
                continue
            # If not repeatable and ordered more than once
            elif num_dish > 1:
                # Generate an error and add it to the error list
                self.errors.append("{0} cannot be ordered more than once".format(dish.dish_name))
                flag = False
        self.need_water()
        return flag

    # Checks to see if the order needs to have water included with it
    def need_water(self):
        array = self.items_ordered
        # Check to see if a drink was ordered
        if self.meal_type.lower() == "dinner":
            if not array.count("Water"):
                position = array.count("Side") + array.count("Main") + array.count("Drink")
                array.insert(position, "Water")
        # If no drink was ordered, add water
        elif array.count("Drink") == 0:
            if array.count("Water") == 0:
                position = array.count("Side") + array.count("Main")
                array.insert(position, "Water")

    # Records the items in an array
    def record_items(self):
        while not self.item_queue.empty():
            # id number representing an item
            i = self.item_queue.get()
            if i == 1:
                self.items_ordered.append('Main')
            elif i == 2:
                self.items_ordered.append('Side')
            elif i == 3:
                self.items_ordered.append('Drink')
            elif self.meal_type == "dinner":
                if i == 4:
                    self.items_ordered.append('Dessert')
            else:
                print("{0} is not a valid item id for {1}".format(i, self.meal_type))

    # This creates the string for an item based upon how many of that item a user ordered
    def build_dish_string(self, dish):
        # If multiple were ordered
        if self.items_ordered.count(dish) > 1:
            return "{0}({1})".format(self.meal.dishes[dish].dish_name, self.items_ordered.count(dish))
        # If none were ordered
        elif self.items_ordered.count(dish) < 1:
            return ""
        # If one was ordered
        else:
            return "{0}".format(self.meal.dishes[dish].dish_name)

    # This builds the string for an order
    def build_order_string(self):
        output_string = ""
        # For key in dishes dictionary
        for dish in self.meal.dishes:
            # self.meal.dishes[dish].dish_name
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

    # This builds an output string for an order if there are errors
    def error_output_builder(self):
        for error in self.errors:
            if len(self.error_message) == 0:
                self.error_message += "{0}".format(error)
            else:
                self.error_message += ", {0}".format(error)
        return "Unable to process: {0}".format(self.error_message.capitalize())

    #
    def print_order(self):
        # Checks if the order is valid
        if self.validate_order():
            # Prints the final output to the user
            return self.build_order_string()
        # If there are errors
        else:
            return self.error_output_builder()

    # Runs a function based upon the meal_type variable
    def build_order(self, order_input):
        self.extract_meal_type(order_input)

        if self.meal_type == "breakfast":
            self.build_breakfast()
            self.extract_items(order_input)
            return self.print_order()
        elif self.meal_type == "lunch":
            self.build_lunch()
            self.extract_items(order_input)
            return self.print_order()
        elif self.meal_type == "dinner":
            self.build_dinner()
            self.extract_items(order_input)
            return self.print_order()
        else:
            return "Please enter a valid meal"

    # This extracts the ids for the items ordered
    def extract_items(self, order_input):
        order = order_input.split(" ")
        ids = []
        if len(order) == 1:
            # Indicates that none of the items were ordered
            # Fills the IDs with 0's
            for key in self.meal.dishes:
                ids.append(0)
        else:
            # Splits the items and puts them in a queue
            ids = order[1].split(",")
            for item_id in ids:
                self.item_queue.put(int(item_id))
        self.record_items()

    # This extracts the type of meal that the user inputs
    def extract_meal_type(self, order_input):
        order = order_input.split(" ")
        meal_info = order[0].lower()
        self.meal_type = meal_info
