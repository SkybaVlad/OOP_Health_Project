import unittest

from services.nutrition.meal import Meal, MealType
from services.nutrition.eating_mode import (
    BalancingMode,
    BulkingMode,
    SlimmingMode,
)


class TestEatingMode(unittest.TestCase):

    def setUp(self):
        self.soup = Meal("Soup", 300, MealType.LUNCH)
        self.chicken = Meal("Chicken", 600, MealType.DINNER)

    # ---------- Balancing ----------

    def test_balancing_mode_always_ok(self):
        mode = BalancingMode()

        result = mode.evaluate_meal(self.soup, daily_calories=1000)

        self.assertEqual(result, "OK")

    # ---------- Bulking ----------

    def test_bulking_mode_too_few_calories(self):
        mode = BulkingMode()

        result = mode.evaluate_meal(self.soup, daily_calories=1200)

        self.assertEqual(result, "Замало калорій для набору маси")

    def test_bulking_mode_enough_calories(self):
        mode = BulkingMode()

        result = mode.evaluate_meal(self.chicken, daily_calories=1200)

        self.assertEqual(result, "Добре для набору маси")

    # ---------- Slimming ----------

    def test_slimming_mode_over_daily_limit(self):
        mode = SlimmingMode()

        result = mode.evaluate_meal(self.chicken, daily_calories=1500)

        self.assertEqual(result, "Перевищення денної норми")

    def test_slimming_mode_ok(self):
        mode = SlimmingMode()

        result = mode.evaluate_meal(self.soup, daily_calories=1200)

        self.assertEqual(result, "OK для схуднення")
