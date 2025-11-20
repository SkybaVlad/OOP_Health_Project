import unittest
from services.body_metrics.body_metrics import (
    StrategyBodyMetricsInterface,
    Context,
    StrategyBMICalculator,
    StrategyBMRCalculator,
    StrategyLeanBodyMassCalculator,
    StrategyFatMassCalculator,
)


class TestBMICalculator(unittest.TestCase):
    def test_body_mass_index_metrics_with_valid_data(self):
        test_cases = [
            (StrategyBMICalculator(90, 190), 23.9307),
            (StrategyBMICalculator(70, 180), 21.6049),
        ]
        for bmi_object, expected_value in test_cases:
            with self.subTest(bmi_object=bmi_object, expected_value=expected_value):
                self.assertAlmostEqual(bmi_object.calculate(), expected_value, places=4)

    def test_body_mass_index_metrics_with_invalid_data(self):
        pass


class TestBMRCalculator(unittest.TestCase):
    def test_calculate_basal_metabolic_rate_metrics_with_valid_data(self):
        test_cases = [
            (StrategyBMRCalculator(90, 190, 19, 'male'), 1997.5),
            (StrategyBMRCalculator(60, 70, 25, 'female'), 772.5),
        ]
        for object_bmi, result in test_cases:
            with self.subTest(object_bmi=object_bmi, result=result):
                self.assertAlmostEqual(object_bmi.calculate(), result, places=1)

    def test_calculate_basal_metabolic_rate_metrics_with_invalid_data(self):
        pass


class TestLeanBodyMassCalculator(unittest.TestCase):
    def test_calculate_lean_body_mass_metrics_with_valid_data(self):
        pass


if '__name__' == '__main__':
    unittest.main()
