import unittest
from services.time_logic import (
    time_converter_minutes_in_hours,
    calculate_duration_of_activity,
    convert_data_from_string_to_number_format_yyyy_mm_dd_in_numbers,
    get_list_of_all_dates_between_start_and_end,
)
from services.validation_user_input.time_validator import (
    is_source_time_less_than_target_time,
)


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


class TestIsStartLessThanEnd(unittest.TestCase):
    def test_valid_cases(self):
        test_cases = [
            ("2025-12-11", "2025-12-12"),
            ("2025-12-11", "2026-01-01"),
            ("2024-11-11", "2024-12-11"),
        ]
        for start_time, end_time in test_cases:
            with self.subTest(start_time=start_time, end_time=end_time):
                self.assertTrue(
                    is_source_time_less_than_target_time(start_time, end_time)
                )

    def test_invalid_cases(self):
        test_cases = [
            ("2025-12-11", "2025-12-10"),
            ("2025-12-11", "2025-11-11"),
            ("2026-01-01", "2025-01-01"),
        ]
        for start_time, end_time in test_cases:
            with self.subTest(start_time=start_time, end_time=end_time):
                self.assertFalse(
                    is_source_time_less_than_target_time(start_time, end_time)
                )


class TestGetListOfAllDatesBetweenStartAndEndTest(unittest.TestCase):
    def test_valid_cases(self):
        test_cases = [
            (
                "2025-12-29",
                "2026-01-02",
                ["2025-12-29", "2025-12-30", "2025-12-31", "2026-01-01", "2026-01-02"],
            ),
            ("2025-11-11", "2025-11-13", ["2025-11-11", "2025-11-12", "2025-11-13"]),
            (
                "2025-02-27",
                "2025-03-02",
                ["2025-02-27", "2025-02-28", "2025-03-01", "2025-03-02"],
            ),
            (
                "2025-11-29",
                "2025-12-02",
                ["2025-11-29", "2025-11-30", "2025-12-01", "2025-12-02"],
            ),
        ]

        for start_time, end_time, expected_values in test_cases:
            with self.subTest(
                start_time=start_time,
                end_time=end_time,
                expected_values=expected_values,
            ):
                self.assertEqual(
                    get_list_of_all_dates_between_start_and_end(start_time, end_time),
                    expected_values,
                )
