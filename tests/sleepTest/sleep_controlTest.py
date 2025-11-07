import unittest
from services.sleep_control.sleep_tracker import Sleep


class TestSleep(unittest.TestCase):
    def setUp(self):
        self.sleep1 = Sleep(8, 23)
        self.sleep2 = Sleep(20, 16)

    def test_constructor(self):
        self.assertEqual(self.sleep1.woke_up, 8)
        self.assertEqual(self.sleep1.went_to_sleep, 23)
        self.assertEqual(self.sleep2.woke_up, 20)
        self.assertEqual(self.sleep2.went_to_sleep, 16)

    def test_get_sleep_duration(self):
        self.assertEqual(self.sleep1.get_sleep_duration(), 9)
        self.assertEqual(self.sleep2.get_sleep_duration(), 4)
