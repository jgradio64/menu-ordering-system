class Meal:
    def __init__(self):
        # Create a dictionary to hold meal objects
        self.dishes = {}

    def add_dish(self, dish_name, dish_type, repeatable, required):
        """
        Adds a dish to the menu
        :param dish_name:
        :param dish_type: 
        :param repeatable: 
        :param required: 
        :return: 
        """
        new_dish = self.Dish(dish_name, dish_type, repeatable, required)
        self.dishes[dish_type] = new_dish

    class Dish:
        """
        Inner class dish holds the information about a Meal's dish
        """
        def __init__(self, name, dish_type, rep, mandated):
            self.dish_name = name
            self.course = dish_type
            self.repeatable = rep
            self.required = mandated

        def is_required(self):
            return self.required

        def is_repeatable(self):
            return self.repeatable
