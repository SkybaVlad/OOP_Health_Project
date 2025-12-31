import unittest

from services.body_metrics.body_metrics_calculator import (
    calculate_lean_body_mass,
    calculate_fat_mass,
    calculate_body_mass_index_metrics,
    calculate_basal_metabolic_rate,
)


class LeanBodyMassCalculatorTest(unittest.TestCase):
    def test_invalid_data(self):
        test_cases = [
            ('123', 5, TypeError),
            (-1, 6, ValueError),
            (1, '123', TypeError),
            (1, -1, ValueError),
        ]
        for weight, fat_percentage, expected_error in test_cases:
            with self.subTest(
                weight=weight,
                fat_percentage=fat_percentage,
                expected_error=expected_error,
            ):
                with self.assertRaises(expected_error):
                    calculate_lean_body_mass(weight, fat_percentage)

    def test_valid_data(self):
        test_cases = [(100, 14, 86), (80, 11, 71.2), (92, 12, 80.96)]
        for weight, fat_percentage, result in test_cases:
            with self.subTest(
                weight=weight, fat_percentage=fat_percentage, result=result
            ):
                self.assertEqual(
                    result, calculate_lean_body_mass(weight, fat_percentage)
                )


class BodyMassCalculatorTest(unittest.TestCase):
    def test_invalid_data(self):
        test_cases = [
            ('123', 5, TypeError),
            (-1, 6, ValueError),
            (1, '123', TypeError),
            (1, -1, ValueError),
        ]
        for weight, height, expected_error in test_cases:
            with self.subTest(
                weight=weight, height=height, expected_error=expected_error
            ):
                with self.assertRaises(expected_error):
                    calculate_body_mass_index_metrics(weight, height)

    def test_valid_data(self):
        test_cases = [
            (100, 190, 27.700),
            (90, 190, 24.9307),
        ]
        for weight, height, expected_result in test_cases:
            with self.subTest(
                weight=weight, height=height, expected_result=expected_result
            ):
                self.assertAlmostEqual(
                    expected_result,
                    calculate_body_mass_index_metrics(weight, height),
                    delta=0.001,
                )


class BasalMetabolicRateCalculator(unittest.TestCase):
    def test_invalid_data(self):
        test_cases = []

    def test_valid_data(self):
        test_cases = []


class FatMassCalculator(unittest.TestCase):
    def test_invalid_data(self):
        pass

    def test_valid_data(self):
        test_cases = []
