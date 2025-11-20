import unittest
from services.activities.activity_type import SpecificActivityType, time_validator


class TestSpecificActivityTypeClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.specific_activity_type = SpecificActivityType("Football", 7, 40, 70)

    @classmethod
    def tearDownClass(cls):
        del cls.specific_activity_type

    def test_constructor(self):
        self.assertIsInstance(self.specific_activity_type, SpecificActivityType)

    def test_getter_get_name(self):
        self.assertEqual(
            self.specific_activity_type.get_name_of_specific_activity(), "Football"
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
            self.specific_activity_type.calculate_activity_duration_in_minutes(), 30
        )

    def test_calculate_count_of_burned_calories_method(self):
        self.assertGreater(self.specific_activity_type.get_burned_calories(), 0)


class TestTimeValidatorFunction(unittest.TestCase):
    def test_time_validator_type_error(self):
        test_cases = [
            (None, '2007-10-22', None),
            ('2007-10-22', None, None),
            (None, None, None),
            (1, '2007-10-22', None),
            ({}, '2007-10-22', None),
            ('2007-10-22', [], None),
        ]
        for start_time, end_time, result in test_cases:
            with self.subTest(start_time=start_time, end_time=end_time, result=result):
                with self.assertRaises(TypeError):
                    time_validator(start_time, end_time)

    def test_time_validator_value_error(self):
        test_cases = [
            ('2007-10-223', '2007-10-22', None),
            ('2007-10-22', '2007-10-223', None),
            ('2007-10--2', '2007-10-22', None),
            ('20o7-10-22', '2007-10-2/', None),
            ('2007--0-22', '2007-10-22', None),
            ('2007-10u22', '2007710-22', None),
        ]
        for start_time, end_time, result in test_cases:
            with self.subTest(start_time=start_time, end_time=end_time, result=result):
                with self.assertRaises(ValueError):
                    time_validator(start_time, end_time)
