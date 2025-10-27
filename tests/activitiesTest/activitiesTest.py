import unittest
from src.activities.activity import Activity, SpecificActivityType
from src.activities.activity_container import ActivityContainer


class TestActivityClass(unittest.TestCase):

    def setUp(self):
        self.activity = Activity()

    def test_constructor_of_activity_class(self):
        self.assertIsInstance(
            self.activity, Activity, "Is not an instance of Activity Class"
        )

    def test_fields_in_constructor(self):
        self.assertEqual(
            self.activity.specific_activity_type_object, None, "Is not a None"
        )
        self.assertIsInstance(
            self.activity.container_of_activities,
            ActivityContainer,
            "Is not an instance of ActivityContainer Class",
        )

    def test_set_specific_activity_type_object_method(self):
        self.activity.create_specific_activity_type_object(
            "Football", 5, 30, 80, "03.05.2007"
        )
        self.assertIsInstance(
            self.activity.specific_activity_type_object,
            SpecificActivityType,
            "Is not an instance of SpecificActivityType Class",
        )

    def test_calculate_duration_of_specific_activity_method(self):
        self.activity.create_specific_activity_type_object(
            "Football", 5, 30, 80, "03.05.2007"
        )
        self.assertEqual(
            self.activity.calculate_duration_of_specific_activity(),
            50,
            "Duration calculated not true",
        )

    def test_get_activities_in_specific_date_method(self):
        self.activity.create_specific_activity_type_object(
            "Football", 5, 30, 80, "03.05.2007"
        )
        self.assertEqual(
            type(self.activity.get_activities_in_specific_date("03.05.2007")),
            type([]),
            "list is not returned",
        )

    def test_get_activities_in_specific_data_with_duplication_data(self):
        self.activity.create_specific_activity_type_object(
            "Football", 5, 30, 80, "03.05.2007"
        )
        self.activity.create_specific_activity_type_object(
            "Volleyball", 5, 30, 80, "03.05.2007"
        )
        self.assertEqual(
            len(
                self.activity.container_of_activities.get_activity_in_specific_date(
                    "03.05.2007"
                )
            ),
            2,
        )


if __name__ == '__main__':
    unittest.main()
