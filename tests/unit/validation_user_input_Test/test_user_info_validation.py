from unittest import TestCase

from services.validation_user_input.user_info_validation import (
    validate_user_name,
    validate_surname,
    validate_age,
    validate_sex,
)


class TestUserInfo(TestCase):
    def test_validate_user_name_valid_input(self):
        test_cases = ["Vlad", "Ivan", "Maks"]

        for name in test_cases:
            with self.subTest(name=name):
                self.assertTrue(validate_user_name(name))

    def test_validate_user_name_invalid_input(self):
        test_cases = [
            (15, TypeError),
            ("Ma", ValueError),
            ("smakdhfksffndldnd", ValueError),
            ("maks", ValueError),
            ("Vla-", ValueError),
            ("Iva1", ValueError),
            ("IvanC", ValueError),
        ]
        for name, error in test_cases:
            with self.subTest(name=name, error=error):
                with self.assertRaises(error):
                    validate_user_name(name)

    def test_validate_user_surname_valid_input(self):
        test_cases = ["Skyba", "Ivanko", "Ivanov", "Asanov"]
        for name in test_cases:
            with self.subTest(name=name):
                self.assertTrue(validate_surname(name))

    def test_validate_user_surname_invalid_input(self):
        test_cases = [
            (15, TypeError),
            ("Ma", ValueError),
            ("smakdhfksffndldnd", ValueError),
            ("ivanov", ValueError),
            ("Ivano1", ValueError),
            ("IVanov", ValueError),
        ]
        for name, error in test_cases:
            with self.subTest(name=name, error=error):
                with self.assertRaises(error):
                    validate_user_name(name)

    def test_validate_age_valid_input(self):
        test_cases = [12, 17, 99, 1, 5]
        for age in test_cases:
            with self.subTest(age=age):
                self.assertTrue(validate_age(age))

    def test_validate_age_invalid_input(self):
        test_cases = [
            ('15', TypeError),
            ([15], TypeError),
            (15.3, TypeError),
            (-1, ValueError),
            (101, ValueError),
        ]
        for age, error in test_cases:
            with self.subTest(age=age, error=error):
                with self.assertRaises(error):
                    validate_age(age)

    def test_validate_user_sex_valid_input(self):
        test_cases = ['Female', 'Male']
        for sex in test_cases:
            with self.subTest(sex=sex):
                self.assertTrue(validate_sex(sex))

    def test_validate_user_sex_invalid_input(self):
        test_cases = [
            (('female',), TypeError),
            (('male',), TypeError),
            (12, TypeError),
            ('female', ValueError),
            ('male', ValueError),
            ('MalE', ValueError),
            ('FemalE', ValueError),
        ]
        for user_sex, error in test_cases:
            with self.subTest(user_sex=user_sex, error=error):
                with self.assertRaises(error):
                    validate_sex(user_sex)
