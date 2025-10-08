import unittest
from src.activities.activity import Activity


class MyTestCase(unittest.TestCase):
    def test_init_method_with_valid_parameters(self):
        activity_obj = Activity('Football', 'Stadium', '17:00', '90')
        self.assertEqual(activity_obj.sport_type, 'Football')
        self.assertEqual(activity_obj.place, 'Stadium')
        self.assertEqual(activity_obj.start_time, '17:00')
        self.assertEqual(activity_obj.duration, '90')

    def test_init_method_with_none_parameters(self):
        activity_obj = Activity('Football', 'Stadium', '17:00', None)
        self.assertEqual(activity_obj.duration, None)


if __name__ == '__main__':
    unittest.main()
