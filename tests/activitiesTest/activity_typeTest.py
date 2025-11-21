import unittest
from services.activities.activity_type import (
    SpecificActivityType,
    time_validator,
    TimeManager,
)
from parameterized import parameterized


class TestSpecificActivityTypeClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.specific_activity_type = SpecificActivityType(
            "Football", 7, '2007-11-11', '17:20', '19:20'
        )

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
        self.assertGreater(self.specific_activity_type.get_burned_calories(), 0)


class TestTimeValidatorFunction(unittest.TestCase):
    def test_time_validator_type_error(self):
        test_cases = [
            (None, '17:20', '17:20', None),
            ('2007-11-12', None, '17:20', None),
            ('2007-11-12', '17:20', None, None),
            (None, None, None, None),
            ('2007-10-22', 1, '17:20', None),
            ({}, '17:20', '17:20', None),
            ('2007-10-22', '17:20', [], None),
        ]
        for date_of_activity, start_time, end_time, result in test_cases:
            with self.subTest(
                date_of_activity=date_of_activity,
                start_time=start_time,
                end_time=end_time,
                result=result,
            ):
                with self.assertRaises(TypeError):
                    time_validator(date_of_activity, start_time, end_time)

    def test_time_validator_value_error(self):
        test_cases = [
            ('2007-10-223', '17:20', '17:20', None),
            ('2007-10-22', '17:201', '17:20', None),
            ('2007-10--2', '17:20', '17:201', None),
            ('20o7-10-22', '17:20', '17:20', None),
            ('2007--0-22', '17:20', '17:20', None),
            ('2007-10u22', '17:20', '17:20', None),
            ('2007-10-22', '17-20', '17:20', None),
            ('2007-10-22', '17:201', '17-20', None),
            ('2007-10-22', '17:2o', '17:20', None),
            ('2007-10-22', '17:20', '17:2p', None),
        ]
        for date_of_activity, start_time, end_time, result in test_cases:
            with self.subTest(
                date_of_activity=date_of_activity,
                start_time=start_time,
                end_time=end_time,
                result=result,
            ):
                with self.assertRaises(ValueError):
                    time_validator(date_of_activity, start_time, end_time)


class TestTimeManager(unittest.TestCase):
    @parameterized.expand(
        [
            (TimeManager('2007-11-12', '17:20', '19:20'), 120),
            (TimeManager('2007-11-12', '17:20', '19:10'), 110),
            (TimeManager('2007-11-12', '17:20', '19:00'), 100),
            (TimeManager('2007-11-12', '23:00', '00:20'), 80),
        ]
    )
    def test_time_converter_in_minutes(self, time_manager_object, result_minutes):
        self.assertEqual(
            time_manager_object._time_converter_in_minutes_(), result_minutes
        )
