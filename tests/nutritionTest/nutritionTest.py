import unittest
from src.nutrition_control.nutrition_tracker import Nutrition
class TestNutrition(unittest.TestCase):

    def setUp(self):
        self.nutrition = Nutrition(2000)

    def test_constructor(self):
        self.assertEqual(self.nutrition.total_calories, 2000)

    def test_add (self):
        self.assertIn(self.nutrition.add_meals(700,"Eggs"), self.nutrition.meals)