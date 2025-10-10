import unittest
from src.water_balance.waterbalance import WaterBalance

class TestWaterBalance(unittest.TestCase):
    def setUp(self):
        self.wb = WaterBalance(2.0)

    def test_constructor(self):
        self.assertEqual(self.wb.total_goal, 2.0)
        self.assertEqual(self.wb.consumed,0)
        self.assertEqual(self.wb.remaining,2.0)
        self.assertEqual(self.wb.water,[])

    def test_add_water(self):
        self.wb.add_water(0.250)
        self.assertEqual(self.wb.total_goal, 2.0)
        self.assertEqual(self.wb.consumed, 0.250)
        self.assertEqual(self.wb.remaining, 1.750)
        self.assertIn(0.250, self.wb.water)