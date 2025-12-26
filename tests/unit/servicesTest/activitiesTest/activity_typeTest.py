import unittest
from services.activities.activity_type import (
    SpecificActivityType,
    ActivityType,
    ActivityCategory,
)
from parameterized import parameterized


class TestSpecificActivityTypeClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.specific_activity_type = SpecificActivityType(
            "Sport", "Football", 800, '17:20', '19:20'
        )

    @classmethod
    def tearDownClass(cls):
        del cls.specific_activity_type

    def test_constructor(self):
        self.assertIsInstance(self.specific_activity_type, SpecificActivityType)

    def test_activity_category(self):
        self.assertEqual("Sport", self.specific_activity_type.get_activity_category())

    def test_getter_get_name(self):
        self.assertEqual(
            self.specific_activity_type.get_name_of_specific_activity(), "Football"
        )

    def test_getter_get_start_time(self):
        self.assertEqual(
            self.specific_activity_type.get_start_time_of_specific_activity(), '17:20'
        )

    def test_getter_get_end_time(self):
        self.assertEqual(
            self.specific_activity_type.get_end_time_of_specific_activity(), '19:20'
        )

    def test_calculate_duration_of_activity_method(self):
        self.assertEqual(
            self.specific_activity_type.calculate_activity_duration_in_minutes(), 120
        )

    def test_calculate_count_of_burned_calories_method(self):
        self.assertEqual(self.specific_activity_type.get_burned_calories(), 800)
