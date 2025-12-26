import unittest
from services.validation_user_input.time_validator import (
    time_validator_format_hh_mm,
    time_validator_format_yyyy_mm_dd,
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
