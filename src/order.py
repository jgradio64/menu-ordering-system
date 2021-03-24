# Imports
from queue import PriorityQueue
from .meal_class import Meal


# This class holds the oder information
class Order:
    """This hold the functions and data necessary for the implementation of
    an order """
    def __init__(self):
        self.meal = Meal()
        self.meal_type = ""  # meal_type.lower()
        self.item_queue = PriorityQueue()
        self.items_ordered = []
        self.errors = []
        self.error_message = ""

    def build_breakfast(self):
        """Adds the Breakfast Dish objects"""
        self.meal.add_dish("Eggs", "Main", False, True)
        self.meal.add_dish("Toast", "Side", False, True)
        self.meal.add_dish("Coffee", "Drink", True, False)
        self.meal.add_dish("Water", "Water", False, False)

    def build_lunch(self):
        """Adds the Lunch Dish objects"""
        self.meal.add_dish("Sandwich", "Main", False, True)
        self.meal.add_dish("Chips", "Side", True, True)
        self.meal.add_dish("Soda", "Drink", False, False)
        self.meal.add_dish("Water", "Water", False, False)

    def build_dinner(self):
        """Adds the Dinner Dish objects"""
        self.meal.add_dish("Steak", "Main", False, True)
        self.meal.add_dish("Potatoes", "Side", False, True)
        self.meal.add_dish("Wine", "Drink", False, False)
        self.meal.add_dish("Water", "Water", False, False)
        self.meal.add_dish("Cake", "Dessert", False, True)

    def validate_order(self):
        """Make sure the number of items for a dish is permitted"""
        is_valid = True
        # Iterates through all the meal options
        for key in self.meal.dishes:
            # Retrieve a dish object
            dish = self.meal.dishes[key]
            # Find how many of that have been ordered
            num_dish = self.items_ordered.count(key)

            # Check to see if the dish is required
            if dish.is_required():
                # If it is required and has not been ordered
                if num_dish == 0:
                    # Generate an error and add it to the error list
                    self.errors.append("{0} is missing".format(dish.course))
                    # Change is_valid to false
                    is_valid = False

            # Checks to see if a dish is repeatable
            if dish.is_repeatable():
                # If so continue
                continue
            # If not repeatable and ordered more than once
            elif num_dish > 1:
                # Generate an error and add it to the error list
                self.errors.append(
                    "{0} cannot be ordered more than once"
                        .format(dish.dish_name))
                # Change is_valid to false
                is_valid = False

        # See if water needs to be added to the order
        self.need_water()
        return is_valid

    def need_water(self):
        """Checks to see if the order needs to have water included with it"""
        array = self.items_ordered
        # Check to see if a drink was ordered
        if self.meal_type.lower() == "dinner":
            # If water has not yet been added to the order
            if not array.count("Water"):
                # Place the Water after the Main, side, and drink
                # (if applicable) in the array.
                position = array.count("Side") + array.count(
                    "Main") + array.count("Drink")
                array.insert(position, "Water")
        # If no drink was ordered, add water
        elif array.count("Drink") == 0:
            # If water has not yet been added to the order
            if array.count("Water") == 0:
                position = array.count("Side") + array.count("Main")
                array.insert(position, "Water")

    def record_items(self):
        """Records the items ordered in an array"""
        while not self.item_queue.empty():
            # id number representing an item
            i = self.item_queue.get()
            # Add an item based upon the item id
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
                # If the user input an invalid number
                print("{0} is not a valid item id for {1}"
                      .format(i, self.meal_type))

    def build_dish_string(self, dish):
        """
        This creates the string for an item,
        based upon how many of that item a user ordered
        :param dish:
        :return: formatted string
        """
        # If multiple were ordered
        if self.items_ordered.count(dish) > 1:
            return "{0}({1})".format(self.meal.dishes[dish].dish_name,
                                     self.items_ordered.count(dish))
        # If none were ordered
        elif self.items_ordered.count(dish) < 1:
            # Return an empty string
            return ""
        # If one was ordered
        else:
            return "{0}".format(self.meal.dishes[dish].dish_name)

    def build_order_string(self):
        """
        This method constructs the output for the order
        :return: the output_string
        """
        output_string = ""

        # For key in dishes dictionary
        for dish in self.meal.dishes:
            # self.meal.dishes[dish].dish_name
            # If the string is initially empty
            if output_string == "":
                # Build a dish string for the dish
                dish_string = self.build_dish_string(dish)
                # Append it to the end of the output string
                output_string += "{0}".format(dish_string)
            # If a dish is already in the string
            else:
                # Build a dish string for the dish
                dish_string = self.build_dish_string(dish)
                if dish_string != "":
                    # Append it to the end of the output_string
                    output_string += ", {0}".format(dish_string)

        # Return the output_string to the main
        return output_string

    def error_output_builder(self):
        """
        This builds an output string for an order
        :return: the error_string output
        """
        for error in self.errors:
            if len(self.error_message) == 0:
                self.error_message += "{0}".format(error)
            else:
                self.error_message += ", {0}".format(error)
        return "Unable to process: {0}".format(self.error_message.capitalize())

    #
    def print_order(self):
        """
        This checks if the order is a valid order, then either builds the order
        string if the order is valid, or builds the error string if it is not.
        :return: either the order_string or the error_string
        """
        # If the order is valid
        if self.validate_order():
            # Returns the final output to the main, which then prints it
            return self.build_order_string()
        # If there are errors
        else:
            # Returns the error output to the main, which then prints it
            return self.error_output_builder()

    def build_order(self, order_input):
        """
        This method runs extractors for input, builds the meal,
        and extracts the items based upon that input.
        Finally it runs the print_order() method and returns the result.

        :param order_input:
        :return: output_to main
        """
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
            # This runs if the meal is not valid
            return "Please enter a valid meal"

    def extract_items(self, order_input):
        """
        This extracts the ids for the items ordered from the input
        :param order_input:
        :return:
        """
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

        # After getting the item id's, call this to record the items
        self.record_items()

    def extract_meal_type(self, order_input):
        """
        This extracts the type of meal from the user input
        :param order_input:
        :return:
        """
        order = order_input.split(" ")
        meal_info = order[0].lower()
        self.meal_type = meal_info
