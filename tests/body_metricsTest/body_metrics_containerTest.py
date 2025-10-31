from src.body_metrics.body_metrics_container import BodyMetricsContainer
import unittest


class BodyMetricsContainerTest(unittest.TestCase):
    def setUp(self):
        self.body_metrics_container = BodyMetricsContainer()

    def test_add_body_mass_index_metrics(self):
        self.body_metrics_container.add_body_mass_index_metrics(30, "17:20")
        self.assertIn(("17:20", 'bmi'), self.body_metrics_container.dictionary.keys())
        self.assertEqual(self.body_metrics_container.dictionary[("17:20", 'bmi')], 30)
