import unittest
from services.activities import ActivityContainer
from services.activities import SpecificActivityType


class ActivityContainerTest(unittest.TestCase):
    def setUp(self):
        self.activity_container_object = ActivityContainer()
        self.activity_type_duplicate_1 = SpecificActivityType("Football", 8, 30, 20)
        self.activity_type_duplicate_2 = SpecificActivityType("Volleyball", 3, 10, 15)
        self.activity_type_unique_1 = SpecificActivityType("Running", 10, 50, 70)
        self.activity_type_unique_2 = SpecificActivityType("Swimming", 3, 8, 19)

    def test_constructor(self):
        self.assertIsInstance(self.activity_container_object, ActivityContainer)

    def test_add_activity_method(self):
        self.activity_container_object.add_activity(
            self.activity_type_unique_1, "03.05.2007"
        )
        self.assertIn(
            "03.05.2007", self.activity_container_object.dictionary.keys()
        )  # maybe use get_all_dates_method
        self.assertIsInstance(
            self.activity_container_object.dictionary["03.05.2007"][0],
            SpecificActivityType,
        )

    def test_add_activity_method_with_duplicate_data(self):
        self.activity_container_object.add_activity(
            self.activity_type_duplicate_1, "03.05.2007"
        )
        self.activity_container_object.add_activity(
            self.activity_type_duplicate_2, "03.05.2007"
        )
        self.assertEqual(
            self.activity_container_object.dictionary["03.05.2007"][0],
            self.activity_type_duplicate_1,
        )
        self.assertEqual(
            self.activity_container_object.dictionary["03.05.2007"][1],
            self.activity_type_duplicate_2,
        )

    # need test with invalid data but need add typehints

    def test_get_activity_in_specific_date_method(self):
        self.activity_container_object.add_activity(
            self.activity_type_unique_1, "03.05.2007"
        )
        self.assertEqual(
            self.activity_container_object.get_activity_in_specific_date("03.05.2007")[
                0
            ],
            self.activity_type_unique_1,
        )

    def test_get_activity_in_specific_date_method_with_duplicate_data(self):
        self.activity_container_object.add_activity(
            self.activity_type_duplicate_1, "03.05.2007"
        )
        self.activity_container_object.add_activity(
            self.activity_type_duplicate_2, "03.05.2007"
        )
        self.assertEqual(
            self.activity_container_object.get_activity_in_specific_date("03.05.2007"),
            [self.activity_type_duplicate_1, self.activity_type_duplicate_2],
        )

    def test_get_all_activities(self):
        self.activity_container_object.add_activity(
            self.activity_type_unique_1, '03.05.2007'
        )
        self.activity_container_object.add_activity(
            self.activity_type_unique_2, '04.05.2007'
        )
        pass
