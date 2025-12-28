import unittest
from services.health_daily.daily_health import HealthDaily
from data.health_diary_container import HealthDiary
from services.medication.medication import MedicationReceiptList
from facade_logic.facade_dairy_manager import DairyFacade
from datetime import date
from services.activities.activity_type import SpecificActivityType
from unittest.mock import Mock, patch


class TestSingeltonDairyFacade(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.dairy_object = DairyFacade(
            HealthDiary(), HealthDaily(str(date.today())), MedicationReceiptList()
        )

    def test_singleton(self):
        dairy_facade1 = DairyFacade(
            HealthDiary(), HealthDaily(str(date.today())), MedicationReceiptList()
        )
        dairy_facade2 = DairyFacade(
            HealthDiary(), HealthDaily(str(date.today())), MedicationReceiptList()
        )
        self.assertIs(self.dairy_object, dairy_facade1)
        self.assertIs(self.dairy_object, dairy_facade2)


class TestAddMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.dairy_object = DairyFacade(
            HealthDiary(), HealthDaily(str(date.today())), MedicationReceiptList()
        )

    def test_01_set_up(self):
        self.assertEqual(len(self.dairy_object.health_diary.get_history_of_days()), 1)
        self.assertIsInstance(
            self.dairy_object.health_diary.history_of_all_days[0], HealthDaily
        )
        self.assertIsInstance(self.dairy_object.health_diary, HealthDiary)
        self.assertIsInstance(self.dairy_object.current_day, HealthDaily)
        self.assertIsInstance(self.dairy_object.list_of_receipts, MedicationReceiptList)

    def test_02_add_activity_with_today_data(self):
        activity_obj = SpecificActivityType(
            "Sport", "Volleyball", 300, "11:20", "12:40"
        )
        self.dairy_object.add_activity(activity_obj, str(date.today()))
        self.assertEqual(len(self.dairy_object.health_diary.get_history_of_days()), 1)
        self.assertIsInstance(
            self.dairy_object.current_day.list_of_activities_for_day[0],
            SpecificActivityType,
        )
        self.assertEqual(self.dairy_object.current_day.date_of_day, str(date.today()))

    def test_03_add_activity_with_other_data(self):
        activity_obj = SpecificActivityType("Sport", "Football", 700, "15:30", "18:20")
        self.dairy_object.add_activity(activity_obj, "2025-12-26")
        self.assertEqual(len(self.dairy_object.health_diary.get_history_of_days()), 2)
        self.assertTrue(self.dairy_object.health_diary.find_day("2025-12-26"))
        day = self.dairy_object.health_diary.find_day("2025-12-26")
        self.assertIn(activity_obj, day.list_of_activities_for_day)

    def test_04_add_activity_create_new_curr_day(self):
        self.dairy_object.is_current_day = Mock(return_value=False)
        with patch.object(
            self.dairy_object,
            "create_new_health_daily",
            return_value=HealthDaily("2025-12-29"),
        ):
            activity_obj = SpecificActivityType(
                "Sport", "Football", 1000, "10:30", "14:20"
            )
            self.dairy_object.add_activity(activity_obj, "2025-12-29")
            self.assertEqual(self.dairy_object.current_day.date_of_day, "2025-12-29")
            self.assertEqual(
                len(self.dairy_object.health_diary.get_history_of_days()), 3
            )

            daily_obj = self.dairy_object.health_diary.find_day("2025-12-29")
            self.assertIn(activity_obj, daily_obj.list_of_activities_for_day)

    def test_05_add_activity_other_date_with_exist_day_obj(self):
        activity_obj = SpecificActivityType("Cardio", "Yoga", 200, "11:00", "12:30")
        self.dairy_object.add_activity(activity_obj, "2025-12-26")
        self.assertEqual(len(self.dairy_object.health_diary.get_history_of_days()), 3)
        day = self.dairy_object.health_diary.find_day("2025-12-26")
        self.assertIn(activity_obj, day.list_of_activities_for_day)
        self.assertEqual(day.burned_calories_for_day, 900)
