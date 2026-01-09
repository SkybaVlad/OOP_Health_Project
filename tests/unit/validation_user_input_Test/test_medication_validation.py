import unittest

from core.validation_user_input import (
    validate_medication_name,
    validate_form_medication,
    validate_dosage,
)


class MedicationValidationTest(unittest.TestCase):
    def test_validate_medication_name_valid_input(self):
        test_cases = [
            "Aspirin",
            "Paracetamol",
            "Ibuprofen",
            "Amoxicillin",
            "Drotaverine",
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertTrue(validate_medication_name(test_case))

    def test_validate_medication_name_invalid_input(self):
        test_cases = [
            ("Asparin", ValueError),
            ("Paracetamo1", ValueError),
            ("123", ValueError),
            ([], TypeError),
        ]
        for name, result in test_cases:
            with self.subTest(name=name, result=result):
                with self.assertRaises(result):
                    validate_medication_name(name)

    def test_medication_form_valid_cases(self):
        test_cases = ["Capsule", "Pill", "Tablet"]
        for form in test_cases:
            with self.subTest(form=form):
                self.assertTrue(validate_form_medication(form))

    def test_medication_form_invalid_cases(self):
        test_cases = [
            ("Capsul1", ValueError),
            ("Pill1", ValueError),
            ("tablet", ValueError),
            ([], TypeError),
        ]
        for form, result in test_cases:
            with self.subTest(form=form, result=result):
                with self.assertRaises(result):
                    validate_form_medication(form)

    def test_validate_dosage_valid_cases(self):
        self.assertTrue(validate_dosage(0))
        self.assertTrue(validate_dosage(1))

    def test_validate_dosage_invalid_cases(self):
        test_cases = [
            (-1, ValueError),
            (1.1, TypeError),
            ([], TypeError),
            ('1', TypeError),
        ]
        for case, result in test_cases:
            with self.subTest(case=case, result=result):
                with self.assertRaises(result):
                    validate_dosage(case)
