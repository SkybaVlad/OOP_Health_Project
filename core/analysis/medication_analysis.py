from datetime import date

from core.health_diary_container import HealthDiary
from core.medication.medication_objects import (
    Frequency,
    Medication,
    Interval,
    MedicationReceipt,
    MedicationReceiptList,
    MedicationObjectReceiptCharacteristic,
)
from core.validation_user_input.time_validator import time_in_period


class MedicationAnalyzer:
    """This class intended for analyze receipts amd medications object. Also this class implement methods
    that manages a list of receipts. For example if concrete receipt is end, we need delete this receipt from
    list of receipts"""

    def __init__(
        self, health_diary: HealthDiary, list_of_receipts: MedicationReceiptList
    ):
        self.health_diary = health_diary
        self.list_of_receipts: MedicationReceiptList | None = list_of_receipts

    def concrete_med_obj_in_receipt_is_completed(
        self, med_obj: Medication, characteristic: MedicationObjectReceiptCharacteristic
    ) -> bool:
        """This method check if concrete med_obj is completed inside a dict {med_obj : characteristic, ... , med_obj : characteristic
        if med_obj is completed -> delete this pair from receipt}"""
        if characteristic.interval == Interval.Forever.value:
            return False
        if characteristic.frequency == Frequency.Every_day.value:
            for day in self.health_diary.get_history_of_days():
                if time_in_period(
                    characteristic.start_time_of_interval,
                    characteristic.end_time_of_interval,
                    day.date_of_day,
                ):
                    if med_obj not in day.list_of_taken_medication:
                        return False
        elif characteristic.frequency == Frequency.SpecificDays.value:
            for day in self.health_diary.get_history_of_days():
                if day.name_of_day in characteristic.list_of_days:
                    if time_in_period(
                        characteristic.start_time_of_interval,
                        characteristic.end_time_of_interval,
                        day.date_of_day,
                    ):
                        if med_obj not in day.list_of_taken_medication:
                            return False
        return True

    def receipt_is_completed(self, receipt_obj: MedicationReceipt) -> bool:
        """This method checks if receipt (MedicationReceipt object) is completed. Is completed
        means that interval of all subreceipts is end and all medication inside subreceipts is taken in one time. Subreceipt means one pair
        (key (Medication): value (MedicationObjectReceiptCharacteristic)) inside receipt obj in dict_of_medications_in_receipt attribute.
        Subreceipts that has MedicationObjectReceiptCharacteristic object with interval = "Forever" never will end.
        """
        for med_obj in receipt_obj.dict_of_medications_in_receipt.keys():
            characteristic = receipt_obj.dict_of_medications_in_receipt[med_obj]
            if characteristic.interval == Interval.Forever.value:
                return False
        for med_obj in receipt_obj.dict_of_medications_in_receipt.keys():
            characteristic = receipt_obj.dict_of_medications_in_receipt[med_obj]
            if not characteristic.interval_is_end():
                return False
            if characteristic.frequency == Frequency.Every_day.value:
                for day in self.health_diary.get_history_of_days():
                    if time_in_period(
                        characteristic.start_time_of_interval,
                        characteristic.end_time_of_interval,
                        day.date_of_day,
                    ):
                        if med_obj not in day.list_of_taken_medication:
                            return False
            elif characteristic.frequency == Frequency.SpecificDays.value:
                for day in self.health_diary.get_history_of_days():
                    if day.name_of_day not in characteristic.list_of_days:
                        if time_in_period(
                            characteristic.start_time_of_interval,
                            characteristic.end_time_of_interval,
                            day.date_of_day,
                        ):
                            if med_obj not in day.list_of_taken_medication:
                                return False
        return True

    def get_list_of_medications_that_need_to_take_today(self) -> list[Medication]:
        """This method filter all meds objects (Medication class)
        from list_of_receipts object if data of curr day enter in interval of take this medication
        For example [{med_obj : characteristic}] if curr date in interval of characteristic (start_date: end_date)
        and frequency (for example if frequency = list of days, we need to check the current day name) is fitting
        """
        lst_of_med_objs_that_need_to_take_today = []
        for (
            medication_receipt_obj
        ) in self.list_of_receipts.get_list_of_all_available_receipts():
            for med_obj in medication_receipt_obj.dict_of_medications_in_receipt.keys():
                if not medication_receipt_obj.dict_of_medications_in_receipt[
                    med_obj
                ].interval_is_end():
                    if (
                        medication_receipt_obj.dict_of_medications_in_receipt[
                            med_obj
                        ].frequency
                        == Frequency.Every_day.value
                    ):
                        lst_of_med_objs_that_need_to_take_today.append(med_obj)
                    else:
                        if medication_receipt_obj.dict_of_medications_in_receipt[
                            med_obj
                        ].day_in_list_of_days(date.today().strftime("%A")):
                            lst_of_med_objs_that_need_to_take_today.append(med_obj)
        return lst_of_med_objs_that_need_to_take_today

    def get_list_of_all_medication_that_user_not_take(
        self,
    ) -> list[tuple[Medication, str]]:
        """This method return list of tuples, where each tuple is contains with medication
        object and data when this medication object user do not take."""
        lst: list[tuple[Medication, str]] = []
        for receipt in self.list_of_receipts.receipts:
            for med_obj in receipt.dict_of_medications_in_receipt:
                for day in self.health_diary.get_history_of_days():
                    date_of_day = date.fromisoformat(day.date_of_day)
                    name_of_day = date_of_day.strftime("%A")
                    if (
                        receipt.dict_of_medications_in_receipt[med_obj].frequency
                        == Frequency.Every_day.value
                        and med_obj not in day.list_of_taken_medication
                    ):
                        lst.append((med_obj, day.date_of_day))
                    elif (
                        receipt.dict_of_medications_in_receipt[med_obj].frequency
                        == Frequency.SpecificDays.value
                    ):
                        if (
                            name_of_day
                            in receipt.dict_of_medications_in_receipt[
                                med_obj
                            ].list_of_days
                            and med_obj not in day.list_of_taken_medication
                        ):
                            lst.append((med_obj, day.date_of_day))
        return lst
