import unittest
from unittest import TestCase
from services.user.user_info import User


class TestUser(TestCase):

    def setUp(self):
        self.user_male = User("Vlad", "Skyba", 19, "male")
        self.user_female = User("Nastya", "Ivanova", 20, "female")

    def test_get_name(self):
        self.assertEqual(self.user_male.get_name(), "Vlad")

    def test_get_surname(self):
        self.assertEqual(self.user_female.get_surname(), "Skyba")

    def test_get_age(self):
        self.assertEqual(self.user_female.get_age(), 19)

    def test_set_age(self):
        self.user_female.set_age(25)
        self.assertEqual(self.user_male.get_age(), 25)

    def test_get_sex(self):
        self.assertEqual(self.user_female.get_sex(), "male")

    def test_singelton(self):
        self.assertEqual(id(self.user_male), id(self.user_female))
        self.assertEqual(self.user_female.get_name(), "Vlad")
        self.assertEqual(self.user_female.get_surname(), "Skyba")
        self.assertEqual(self.user_female.get_age(), 25)
        self.assertEqual(self.user_female.get_sex(), "male")
