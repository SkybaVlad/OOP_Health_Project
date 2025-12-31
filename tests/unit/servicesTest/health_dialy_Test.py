import unittest
from datetime import date
from parameterized import parameterized
from services.nutrition.meal import Meal, MealType
from services.activities.activity_type import SpecificActivityType
from services.medication.medication import Medication
from services.health_daily.daily_health import HealthDaily


class HealthDailyTest(unittest.TestCase):
    def setUp(self):
        self.health_obj = HealthDaily(str(date.today()))
        self.activity = SpecificActivityType("Sport", "Football", 500, "14:25", "16:43")
        self.activity1 = SpecificActivityType(
            "Sport", "Volleyball", 400, "11:25", "13:43"
        )
        self.meal = Meal("Soup", 200, MealType.BREAKFAST)
        self.meal1 = Meal("Soup", 300, MealType.LUNCH)
        self.med = Medication("Aspirin", "Capsule", "ml")

    def test_init(self):
        self.assertEqual(self.health_obj.date_of_day, str(date.today()))
        self.assertEqual(self.health_obj.burned_calories_for_day, 0.0)
        self.assertEqual(self.health_obj.consumed_calories_for_day, 0.0)
        self.assertEqual(self.health_obj.list_of_activities_for_day, [])
        self.assertEqual(self.health_obj.list_of_meals_for_day, [])
        self.assertEqual(self.health_obj.list_of_taken_medication, [])
        self.assertEqual(self.health_obj.drunk_water, 0.0)
        self.assertEqual(self.health_obj.sleep_duration, 0.0)
        self.assertEqual(self.health_obj.count_of_steps_for_day, 0.0)
        self.assertEqual(self.health_obj.weight, 0.0)
        self.assertEqual(self.health_obj.height, 0.0)
        self.assertEqual(self.health_obj.fat_percentage, 0.0)
        self.assertEqual(self.health_obj.total_time_spend_on_activities, 0.0)

    def test_add_methods(self):
        self.health_obj.add_activity(self.activity)
        self.assertEqual(self.health_obj.list_of_activities_for_day, [self.activity])
        self.assertEqual(self.health_obj.burned_calories_for_day, 500)
        self.assertEqual(self.health_obj.total_time_spend_on_activities, 138)

        self.health_obj.add_activity(self.activity1)
        self.assertEqual(self.health_obj.burned_calories_for_day, 900)

        self.health_obj.add_meals(self.meal)
        self.assertEqual(self.health_obj.list_of_meals_for_day, [self.meal])
        self.assertEqual(self.health_obj.consumed_calories_for_day, 200)

        self.health_obj.add_meals(self.meal1)
        self.assertEqual(self.health_obj.consumed_calories_for_day, 500)

        self.health_obj.add_drunk(1)
        self.assertEqual(self.health_obj.drunk_water, 1)

        self.health_obj.add_sleep(1)
        self.assertEqual(self.health_obj.sleep_duration, 1)

        self.health_obj.set_weight(100)
        self.assertEqual(self.health_obj.weight, 100)

        self.health_obj.set_height(200)
        self.assertEqual(self.health_obj.height, 200)

        self.health_obj.set_fat_percentage(12)
        self.assertEqual(self.health_obj.fat_percentage, 12)

        self.health_obj.add_count_of_steps(100)
        self.assertEqual(self.health_obj.count_of_steps_for_day, 100)

        self.health_obj.add_count_of_steps(200)
        self.assertEqual(self.health_obj.count_of_steps_for_day, 300)
