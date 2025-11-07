import unittest
from services.activities import SpecificActivityType


class TestSpecificActivityTypeClass(unittest.TestCase):
    def setUp(self):
        self.specific_activity_type = SpecificActivityType("Football", 7, 40, 70)

    def test_constructor(self):
        self.assertIsInstance(self.specific_activity_type, SpecificActivityType)

    def test_getter_get_name(self):
        self.assertEqual(
            self.specific_activity_type.get_name_of_specific_activity(), "Football"
        )

    def test_getter_get_intensity(self):
        self.assertEqual(
            self.specific_activity_type.get_intensity_of_specific_activity(), 7
        )

    def test_getter_get_start_time(self):
        self.assertEqual(
            self.specific_activity_type.get_start_time_of_specific_activity(), 40
        )

    def test_getter_get_end_time(self):
        self.assertEqual(
            self.specific_activity_type.get_end_time_of_specific_activity(), 70
        )

    def test_calculate_duration_of_activity_method(self):
        self.assertEqual(
            self.specific_activity_type.calculate_duration_of_specific_activity(), 30
        )

    def test_calculate_count_of_burned_calories_method(self):
        self.assertGreater(
            self.specific_activity_type.calculate_count_of_burned_calories(), 0
        )
