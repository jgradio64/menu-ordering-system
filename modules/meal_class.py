class Meal:
    def __init__(self):
        # Create a dictionary to hold meal items
        self.meals = {}

    # Adds a dish to the menu
    def add_dish(self, dish_name, number, type, repeatable, needed):
        new_dish = self.Dish(dish_name, type, repeatable, needed)
        self.meals[number] = new_dish

    # Retrieves the dish name based upon the dish number
    def get_dishes(self):
        try:
            for dish in self.meals:
                print(dish.dish_name)
        except TypeError:
            # Change this to be more specific as it progresses
            raise Exception("ID's is not valid")

    # Inner class dish holds
    class Dish:
        def __init__(self, name, type, rep, mandated):
            self.dish_name = name
            self.dish_type = type
            self.repeatable = rep
            self.required = mandated

        def is_required(self):
            return self.required

        def is_repeatable(self):
            return self.repeatable
