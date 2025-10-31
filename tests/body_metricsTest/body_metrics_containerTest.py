from src.body_metrics.body_metrics_container import BodyMetricsContainer
import unittest


class BodyMetricsContainerTest(unittest.TestCase):

    def setUp(self):
        self.body_metrics_container = BodyMetricsContainer()


    def test_add_body_mass_index_metrics(self):
        self.body_metrics_container.add_body_mass_index_metrics(30, "17:20")
        self.assertIn(("17:20", 'bmi'), self.body_metrics_container.dictionary.keys())
        self.assertEqual(self.body_metrics_container.dictionary[("17:20", 'bmi')], [30])

    def test_add_body_mass_index_metrics_in_different_time(self):
        self.body_metrics_container.add_body_mass_index_metrics(30, "17:20")
        self.body_metrics_container.add_body_mass_index_metrics(30, "17:21")
        self.assertIn(("17:21", 'bmi'), self.body_metrics_container.dictionary.keys())
        self.assertEqual(self.body_metrics_container.dictionary[("17:21", 'bmi')], [30])
        self.assertIn(("17:20", 'bmi'), self.body_metrics_container.dictionary.keys())
        self.assertEqual(self.body_metrics_container.dictionary[("17:20", 'bmi')], [30])

    def test_add_body_mass_index_metrics_in_same_time(self):
        self.body_metrics_container.add_body_mass_index_metrics(30, "17:21")
        self.body_metrics_container.add_body_mass_index_metrics(40, "17:21")
        self.assertIn(("17:21", 'bmi'), self.body_metrics_container.dictionary.keys())

    def test_add_body_mass_index_metrics_in_same_time_and_same_value(self):
        self.body_metrics_container.add_body_mass_index_metrics(30, "17:21")
        self.body_metrics_container.add_body_mass_index_metrics(30, "17:21")
        pass

    def test_add_basal_mass_index_metrics(self):
        self.body_metrics_container.add_basal_metabolic_rate(30, "17:20")
        self.assertIn(("17:20", 'bmr'), self.body_metrics_container.dictionary.keys())
        self.assertEqual(self.body_metrics_container.dictionary[("17:20", 'bmr')], [30])

    def test_add_lean_body_mass_metrics(self):
        self.body_metrics_container.add_lean_body_mass(30, "17:20")
        self.assertIn(("17:20", 'lbm'), self.body_metrics_container.dictionary.keys())
        self.assertEqual(self.body_metrics_container.dictionary[("17:20", 'lbm')], [30])

    def testadd_fat_mass_metrics(self):
        self.body_metrics_container.add_fat_mass(30, "17:20")
        self.assertIn(("17:20", 'fm'), self.body_metrics_container.dictionary.keys())
        self.assertEqual(self.body_metrics_container.dictionary[("17:20", 'fm')], [30])
