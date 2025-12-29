import unittest

from services.validation_user_input.time_validator import (
    time_validator_format_hh_mm,
    time_validator_format_yyyy_mm_dd,
    time_in_period,
)


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
            ('2026-12-12', ValueError),
            ('2023-12-12', ValueError),
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


class TimeInPeriodFunctionTest(unittest.TestCase):
    """This class test time_in_period function that located in time_logic module
    time_in_period function has the next format time_in_period(start_time, end_time, time_provided_by_user) -> bool
    Time should have the next format YYYY-MM-DD"""

    def test_time_in_period_valid_cases(self):
        test_cases = [
            ("2024-10-12", "2024-11-12", "2024-10-30"),
            ("2025-05-13", "2025-06-14", "2025-05-29"),
            ("2025-06-13", "2025-06-14", "2025-06-13"),
            ("2025-06-13", "2025-06-14", "2025-06-14"),
            ("2024-12-31", "2025-01-02", "2025-01-01"),
            ("2024-12-31", "2024-12-31", "2024-12-31"),
            ("2024-11-27", "2025-01-02", "2024-12-15"),
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
