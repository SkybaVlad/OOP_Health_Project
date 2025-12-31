import unittest
from sys import path

path.append("C:/Users/user/PycharmProjects/OOP_Health_Project")
from services.validation_user_input.activity_validation import (
    validate_burned_calories,
    validate_activity_name,
    validate_activity_category,
)


class TestValidationFunctionsForActivityClass(unittest.TestCase):
    def test_activity_name_valid_cases(self):
        test_cases = [
            "Football",
            "Volleyball",
            "Yoga",
            "Tennis",
            "Basketball",
            "Paintball",
            "Boxing",
        ]
        for name in test_cases:
            with self.subTest(name=name):
                self.assertTrue(validate_activity_name(name))

    def test_activity_category_invalid_cases(self):
        test_cases = [
            ("123", ValueError),
            ("Football1", ValueError),
            ("football", ValueError),
            ("sm", ValueError),
            ([], TypeError),
        ]
        for name, result in test_cases:
            with self.subTest(name=name, result=result):
                with self.assertRaises(result):
                    validate_activity_name(name)

    def test_burned_calories_valid_cases(self):
        test_cases = [123, 1, 2, 0]
        for value in test_cases:
            with self.subTest(value=value):
                self.assertTrue(validate_burned_calories(value))

    def test_burned_calories_invalid_cases(self):
        test_cases = [
            (-1, ValueError),
            (1.1, TypeError),
            ('1.1', TypeError),
            ('1', TypeError),
            ([1], TypeError),
        ]
        for value, result in test_cases:
            with self.subTest(value=value, result=result):
                with self.assertRaises(result):
                    validate_burned_calories(value)
