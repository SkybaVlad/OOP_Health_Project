import unittest
from buisness.facade import Facade
from unittest.mock import patch
from services.user.user_info import User


user = User("Vlad", 'Skyba', 18, 'mail')


# class TestFacadeSetters(unittest.TestCase):
#     def setUp(self):
#         self.facade = Facade(user)
#
#     def test_set_weight_method_with_valid_data(self):
#         self.facade.set_weight(100)
#         self.assertEqual(
#             self.facade.get_weight(), 100, "Weight value have unexpected value"
#         )
#
#     def test_set_weight_method_with_invalid_data(self):
#         self.facade.set_weight(100)
#         self.facade.set_weight(-100)
#         self.assertEqual(
#             self.facade.get_weight(), 100, "Weight value must have a previous value"
#         )
#         self.facade.set_weight(50)
#         self.facade.set_weight(None)
#         self.assertEqual(
#             self.facade.get_weight(), 50, "Weight value must have a previous value"
#         )
#
#
# class TestFacadeGetters(unittest.TestCase):
#     pass


if '__name__' == '__main__':
    unittest.main()
