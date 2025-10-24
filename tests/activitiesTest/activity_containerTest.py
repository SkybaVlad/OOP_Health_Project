import unittest
from src.activities.activity_container import ActivityContainer


class ActivityContainerTest(unittest.TestCase):
    def setUp(self):
        self.activity_container_object = ActivityContainer()

    def test_constructor(self):
        self.assertIsInstance(self.activity_container_object, ActivityContainer)

    def test_add_activity_method(self):
        self.activity_container_object.add_activity("Football", "03.05.2007")
        self.assertIn("03.05.2007", self.activity_container_object.dictionary.keys())
        self.assertEqual(
            self.activity_container_object.dictionary["03.05.2007"][0], "Football"
        )

    def test_add_activity_method_with_duplicate_data(self):
        self.activity_container_object.add_activity("Football", "03.05.2007")
        self.activity_container_object.add_activity("Volleyball", "03.05.2007")
        self.assertIn("03.05.2007", self.activity_container_object.dictionary.keys())
        self.assertEqual(
            self.activity_container_object.dictionary["03.05.2007"][0], "Football"
        )
        self.assertEqual(
            self.activity_container_object.dictionary["03.05.2007"][1], "Volleyball"
        )

    def test_add_activity_method_with_two_different_activities(self):
        self.activity_container_object.add_activity("Football", "03.05.2007")
        self.activity_container_object.add_activity("Volleyball", "02.05.2007")
        self.assertIn("03.05.2007", self.activity_container_object.dictionary.keys())
        self.assertIn("02.05.2007", self.activity_container_object.dictionary.keys())
        self.assertEqual(
            self.activity_container_object.dictionary["03.05.2007"][0], "Football"
        )
        self.assertEqual(
            self.activity_container_object.dictionary["02.05.2007"][0], "Volleyball"
        )

    # need test with invalid data but need add typehints

    def test_get_activity_in_specific_date_method(self):
        self.activity_container_object.add_activity("Football", "03.05.2007")
        self.activity_container_object.add_activity("Volleyball", "02.05.2007")
        self.assertEqual(
            self.activity_container_object.get_activity_in_specific_date("03.05.2007")[
                0
            ],
            "Football",
        )

    def test_get_activity_in_specific_date_method_with_duplicate_data(self):
        self.activity_container_object.add_activity("Football", "03.05.2007")
        self.activity_container_object.add_activity("Volleyball", "03.05.2007")
        self.assertEqual(
            self.activity_container_object.get_activity_in_specific_date("03.05.2007"),
            ["Football","Volleyball"]
        )
        self.assertIn("Football", self.activity_container_object.get_activity_in_specific_date(
            "03.05.2007"))
        self.assertIn("Volleyball", self.activity_container_object.get_activity_in_specific_date("03.05.2007"))
