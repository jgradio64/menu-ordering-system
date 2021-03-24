class Meal:
    def __init__(self):
        # Create a dictionary to hold meal items
        self.dishes = {}
        self.water_required = False

    # Adds a dish to the menu
    def add_dish(self, dish_name, dish_type, repeatable, needed):
        new_dish = self.Dish(dish_name, dish_type, repeatable, needed)
        self.dishes[dish_type] = new_dish

    # Inner class dish holds
    class Dish:
        def __init__(self, name, dish_type, rep, mandated):
            self.dish_name = name
            self.course = dish_type
            self.repeatable = rep
            self.required = mandated

        def is_required(self):
            return self.required

        def is_repeatable(self):
            return self.repeatable
