import unittest
from src.user.user_body_info import UserBodyInfo


class TestUserBodyInfo(unittest.TestCase):
    def setUp(self):
        self.user_body_info = UserBodyInfo()

    def test_fields_values_after_constructor(self):
        self.assertEqual(self.user_body_info.get_weight(), 0)
        self.assertEqual(self.user_body_info.get_height(), 0)
        self.assertEqual(self.user_body_info.get_fat_percentage(), 0)
        self.assertEqual(self.user_body_info.get_percentage_of_water_level(), 0)

    def test_set_and_get_weight_with_valid_int_data(self):
        self.user_body_info.set_weight(100)
        self.assertEqual(self.user_body_info.get_weight(), 100)

    def test_set_and_get_weight_with_valid_float_data(self):
        self.user_body_info.set_weight(5.5)
        self.assertEqual(self.user_body_info.get_weight(), 5.5)

    def test_set_and_get_weight_with_invalid_data(self):
        with self.assertRaises(ValueError):
            self.user_body_info.set_weight(-10)

    def test_set_and_get_height_with_valid_int_data(self):
        self.user_body_info.set_height(100)
        self.assertEqual(self.user_body_info.get_height(), 100)

    def test_set_and_get_height_with_valid_float_data(self):
        self.user_body_info.set_height(5.5)
        self.assertEqual(self.user_body_info.get_height(), 5.5)

    def test_set_and_get_height_with_invalid_data(self):
        with self.assertRaises(ValueError):
            self.user_body_info.set_height(-10)

    def test_set_and_get_fat_percentage_with_valid_int_data(self):
        self.user_body_info.set_fat_percentage(100)
        self.assertEqual(self.user_body_info.get_fat_percentage(), 100)

    def test_set_and_get_fat_percentage_with_valid_float_data(self):
        self.user_body_info.set_fat_percentage(5.5)
        self.assertEqual(self.user_body_info.get_fat_percentage(), 5.5)

    def test_set_and_get_fat_percentage_with_invalid_data(self):
        with self.assertRaises(ValueError):
            self.user_body_info.set_fat_percentage(-10)

    def test_set_and_get_percentage_of_water_level_with_valid_int_data(self):
        self.user_body_info.set_percentage_of_water_level(100)
        self.assertEqual(self.user_body_info.get_percentage_of_water_level(), 100)

    def test_set_and_get_percentage_of_water_level_with_valid_float_data(self):
        self.user_body_info.set_percentage_of_water_level(5.5)
        self.assertEqual(self.user_body_info.get_percentage_of_water_level(), 5.5)

    def test_set_and_get_percentage_of_water_level_with_invalid_data(self):
        with self.assertRaises(ValueError):
            self.user_body_info.set_percentage_of_water_level(-10)
