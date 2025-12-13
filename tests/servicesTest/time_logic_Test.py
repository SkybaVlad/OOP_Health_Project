import unittest
from services.time_logic import (
    time_in_period,
    time_validator_format_yyyy_mm_dd,
    time_validator_format_hh_mm,
    time_converter_minutes_in_hours,
    calculate_duration_of_activity,
    convert_data_from_string_to_number_format_yyyy_mm_dd_in_numbers,
)


class TimeInPeriodFunctionTest(unittest.TestCase):
    """This class test time_in_period function that located in time_logic module
    time_in_period function has the next format time_in_period(start_time, end_time, time_provided_by_user) -> bool
    Time should have the next format YYYY-MM-DD"""

    def test_time_in_period_valid_cases(self):
        test_cases = [
            ("2025-05-13", "2025-06-14", "2025-05-29"),
            ("2025-06-13", "2025-06-14", "2025-06-13"),
            ("2025-06-13", "2025-06-14", "2025-06-14"),
            ("2024-12-31", "2025-01-02", "2025-01-01"),
            ("2024-12-31", "2024-12-31", "2024-12-31"),
            ("2024-10-12", "2024-11-12", "2024-10-30"),
        ]

        for start_time, end_time, user_provided_time in test_cases:
            with self.subTest(
                start_time=start_time,
                end_time=end_time,
                user_provided_time=user_provided_time,
            ):
                self.assertTrue(
                    time_in_period(start_time, end_time, user_provided_time)
                )

    def test_time_in_period_invalid_cases(self):
        test_cases = [
            ("2025-05-13", "2025-06-14", "2025-06-29"),
            ("2025-05-13", "2025-06-14", "2025-05-12"),
            ("2025-05-13", "2025-06-14", "2025-07-29"),
            ("2025-05-13", "2025-06-14", "2025-04-29"),
            ("2025-05-13", "2025-06-14", "2025-06-29"),
            ("2025-05-13", "2025-06-14", "2025-05-12"),
        ]

        for start_time, end_time, user_provided_time in test_cases:
            self.assertFalse(time_in_period(start_time, end_time, user_provided_time))


class TimeValidatorFormatYYYYMMDDTest(unittest.TestCase):
    def test_type_error_cases(self):
        test_cases = [
            (None, TypeError),
            (1234, TypeError),
            ([], TypeError),
            ({}, TypeError),
        ]
        for value, expected_error in test_cases:
            with self.subTest(value=value, expected_error=expected_error):
                with self.assertRaises(expected_error):
                    time_validator_format_yyyy_mm_dd(value)

    def test_value_error_cases(self):
        test_cases = [
            ('1234', ValueError),
            ('2025--1-12', ValueError),
            ('a234-01-01', ValueError),
            ('2025-01-1-', ValueError),
            ('2025-01-0a', ValueError),
            ('2025-01-1@', ValueError),
            ('-----01---', ValueError),
            ('2025-01-32', ValueError),
            ('2025-04-31', ValueError),
            ('2025-02-30', ValueError),
            ('2025-13-30', ValueError),
            ('2025-00-30', ValueError),
        ]

        for value, expected_error in test_cases:
            with self.subTest(value=value, expected_error=expected_error):
                with self.assertRaises(expected_error):
                    time_validator_format_yyyy_mm_dd(value)


class TimeValidatorFormatHHMMSSTest(unittest.TestCase):
    def test_type_error_cases(self):
        test_cases = [None, 1234, [], {}]
        for value in test_cases:
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    time_validator_format_hh_mm(value)

    def test_value_error_cases(self):
        test_cases = [
            '11:333',
            '11:3',
            '11-33',
            '-1:23',
            '23232',
            '24:00',
            '-10:35',
            '23:69',
            '23:-1',
        ]
        for value in test_cases:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    time_validator_format_hh_mm(value)


class ConverterMinutesInHoursTest(unittest.TestCase):
    def test_invalid_input(self):
        test_cases = [
            ('450', TypeError),
            ([], TypeError),
            ({}, TypeError),
            (None, TypeError),
            ((), TypeError),
            (455.5, TypeError),
            (-100, ValueError),
        ]

        for value, expected_error in test_cases:
            with self.subTest(value=value, expected_error=expected_error):
                with self.assertRaises(expected_error):
                    time_converter_minutes_in_hours(value)

    def test_valid_cases(self):
        test_cases = [
            (120, 2, 0),
            (150, 2, 30),
            (200, 3, 20),
            (100, 1, 40),
            (60, 1, 0),
            (40, 0, 40),
            (0, 0, 0),
            (110, 1, 50),
            (61, 1, 1),
        ]
        for value, expected_value1, expected_value2 in test_cases:
            with self.subTest(
                value=value,
                expected_value1=expected_value1,
                expected_value2=expected_value2,
            ):
                self.assertEqual(
                    (expected_value1, expected_value2),
                    (time_converter_minutes_in_hours(value)),
                )


class CalculateDurationOfActivityTest(unittest.TestCase):
    def test(self):
        test_cases = [
            ('15:10', '17:10', 120),
            ('14:25', '15:25', 60),
            ('10:00', '12:00', 120),
            ('23:45', '00:25', 40),
            ('15:41', '15:59', 18),
        ]

        for start_time, end_time, result in test_cases:
            with self.subTest(start_time=start_time, end_time=end_time):
                self.assertEqual(
                    result, calculate_duration_of_activity(start_time, end_time)
                )


class ConvertDataFromStringToNumberTest(unittest.TestCase):
    def test(self):
        test_cases = [
            ('2025-11-11', 20251111),
            ('2025-11-10', 20251110),
            ('2025-11-20', 20251120),
        ]
        for input_time, result in test_cases:
            with self.subTest(input_time=input_time, result=result):
                self.assertEqual(
                    result,
                    convert_data_from_string_to_number_format_yyyy_mm_dd_in_numbers(
                        input_time
                    ),
                )
