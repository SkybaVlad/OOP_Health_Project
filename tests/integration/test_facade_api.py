import datetime
import unittest
from unittest.mock import Mock, patch

import core
from core.activity.activity_type import SpecificActivityType
from core.dto_objects import (
    MedicationDTO,
    ActivityTypeDTO,
    convert_activity_obj_into_activity_dto,
)
from core.exceptions import DateOfDayIsGreaterThanTodayError
from core.facade_logic import facade_dairy_manager
from core.facade_logic import facade_api
from core.medication.medication_objects import (
    MedicationReceipt,
    Medication,
    MedicationCharacteristicBuilder,
)
from core import health_analysis
from core.medication import medication_objects

"""This test module tests the API. That means in the tests you can see 
tests that simulate real-user activity and checks that system working correctly.
Django will be using this API so ypu can not see any validation errors because this error
will be in django level. This level only about provide API that working with validated data"""


class TestFacadeAPIConfiguration(unittest.TestCase):
    """This test case tests that all system components is correctly configured"""

    @classmethod
    def setUpClass(cls):
        cls.user = core.User("Vlad", "Skyba", 19, "Male")
        cls.facade_obj = core.create_and_configure_facade_for_start(cls.user)

    def test_01_components_is_configured(self):
        # as from user.user_info import User in core/__init__ act after
        # from facade_logic.facade_api import MainFacade, create_and_configure_facade_for_start
        # the User class name is overwritted by first import so core.facade_logic.facade_api.User
        # does not work
        self.assertIsInstance(
            self.facade_obj.user,
            core.User,
            "Facade user attribute is not instance of User class",
        )
        self.assertIsInstance(
            self.facade_obj.health_diary_facade,
            core.facade_logic.facade_api.DairyFacade,
        )
        self.assertIsInstance(
            self.facade_obj.medication_manager,
            core.facade_logic.facade_api.MedicationManager,
        )
        self.assertIsInstance(
            self.facade_obj.health_diary, core.facade_logic.facade_api.HealthDiary
        )
        self.assertIsInstance(
            self.facade_obj.health_daily, core.facade_logic.facade_api.HealthDaily
        )
        self.assertIsInstance(
            self.facade_obj.health_daily_analyzer,
            core.facade_logic.facade_api.HealthDailyAnalyzer,
        )
        self.assertIsInstance(
            self.facade_obj.health_in_some_period_analyzer,
            core.facade_logic.facade_api.HealthInSomePeriodAnalyzer,
        )
        self.assertIsInstance(
            self.facade_obj.medication_manager.medication_analyzer,
            core.facade_logic.facade_api.MedicationAnalyzer,
        )
        self.assertIsInstance(
            self.facade_obj.medication_manager.list_of_receipts,
            core.facade_logic.facade_api.MedicationReceiptList,
        )

    def test_02_day_is_created(self):
        """Test if after starts off app, the first day is created automatically (with date of starting the program)"""
        self.assertEqual(
            len(self.facade_obj.health_diary_facade.health_diary.get_history_of_days()),
            1,
        )
        self.assertEqual(
            self.facade_obj.health_diary_facade.current_day.date_of_day,
            str(datetime.date.today()),
        )
        self.assertEqual(
            self.facade_obj.health_diary_facade.current_day.name_of_day,
            datetime.date.today().strftime("%A"),
        )

    def test_03_user_is_created_correctly(self):
        """This test check is the user obj is created with correctly data"""
        self.assertEqual(self.facade_obj.user.get_name(), "Vlad")
        self.assertEqual(self.facade_obj.user.get_sex(), "Male")
        self.assertEqual(self.facade_obj.user.get_surname(), "Skyba")
        self.assertEqual(self.facade_obj.user.get_age(), 19)


