from datetime import date

from services.health_analysis import MedicationAnalyzer
from services.medication.medication_objects import (
    MedicationReceiptList,
    MedicationReceipt,
    Medication,
)
from services.validation_user_input.time_validator import time_in_period


def convert_list_of_medication_to_dict_with_status(
    list_of_medications: list[Medication],
) -> dict[Medication, bool]:
    """This functions convert list of Medication objects to dict with status. Status == False means that user don't
    take medication. Status == True means that user take medication. On start of day
    all medication objects has STATUS == False"""
    return {med_object: False for med_object in list_of_medications}


class MedicationManager:
    def __init__(self, list_of_receipts: MedicationReceiptList):
        self.list_of_receipts: MedicationReceiptList = list_of_receipts
        self.medication_analyzer: MedicationAnalyzer | None = None

    def add_medication_receipt(self, receipt: MedicationReceipt):
        self.list_of_receipts.add_receipt(receipt)

    def get_list_of_all_available_receipts(
        self,
    ) -> list[MedicationReceipt]:
        return self.list_of_receipts.get_list_of_all_available_receipts()

    def get_medications_that_need_to_take_today(self) -> dict[Medication, bool]:
        """This method filter all meds objects (Medication class)
        from list_of_receipts object if data of curr day enter in interval of take this medication
        For example [{med_obj : characteristic}] if curr date in interval of characteristic (start_date: end_date)
        and frequency (for example if frequency = list of days, we need to check the current day name) is fitting
        """
        today_date = str(date.today())
        today_day_name = date.today().strftime("%A")
        lst_of_med_objs_that_need_to_take_today = []
        for (
            medication_receipt_obj # -> {med_obj : char., ..., med_obj_n : char._n}
        ) in self.list_of_receipts.get_list_of_all_available_receipts():
            for med_obj in medication_receipt_obj.dict_of_medications_in_receipt.keys():
                if (
                    medication_receipt_obj.dict_of_medications_in_receipt[med_obj].frequency == "everyday"
                    and medication_receipt_obj.dict_of_medications_in_receipt[med_obj].interval == "always"
                    or time_in_period(
                        medication_receipt_obj.dict_of_medications_in_receipt[
                            med_obj
                        ].start_time_of_interval,
                        medication_receipt_obj.dict_of_medications_in_receipt[
                            med_obj
                        ].end_time_of_interval,
                        today_date,
                    )
                ):
                    lst_of_med_objs_that_need_to_take_today.append(med_obj)
                elif (
                    len(medication_receipt_obj.dict_of_medications_in_receipt[med_obj].list_of_days) != 0
                    and medication_receipt_obj.dict_of_medications_in_receipt[med_obj].interval == "always"
                    or time_in_period(
                        medication_receipt_obj.dict_of_medications_in_receipt[
                            med_obj
                        ].start_time_of_interval,
                        medication_receipt_obj.dict_of_medications_in_receipt[
                            med_obj
                        ].end_time_of_interval,
                        today_date,
                    )
                ):
                    if (
                        today_day_name
                        in medication_receipt_obj.dict_of_medications_in_receipt[med_obj].list_of_days
                    ):
                        lst_of_med_objs_that_need_to_take_today.append(med_obj)
                elif (
                    medication_receipt_obj.dict_of_medications_in_receipt[med_obj].frequency == "arbitrary"
                ):
                    lst_of_med_objs_that_need_to_take_today.append(med_obj)
        return convert_list_of_medication_to_dict_with_status(
            lst_of_med_objs_that_need_to_take_today
        )

    def took_medication_object(self, medication_object: Medication):
        ...
        receipt_obj = self.find_receipt_with_appropriate_med_obj(medication_object)
        ...
        if self.receipt_is_completed(receipt_obj):
            self.delete_receipt(receipt_obj)

    def receipt_is_completed(self, receipt_obj: MedicationReceipt) -> bool:
        return self.medication_analyzer.receipt_is_completed(receipt_obj)

    def delete_receipt(self, _receipt_obj: MedicationReceipt):
        lst = self.list_of_receipts.get_list_of_all_available_receipts()
        for receipt_obj in lst:
            if receipt_obj == _receipt_obj:
                lst.remove(receipt_obj)

    def find_receipt_with_appropriate_med_obj(
        self, medication_obj: Medication
    ) -> MedicationReceipt | None:
        # receipt_list = [{med_obj:characteristic},...,{}]
        for _receipt in self.list_of_receipts.get_list_of_all_available_receipts():
            if medication_obj in _receipt:
                return _receipt
        return None
