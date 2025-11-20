from data.body_metrics_container import BodyMetricsContainer
from data.body_metrics_container import BodyMetricsType
import unittest


class BodyMetricsContainerTest(unittest.TestCase):

    def setUp(self):
        self.body_metrics_container = BodyMetricsContainer()

    def test_add_body_mass_index_metrics(self):
        self.body_metrics_container.add_body_metrics(
            BodyMetricsType.body_mass_index_metrics.value, 30, '03.05.2007'
        )
        self.assertIn(
            ('03.05.2007', 'bmi'), self.body_metrics_container._dictionary.keys()
        )
        self.assertEqual(
            self.body_metrics_container._dictionary[('03.05.2007', 'bmi')], [30]
        )

    def test_add_body_mass_index_metrics_in_different_time(self):
        self.body_metrics_container.add_body_metrics(
            BodyMetricsType.body_mass_index_metrics.value, 30, '03.05.2007'
        )
        self.body_metrics_container.add_body_metrics(
            BodyMetricsType.body_mass_index_metrics.value, 30, '04.05.2007'
        )
        self.assertIn(
            ('03.05.2007', 'bmi'), self.body_metrics_container._dictionary.keys()
        )
        self.assertEqual(
            self.body_metrics_container._dictionary[('03.05.2007', 'bmi')], [30]
        )
        self.assertIn(
            ('04.05.2007', 'bmi'), self.body_metrics_container._dictionary.keys()
        )
        self.assertEqual(
            self.body_metrics_container._dictionary[('04.05.2007', 'bmi')], [30]
        )

    def test_add_body_mass_index_metrics_in_same_time(self):
        self.body_metrics_container.add_body_metrics(
            BodyMetricsType.body_mass_index_metrics.value, 30, '03.05.2007'
        )
        self.body_metrics_container.add_body_metrics(
            BodyMetricsType.body_mass_index_metrics.value, 40, '03.05.2007'
        )
        self.assertIn(
            ('03.05.2007', 'bmi'), self.body_metrics_container._dictionary.keys()
        )

    def test_add_body_mass_index_metrics_in_same_time_and_same_value(self):
        self.body_metrics_container.add_body_metrics(
            BodyMetricsType.body_mass_index_metrics.value, 30, '03.05.2007'
        )
        self.body_metrics_container.add_body_metrics(
            BodyMetricsType.body_mass_index_metrics.value, 30, '03.05.2007'
        )
        self.assertIn(
            ('03.05.2007', 'bmi'), self.body_metrics_container._dictionary.keys()
        )
        self.assertEqual(
            self.body_metrics_container._dictionary[('03.05.2007', 'bmi')], [30, 30]
        )

    def test_get_body_metrics_method(self):
        self.assertIsInstance(
            self.body_metrics_container.get_body_metrics(),
            dict,
            "Return data must be a dict type",
        )

    # def test_add_basal_mass_index_metrics(self):
    #     self.body_metrics_container.add_basal_metabolic_rate(30, "17:20")
    #     self.assertIn(("17:20", 'bmr'), self.body_metrics_container.dictionary.keys())
    #     self.assertEqual(self.body_metrics_container.dictionary[("17:20", 'bmr')], [30])
    #
    # def test_add_lean_body_mass_metrics(self):
    #     self.body_metrics_container.add_lean_body_mass(30, "17:20")
    #     self.assertIn(("17:20", 'lbm'), self.body_metrics_container.dictionary.keys())
    #     self.assertEqual(self.body_metrics_container.dictionary[("17:20", 'lbm')], [30])
    #
    # def testadd_fat_mass_metrics(self):
    #     self.body_metrics_container.add_fat_mass(30, "17:20")
    #     self.assertIn(("17:20", 'fm'), self.body_metrics_container.dictionary.keys())
    #     self.assertEqual(self.body_metrics_container.dictionary[("17:20", 'fm')], [30])
