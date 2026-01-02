from unittest.mock import Mock, patch
import unittest
import datetime
from services.medication.medication_objects import (
    MedicationReceipt,
    Medication,
    MedicationReceiptList,
    MedicationCharacteristicBuilder,
)
from facade_logic.facade_dairy_manager import DairyFacade
from services.medication.medication_manager import MedicationManager
from services.health_analysis import MedicationAnalyzer
from services.health_daily.daily_health import HealthDaily
from data.health_diary_container import HealthDiary
from datetime import date


# create receipt with 2 medication objs
# create receipt with 1 medication objs

# get list of medication that need to take today

# take some medication -> view if medication added to list in day obj
# complete plan and check if meds objs deleted and receipts is deleted


class TestMedicationManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        first_day = HealthDaily(str(datetime.date.today()))
        health_diary = HealthDiary()

        list_of_receipts = MedicationReceiptList()

        medication_analyzer = MedicationAnalyzer(health_diary, list_of_receipts)

        cls.medication_manager = MedicationManager(list_of_receipts)
        cls.medication_manager.set_medication_analyzer(medication_analyzer)

        cls.facade_dairy = DairyFacade(health_diary, first_day, cls.medication_manager)

        builder = MedicationCharacteristicBuilder()

        cls.med_obj_1_rec_1 = Medication("Aspirin", "Capsule", "ml")

        cls.chars_1_rec_1 = (
            builder.set_medication_dosage_per_one_take(200)
            .set_frequency("Every day")
            .set_interval("Choose specific interval")
            .set_start_time(str(datetime.date.today()))
            .set_end_time("2026-01-07")
            .get_result()
        )

        cls.med_obj_2_rec_1 = Medication("No-Spa", "Tablet", "ml")
        cls.chars_2_rec_1 = (
            builder.reset()
            .set_medication_dosage_per_one_take(50)
            .set_frequency("Specific days")
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
            .set_frequency("Specific days")
            .set_list_of_days(["Tuesday", "Friday"])
            .set_interval("Choose specific interval")
            .set_start_time(str(datetime.date.today()))
            .set_end_time("2026-01-04")
            .get_result()
        )

        cls.receipt_3 = MedicationReceipt()
        cls.receipt_3.add_pair_to_receipt(cls.med_obj_4_rec_3, cls.chars_4_rec_3)

        cls.medication_manager.add_medication_receipt(cls.receipt_1)
        cls.medication_manager.add_medication_receipt(cls.receipt_2)
        cls.medication_manager.add_medication_receipt(cls.receipt_3)

    def test_creation_functionality(self):
        self.assertEqual(self.chars_1_rec_1.medication_dosage_per_one_take, 200)
        self.assertEqual(self.chars_1_rec_1.frequency, "Every day")
        self.assertEqual(self.chars_1_rec_1.list_of_days, None)
        self.assertEqual(self.chars_1_rec_1.interval, "Choose specific interval")

    def test_receipt_add_functionality(self):

        self.assertEqual(len(self.medication_manager.list_of_receipts.receipts), 3)

        self.assertIn(self.receipt_1, self.medication_manager.list_of_receipts.receipts)
        self.assertIn(self.receipt_2, self.medication_manager.list_of_receipts.receipts)
        self.assertIn(self.receipt_3, self.medication_manager.list_of_receipts.receipts)

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

        with patch("services.medication.medication_manager.date") as mock_date:
            mock_date.today.return_value = date(2026, 1, 2)
            self.assertEqual(
                self.medication_manager.get_list_of_medications_that_need_to_take_today(),
                [self.med_obj_1_rec_1, self.med_obj_3_rec_2, self.med_obj_4_rec_3],
            )

    @patch(
        'services.health_analysis.MedicationAnalyzer.concrete_med_obj_in_receipt_is_completed',
        return_value=True,
    )
    def test_took_medication(self, mocked_method):
        self.medication_manager.took_medication_object(self.med_obj_3_rec_2)

        self.assertEqual(len(self.receipt_2.dict_of_medications_in_receipt), 0)
        self.assertEqual(len(self.medication_manager.list_of_receipts.receipts), 2)

        self.medication_manager.took_medication_object(self.med_obj_1_rec_1)

        self.assertEqual(len(self.receipt_1.dict_of_medications_in_receipt), 1)
        self.assertNotIn(
            self.med_obj_1_rec_1, self.receipt_1.dict_of_medications_in_receipt
        )
