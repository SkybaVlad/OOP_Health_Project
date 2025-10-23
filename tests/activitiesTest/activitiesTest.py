import unittest
from src.activities.activity import Activity, SpecificActivityType


class MyTestCase(unittest.TestCase):

    def test_constructor_of_activity_class(self):
        activity = Activity()
        self.assertIsInstance(
            activity, Activity, "Is not an instance of Activity Class"
        )

    def test_field_value_of_created_object(self):
        activity_object = Activity()
        self.assertEqual(
            activity_object.specific_activity_type_object, None, "Field is not None"
        )

    def test_field_value_when_its_created(self):
        activity_object = Activity()
        activity_object.set_specific_activity_type_object(10, 20, 30)
        self.assertIsInstance(
            activity_object.specific_activity_type_object,
            SpecificActivityType,
            "Field is not a object of SpecificActivityType Class",
        )

    def test_set_specific_activity_type_object_method(self):
        activity_object = Activity()
        activity_object.set_specific_activity_type_object(10, 20, 30)
        self.assertEqual(
            activity_object.specific_activity_type_object.intensity_of_activity,
            10,
            "Field intensity consists not expected value",
        )
        self.assertEqual(
            activity_object.specific_activity_type_object.start_time_of_activity,
            20,
            "Field intensity consists not expected value",
        )
        self.assertEqual(
            activity_object.specific_activity_type_object.end_time_of_activity,
            30,
            "Field intensity consists not expected value",
        )

    def test_constructor_of_specific_activity_type_class(self):
        specific_activity_type_object = SpecificActivityType(10, 20, 30)
        self.assertEqual(
            specific_activity_type_object.intensity_of_activity,
            10,
            "Intensity of Activity Class",
        )
        self.assertEqual(
            specific_activity_type_object.start_time_of_activity,
            20,
            "Start Time of Activity Class",
        )
        self.assertEqual(
            specific_activity_type_object.end_time_of_activity,
            30,
            "End Time of Activity Class",
        )

    def test_calculate_duration_of_activity_method(self):
        specific_activity_type_object = SpecificActivityType(10, 20, 30)
        self.assertEqual(
            specific_activity_type_object.calculate_duration_of_activity(), 10
        )

    def test_calculate_count_of_burned_calories_method(self):
        specific_activity_type_object = SpecificActivityType(10, 20, 30)
        self.assertGreater(
            specific_activity_type_object.calculate_count_of_burned_calories(), 0
        )


if __name__ == '__main__':
    unittest.main()
