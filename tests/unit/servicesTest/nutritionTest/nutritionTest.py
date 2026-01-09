import unittest
from services.nutrition_control.nutrition_tracker import Nutrition


class TestNutrition(unittest.TestCase):

    def setUp(self):
        self.nutrition = Nutrition(2000)

    def test_constructor(self):
        self.assertEqual(self.nutrition.total_calories, 2000)
        self.assertEqual(self.nutrition.consumed_calories, 0)
        self.assertEqual(self.nutrition.calories_remaining, 2000)
        self.assertEqual(self.nutrition.meals, [])

    def test_add(self):
        self.assertIn(self.nutrition.add_meals(700, "Eggs"), self.nutrition.meals)
