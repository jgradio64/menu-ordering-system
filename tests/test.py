# Imports
import unittest
from src.order import Order


class TestOrder(unittest.TestCase):
    def test_order_output(self):
        test_cases = {
            "1": ["Breakfast 1,2,3", "Eggs, Toast, Coffee"],
            "2": ["Breakfast 2,3,1", "Eggs, Toast, Coffee"],
            "3": ["Breakfast 1,2,3,3,3", "Eggs, Toast, Coffee(3)"],
            "4": ["Breakfast 1", "Unable to process: Side is missing"],
            "5": ["Lunch 1,2,3", "Sandwich, Chips, Soda"],
            "6": ["Lunch 1,2", "Sandwich, Chips, Water"],
            "7": ["Lunch 1,1,2,3", "Unable to process: Sandwich cannot be ordered more than once"],
            "8": ["Lunch 1,2,2", "Sandwich, Chips(2), Water"],
            "9": ["Lunch", "Unable to process: Main is missing, side is missing"],
            "10": ["Dinner 1,2,3,4", "Steak, Potatoes, Wine, Water, Cake"],
            "11": ["Dinner 1,2,3", "Unable to process: Dessert is missing"]
        }

        for key in test_cases:
            new_order = Order()
            print(test_cases[key])
            result = new_order.build_order(test_cases[key][0])
            self.assertEqual(result, test_cases[key][1])
            print("works")


if __name__ == '__main__':
    unittest.main()
