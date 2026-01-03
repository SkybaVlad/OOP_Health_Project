from unittest.mock import Mock, patch
import unittest
import datetime
from sys import path

path.append('C:/Users/user/PycharmProjects/OOP_Health_Project')
from services.medication.medication_objects import (
    MedicationReceipt,
    Medication,
    MedicationReceiptList,
    MedicationCharacteristicBuilder,
)
from facade_logic.facade_dairy_manager import DairyFacade
from services.medication.medication_manager import MedicationManager
from services.health_analysis import MedicationAnalyzer
from data.health_diary_container import HealthDiary
from datetime import date as real_date
from services.health_daily.daily_health import HealthDaily


medication_manager: MedicationManager | None = None


def setUpModule():
    global medication_manager
    first_day = HealthDaily(str(datetime.date.today()))
    health_diary = HealthDiary()
    list_of_receipts = MedicationReceiptList()
    medication_analyzer = MedicationAnalyzer(health_diary, list_of_receipts)
    medication_manager = MedicationManager(list_of_receipts, health_diary)
    medication_manager.set_medication_analyzer(medication_analyzer)
    facade_dairy = DairyFacade(health_diary, first_day, medication_manager)


class TestMedicationFunctionality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        builder = MedicationCharacteristicBuilder()
        cls.med_obj_1_rec_1 = Medication("Aspirin", "Capsule", "ml")

        cls.chars_1_rec_1 = (
            builder.set_medication_dosage_per_one_take(200)
            .set_frequency("Every day")
            .set_interval("Choose specific interval")
            .set_start_time("2026-01-01")
            .set_end_time("2026-01-07")
            .get_result()
        )

        cls.med_obj_2_rec_1 = Medication("No-Spa", "Tablet", "ml")
        cls.chars_2_rec_1 = (
            builder.reset()
            .set_medication_dosage_per_one_take(50)
            .set_frequency("Choose specific days")
            .set_list_of_days(["Monday", "Sunday"])
            .set_interval("Forever")
            .get_result()
        )

        cls.receipt_1 = MedicationReceipt()
        cls.receipt_1.add_pair_to_receipt(cls.med_obj_1_rec_1, cls.chars_1_rec_1)
        cls.receipt_1.add_pair_to_receipt(cls.med_obj_2_rec_1, cls.chars_2_rec_1)

        cls.med_obj_3_rec_2 = Medication("Paracetamol", "Tablet", "mg")
        cls.chars_3_rec_2 = (
            builder.reset()
            .set_medication_dosage_per_one_take(20)
            .set_frequency("Every day")
            .set_interval("Forever")
            .get_result()
        )

        cls.receipt_2 = MedicationReceipt()
        cls.receipt_2.add_pair_to_receipt(cls.med_obj_3_rec_2, cls.chars_3_rec_2)

        cls.med_obj_4_rec_3 = Medication("Augmentin", "Elixir", "ml")
        cls.chars_4_rec_3 = (
            builder.reset()
            .set_medication_dosage_per_one_take(10)
            .set_frequency("Choose specific days")
            .set_list_of_days(["Tuesday", "Friday"])
            .set_interval("Choose specific interval")
            .set_start_time("2026-01-01")
            .set_end_time("2026-01-04")
            .get_result()
        )

        cls.receipt_3 = MedicationReceipt()
        cls.receipt_3.add_pair_to_receipt(cls.med_obj_4_rec_3, cls.chars_4_rec_3)

        medication_manager.add_medication_receipt(cls.receipt_1)
        medication_manager.add_medication_receipt(cls.receipt_2)
        medication_manager.add_medication_receipt(cls.receipt_3)

    def test_creation_functionality(self):
        # test whether receipt objects created correctly
        self.assertEqual(self.chars_1_rec_1.medication_dosage_per_one_take, 200)
        self.assertEqual(self.chars_1_rec_1.frequency, "Every day")
        self.assertEqual(self.chars_1_rec_1.list_of_days, None)
        self.assertEqual(self.chars_1_rec_1.interval, "Choose specific interval")

    def test_receipt_add_functionality(self):

        self.assertEqual(len(medication_manager.list_of_receipts.receipts), 3)

        self.assertIn(self.receipt_1, medication_manager.list_of_receipts.receipts)
        self.assertIn(self.receipt_2, medication_manager.list_of_receipts.receipts)
        self.assertIn(self.receipt_3, medication_manager.list_of_receipts.receipts)

        self.assertTrue(self.receipt_1.is_exist_med_obj(self.med_obj_1_rec_1))
        self.assertTrue(self.receipt_1.is_exist_med_obj(self.med_obj_2_rec_1))
        self.assertTrue(self.receipt_2.is_exist_med_obj(self.med_obj_3_rec_2))
        self.assertTrue(self.receipt_3.is_exist_med_obj(self.med_obj_4_rec_3))

        self.assertEqual(
            self.receipt_1.dict_of_medications_in_receipt[self.med_obj_1_rec_1],
            self.chars_1_rec_1,
        )
        self.assertEqual(
            self.receipt_1.dict_of_medications_in_receipt[self.med_obj_2_rec_1],
            self.chars_2_rec_1,
        )
        self.assertEqual(
            self.receipt_2.dict_of_medications_in_receipt[self.med_obj_3_rec_2],
            self.chars_3_rec_2,
        )
        self.assertEqual(
            self.receipt_3.dict_of_medications_in_receipt[self.med_obj_4_rec_3],
            self.chars_4_rec_3,
        )

    def test_get_list_of_med_objs_that_need_to_take_today_functionality(self):
        with patch("services.health_analysis.date") as mock_date:
            mock_date.today.return_value = real_date(2026, 1, 2)
            self.assertEqual(
                medication_manager.get_list_of_medications_that_need_to_take_today(),
                [self.med_obj_1_rec_1, self.med_obj_3_rec_2, self.med_obj_4_rec_3],
            )

    @patch(
        'services.health_analysis.MedicationAnalyzer.concrete_med_obj_in_receipt_is_completed',
        return_value=True,
    )
    def test_took_medication(self, mocked_method):
        medication_manager.took_medication_object(self.med_obj_3_rec_2)

        self.assertEqual(len(self.receipt_2.dict_of_medications_in_receipt), 0)
        self.assertEqual(len(medication_manager.list_of_receipts.receipts), 2)

        medication_manager.took_medication_object(self.med_obj_1_rec_1)

        self.assertEqual(len(self.receipt_1.dict_of_medications_in_receipt), 1)
        self.assertNotIn(
            self.med_obj_1_rec_1, self.receipt_1.dict_of_medications_in_receipt
        )

    def test_no_took_medication(self):
        day_2: HealthDaily = HealthDaily("2026-01-02")
        day_3: HealthDaily = HealthDaily("2026-01-03")
        day_4: HealthDaily = HealthDaily("2026-01-04")
        day_5: HealthDaily = HealthDaily("2026-01-05")
        # create and add day object to list of object for test
        # whether no_took_medication working correctly
        medication_manager.health_diary.add_day(day_2)
        medication_manager.health_diary.add_day(day_3)
        medication_manager.health_diary.add_day(day_4)
        medication_manager.health_diary.add_day(day_5)

        lst = medication_manager.get_list_of_all_medication_that_user_not_take()
        self.assertEqual(len(lst), 11)

        day_5.list_of_taken_medication.append(self.med_obj_1_rec_1)

        lst = medication_manager.get_list_of_all_medication_that_user_not_take()
        self.assertEqual(len(lst), 10)

        day_2.list_of_taken_medication.append(self.med_obj_1_rec_1)
        lst = medication_manager.get_list_of_all_medication_that_user_not_take()
        self.assertEqual(len(lst), 9)