class TestFacadeAPIAddAndGetFunctionality(unittest.TestCase):
    """This test class test the api that interact with day object of HealthDaily class"""

    @classmethod
    def setUpClass(cls):
        facade_api.date = Mock()
        facade_api.date.today = Mock(return_value=datetime.date(2026, 1, 4))

        facade_dairy_manager.date = Mock(return_value=datetime.date(2026, 1, 4))
        facade_dairy_manager.date.today = Mock(return_value=datetime.date(2026, 1, 4))

        cls.user = core.User("Vlad", "Skyba", 19, "Male")
        cls.facade_obj = facade_api.create_and_configure_facade_for_start(cls.user)

        cls.activity_obj_1 = SpecificActivityType(
            "Sport", "Football", 300, "14:20", "15:50"
        )
        cls.activity_obj_2 = SpecificActivityType(
            "Sport", "Volleyball", 200, "14:20", "15:50"
        )
        cls.activity_obj_3 = SpecificActivityType(
            "Sport", "Volleyball", 100, "14:20", "15:50"
        )

        cls.medication_obj_1 = Medication("Aspirin", "Capsule", "ml")
        cls.medication_obj_2 = Medication("No-Spa", "Tablet", "mg")

    def test_00_correctly_configured(self):
        self.assertEqual(
            self.facade_obj.health_diary_facade.current_day.date_of_day,
            str(datetime.date(2026, 1, 4)),
        )
        self.assertEqual(
            len(self.facade_obj.health_diary_facade.health_diary.get_history_of_days()),
            1,
        )
        self.assertEqual(self.facade_obj.user.get_sex(), "Male")

    def test_00_get_daily_result_when_nothing_is_add(self):
        day_dto = self.facade_obj.get_daily_results()
        self.assertEqual(day_dto.date, "2026-01-04")
        self.assertEqual(day_dto.body_mass_index, None)
        self.assertEqual(day_dto.lean_body_mass_index, None)
        self.assertEqual(day_dto.basal_metabolic_rate, None)

    def test_01_add_activity_other_date(self):
        facade_api.date.fromisoformat = Mock(
            return_value=datetime.date.fromisoformat("2026-01-03")
        )
        self.facade_obj.add_activity(self.activity_obj_1, "2026-01-03")

        self.assertEqual(
            len(self.facade_obj.health_diary_facade.health_diary.history_of_all_days), 2
        )
        self.assertIsNotNone(
            self.facade_obj.health_diary_facade.health_diary.find_day("2026-01-03")
        )
        day = self.facade_obj.health_diary_facade.health_diary.find_day("2026-01-03")
        self.assertIn(self.activity_obj_1, day.list_of_activities_for_day)

    def test_02_add_activity_today_date(self):
        facade_api.date.fromisoformat = Mock(
            return_value=datetime.date.fromisoformat(str(datetime.date(2026, 1, 4)))
        )
        self.facade_obj.add_activity(
            self.activity_obj_1, str(datetime.date(2026, 1, 4))
        )
        day = self.facade_obj.health_diary_facade.health_diary.find_day(
            str(datetime.date(2026, 1, 4))
        )
        self.assertIn(self.activity_obj_1, day.list_of_activities_for_day)

        self.facade_obj.add_activity(
            self.activity_obj_2, str(datetime.date(2026, 1, 4))
        )
        self.assertEqual(
            self.facade_obj.health_diary_facade.current_day.burned_calories_for_day, 500
        )

        self.assertEqual(len(self.facade_obj.health_diary.get_history_of_days()), 2)

    def test_03_add_activity_with_date_than_greater_than_today(self):
        facade_api.date.fromisoformat = Mock(
            return_value=datetime.date.fromisoformat("2045-12-12")
        )
        with self.assertRaises(DateOfDayIsGreaterThanTodayError):
            self.facade_obj.add_activity(self.activity_obj_3, "2045-12-12")

    def test_04_add_weight_today_date(self):
        facade_api.date.fromisoformat = Mock(
            return_value=datetime.date.fromisoformat(str(datetime.date(2026, 1, 4)))
        )
        self.facade_obj.add_weight(100.0, str(datetime.date(2026, 1, 4)))
        self.assertEqual(self.facade_obj.health_diary_facade.current_day.weight, 100.0)

    def test_05_add_weight_to_exist_day(self):
        facade_api.date.fromisoformat = Mock(
            return_value=datetime.date.fromisoformat("2026-01-03")
        )
        self.facade_obj.add_weight(100.0, "2026-01-03")
        day = self.facade_obj.health_diary_facade.health_diary.find_day("2026-01-03")
        self.assertEqual(day.weight, 100.0)

        self.facade_obj.add_weight(101.0, "2026-01-03")
        self.assertEqual(day.weight, 101.0)

    def test_06_add_weight_to_new_day(self):
        facade_api.date.fromisoformat = Mock(
            return_value=datetime.date.fromisoformat("2026-01-02")
        )
        self.facade_obj.add_weight(99.0, "2026-01-02")
        self.assertEqual(
            len(self.facade_obj.health_diary_facade.health_diary.get_history_of_days()),
            3,
        )
        day = self.facade_obj.health_diary_facade.health_diary.find_day("2026-01-02")
        self.assertEqual(day.weight, 99.0)

    def test_07_add_height_value_today_date(self):
        facade_api.date.fromisoformat = Mock(
            return_value=datetime.date.fromisoformat(str(datetime.date(2026, 1, 4)))
        )
        self.facade_obj.add_height(190.0, str(datetime.date(2026, 1, 4)))
        self.assertEqual(self.facade_obj.health_diary_facade.current_day.height, 190.0)

        self.facade_obj.add_height(191.0, str(datetime.date(2026, 1, 4)))
        self.assertEqual(self.facade_obj.health_diary_facade.current_day.height, 191.0)

    def test_08_add_height_value_to_exist_day(self):
        facade_api.date.fromisoformat = Mock(
            return_value=datetime.date.fromisoformat("2026-01-03")
        )
        self.facade_obj.add_height(185.0, "2026-01-03")
        day = self.facade_obj.health_diary_facade.health_diary.find_day("2026-01-03")
        self.assertEqual(day.height, 185.0)

        self.facade_obj.add_height(185.5, "2026-01-03")
        self.assertEqual(day.height, 185.5)

    def test_09_add_height_value_new_date(self):
        facade_api.date.fromisoformat = Mock(
            return_value=datetime.date.fromisoformat("2025-12-31")
        )
        self.facade_obj.add_height(184.0, "2025-12-31")
        day = self.facade_obj.health_diary_facade.health_diary.find_day("2025-12-31")
        self.assertEqual(day.height, 184.0)
        self.assertEqual(
            len(self.facade_obj.health_diary_facade.health_diary.get_history_of_days()),
            4,
        )

    def test_10_add_fat_percentage_to_today_date(self):
        facade_api.date.fromisoformat = Mock(
            return_value=datetime.date.fromisoformat("2026-01-04")
        )
        self.facade_obj.add_fat_percentage(13.5, "2026-01-04")
        self.assertEqual(
            self.facade_obj.health_diary_facade.current_day.fat_percentage, 13.5
        )

    def test_11_change_age(self):
        self.facade_obj.change_age(20)
        self.assertEqual(self.facade_obj.user.get_age(), 20)

    def test_12_add_medication_receipts(self):
        builder = MedicationCharacteristicBuilder()
        med_chars_1 = (
            builder.set_medication_dosage_per_one_take(50)
            .set_frequency("Every day")
            .set_interval("Forever")
            .get_result()
        )

        self.receipt_obj_1 = MedicationReceipt()
        self.assertIsInstance(self.receipt_obj_1, MedicationReceipt)
        self.receipt_obj_1.add_pair_to_receipt(self.medication_obj_1, med_chars_1)

        med_chars_2 = (
            builder.reset()
            .set_medication_dosage_per_one_take(200)
            .set_frequency("Choose specific days")
            .set_list_of_days(["Sunday"])
            .set_interval("Choose specific interval")
            .set_start_time("2026-01-02")
            .set_end_time("2026-01-04")
            .get_result()
        )

        self.receipt_obj_2 = MedicationReceipt()
        self.receipt_obj_2.add_pair_to_receipt(self.medication_obj_2, med_chars_2)

        self.assertEqual(
            type(self.facade_obj.medication_manager.list_of_receipts.receipts), list
        )

        self.assertEqual(
            len(self.facade_obj.medication_manager.list_of_receipts.receipts), 0
        )

        self.facade_obj.add_receipt(self.receipt_obj_1)

        self.facade_obj.add_receipt(self.receipt_obj_2)

        self.assertEqual(
            len(self.facade_obj.medication_manager.list_of_receipts.receipts), 2
        )

        self.assertIn(
            self.receipt_obj_1,
            self.facade_obj.medication_manager.list_of_receipts.receipts,
        )
        self.assertIn(
            self.receipt_obj_2,
            self.facade_obj.medication_manager.list_of_receipts.receipts,
        )

    def test_13_get_list_of_medication_on_today(self):
        health_analysis.date = Mock()
        health_analysis.date.today = Mock(return_value=datetime.date(2026, 1, 4))

        medication_objects.date = Mock(return_value=datetime.date(2026, 1, 4))
        medication_objects.date.today = Mock(return_value=datetime.date(2026, 1, 4))
        medication_objects.date.fromisoformat = Mock(
            return_value=datetime.date(2026, 1, 4)
        )
        med_dto = MedicationDTO(
            name="Aspirin", form="Capsule", unit_of_measurements="ml"
        )
        med_dto_2 = MedicationDTO(
            name="No-Spa", form="Tablet", unit_of_measurements="mg"
        )
        dct = self.facade_obj.get_medications_that_need_to_take_today()
        self.assertEqual(len(dct), 2)
        self.assertIn(med_dto, dct)
        self.assertIn(med_dto_2, dct)

    def test_14_took_medication(self):
        self.facade_obj.took_medication_object(self.medication_obj_1)
        self.assertEqual(
            len(
                self.facade_obj.health_diary_facade.current_day.list_of_taken_medication
            ),
            1,
        )
        self.facade_obj.took_medication_object(self.medication_obj_2)
        self.assertEqual(
            len(
                self.facade_obj.health_diary_facade.current_day.list_of_taken_medication
            ),
            2,
        )

        self.assertEqual(
            len(self.facade_obj.medication_manager.list_of_receipts.receipts), 1
        )

    def test_15_get_list_of_medication_that_no_took(self):
        self.assertEqual(
            [
                (self.medication_obj_1, "2026-01-03"),
                (self.medication_obj_1, "2026-01-02"),
                (self.medication_obj_1, "2025-12-31"),
            ],
            self.facade_obj.get_list_of_skipped_medication(),
        )

    def test_took_med_obj_with_no_today_date(self):
        # in test_14 we took medication object No-Spa and this obj deleted from receipt and as receipt has only this med_obj -> receipt also deleted
        # so we have only 1 receipt in list (Aspirin med_obj in list)

        self.facade_obj.took_medication_object_with_no_today_date(
            self.medication_obj_1, "2025-12-31"
        )
        self.facade_obj.took_medication_object_with_no_today_date(
            self.medication_obj_1, "2026-01-02"
        )
        self.facade_obj.took_medication_object_with_no_today_date(
            self.medication_obj_1, "2026-01-03"
        )
        day = self.facade_obj.health_diary_facade.health_diary.find_day("2025-12-31")
        self.assertIn(self.medication_obj_1, day.list_of_taken_medication)

        day = self.facade_obj.health_diary_facade.health_diary.find_day("2026-01-02")
        self.assertIn(self.medication_obj_1, day.list_of_taken_medication)

        day = self.facade_obj.health_diary_facade.health_diary.find_day("2026-01-03")
        self.assertIn(self.medication_obj_1, day.list_of_taken_medication)

        self.assertEqual(
            len(self.facade_obj.medication_manager.list_of_receipts.receipts), 1
        )

        self.assertEqual(len(self.facade_obj.get_list_of_skipped_medication()), 0)

    def test_16_get_daily_result(self):
        dto_obj = self.facade_obj.get_daily_results()
        self.assertEqual(dto_obj.height, 191.0)
        self.assertEqual(dto_obj.burned_calories, 500)
        self.assertEqual(dto_obj.weight, 100.0)
        self.assertEqual(len(dto_obj.activity), 2)
        self.assertAlmostEqual(dto_obj.body_mass_index, 27.411, places=2)
        self.assertAlmostEqual(dto_obj.basal_metabolic_rate, 2098.75, places=2)
        self.assertEqual(dto_obj.lean_body_mass_index, 86.5)
        self.assertEqual(dto_obj.steps, 0)
        self.assertEqual(dto_obj.date, "2026-01-04")

    def test_17_get_result_of_another_day(self):
        day = self.facade_obj.get_result_of_another_day("2026-01-03")
        self.assertEqual(day.height, 185.5)
        self.assertEqual(day.weight, 101.0)
        self.assertEqual(day.burned_calories, 300)
        self.assertEqual(len(day.activity), 1)
        self.assertIsInstance(day.activity[0], ActivityTypeDTO)

    def test_18_get_daily_res_after_get_res_with_another_day(self):
        self.test_16_get_daily_result()

    @patch("facade_api.date.today")
    @patch("facade_api.date")  # -> test_func = patch(param) -> object of _patch class
    def test_19_get_daily_res_with_update_curr_day(
        self, mock_1_facade_api_date, mock_2_facade_api_date_today
    ):

        facade_dairy_manager.date = Mock()
        facade_dairy_manager.date.today = Mock(return_value=datetime.date(2026, 1, 5))
        mock_2_facade_api_date_today.return_value = datetime.date(2026, 1, 5)

        day = self.facade_obj.get_daily_results()
        self.assertEqual(day.date, "2026-01-05")
        self.assertAlmostEqual(day.body_mass_index, 27.411, places=2)
        self.assertAlmostEqual(day.basal_metabolic_rate, 2098.75, places=2)
        self.assertEqual(day.lean_body_mass_index, 86.5)


if __name__ == '__main__':
    unittest.main()
