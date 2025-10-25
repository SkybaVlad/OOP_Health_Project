import unittest
from src.body_metrics.body_metrics import Weight


class TestWeight(unittest.TestCase):
    def test_init_method(self):
        weight_obj = Weight(80)
        self.assertEqual(weight_obj.value, 80)

    def test_add_method(self):
        weight_obj = Weight(80)
        weight_obj.add_weight(50)
        self.assertEqual(weight_obj.value, 130)

    def test_remove_method(self):
        weight_obj = Weight(80)
        weight_obj.remove_weight(50)
        self.assertEqual(weight_obj.value, 30)

    def test_get_weight_method(self):
        weight_obj = Weight(80)
        self.assertEqual(weight_obj.get_weight(), 80)
