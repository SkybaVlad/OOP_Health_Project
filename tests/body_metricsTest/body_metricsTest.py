import unittest
from src.body_metrics.body_metrics import BodyMetrics


class TestBodyMetricsClass(unittest.TestCase):

    def setUp(self):
        self.body_metrics = BodyMetrics()

    def test_body_mass_index_metrics_with_valid_data(self):
        self.assertAlmostEqual(self.body_metrics.calculate_body_mass_index_metrics(80, 190), 22, places=0)
        self.assertAlmostEqual(self.body_metrics.calculate_body_mass_index_metrics(80, 100), 80, places=0)

    def test_body_mass_index_metrics_with_invalid_data(self):
        with self.assertRaises(ValueError):
            self.body_metrics.calculate_body_mass_index_metrics(0, 190)
        with self.assertRaises(ValueError):
            self.body_metrics.calculate_body_mass_index_metrics(90, 0)

    def test_calculate_basal_metabolic_rate_metrics_with_valid_data(self):
        self.assertAlmostEqual(self.body_metrics.calculate_basal_metabolic_rate_metrics(90, 190, 18, 'male'), 2002.5,
                               places=1)
        self.assertAlmostEqual(self.body_metrics.calculate_basal_metabolic_rate_metrics(90, 190, 18, 'female'), 1836.5,
                               places=1)

    def test_calculate_basal_metabolic_rate_metrics_with_invalid_data(self):
        with self.assertRaises(ValueError):
            self.body_metrics.calculate_basal_metabolic_rate_metrics(0, 190, 18,'male')
        with self.assertRaises(ValueError):
            self.body_metrics.calculate_basal_metabolic_rate_metrics(90, 0,18,'male')

    def test_calculate_lean_body_mass_metrics_with_valid_data(self):
        pass

if '__name__' == '__main__':
    unittest.main()
