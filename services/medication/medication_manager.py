from data.health_diary_container import HealthDiary
from services.health_analysis import MedicationAnalyzer
from services.medication.medication_objects import (
    MedicationReceiptList,
    MedicationReceipt,
    Medication,
)


def convert_list_of_medication_to_dict_with_status(
    list_of_medications: list[Medication],
) -> dict[Medication, bool]:
    """This functions convert list of Medication objects to dict with status. Status == False means that user don't
    take medication. Status == True means that user take medication. On start of day
    all medication objects has STATUS == False"""
    return {med_object: False for med_object in list_of_medications}


class MedicationManager:
    """This class is responsible for managing medication objects and receipts. This class
    provide a wide range of methods that allow to manage all receipts that user add and deliver
    lists of medication objects that need to take every day. If user is took medication object this class
    may delete receipts if user complete entire plan of receipts.

    This class has a list_of_receipts attribute of MedicationReceiptList type and
    medication_analyzer attribute of MedicationAnalyzer type"""

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(
        self, list_of_receipts: MedicationReceiptList, health_diary: HealthDiary
    ):
        if not hasattr(self, "initialize"):
            self.list_of_receipts: MedicationReceiptList = list_of_receipts
            self.medication_analyzer: MedicationAnalyzer | None = None
            self.health_diary: HealthDiary = health_diary
            self.initialize = True

    def add_medication_receipt(self, receipt: MedicationReceipt):
        """This method adds receipt object to list of receipts"""
        self.list_of_receipts.add_receipt(receipt)

    def set_medication_analyzer(self, medication_analyzer: MedicationAnalyzer):
        self.medication_analyzer = medication_analyzer

    def get_list_of_all_available_receipts(
        self,
    ) -> list[MedicationReceipt]:
        """This method return result of MedicationReceiptList.get_list_of_all_available_receipts method"""
        return self.list_of_receipts.get_list_of_all_available_receipts()

    def get_list_of_medications_that_need_to_take_today(self) -> list[Medication]:
        """This method return result of MedicationAnalyzer.get_list_of_medications_that_need_to_take_today method"""
        return (
            self.medication_analyzer.get_list_of_medications_that_need_to_take_today()
        )

    def took_medication_object(self, medication_object: Medication) -> None:
        """This method accept medication object that user is took and check that
        receipt is end. If yes - need delete receipt or if concrete interval of take some medication
        is end - need to delete this inside a receipt"""
        receipt_obj = self.list_of_receipts.find_receipt_with_appropriate_med_obj(
            medication_object
        )
        ...
        if receipt_obj is not None:
            if self.medication_analyzer.concrete_med_obj_in_receipt_is_completed(
                medication_object,
                receipt_obj.dict_of_medications_in_receipt[medication_object],
            ):
                self.delete_med_obj_inside_receipt(medication_object)
            if self.receipt_is_completed(receipt_obj):
                self.delete_receipt(receipt_obj)

    def no_took_medication(self, medication_object: Medication) -> None:
        pass

    def get_list_of_all_medication_that_user_not_take(
        self,
    ) -> list[tuple[Medication, str]]:
        return self.medication_analyzer.get_list_of_all_medication_that_user_not_take()

    def receipt_is_completed(self, receipt_obj: MedicationReceipt) -> bool:
        """This method return result of MedicationAnalyzer.receipt_is_completed method"""
        return self.medication_analyzer.receipt_is_completed(receipt_obj)

    def delete_receipt(self, _receipt_obj: MedicationReceipt):
        self.list_of_receipts.delete_receipt(_receipt_obj)

    def delete_med_obj_inside_receipt(self, medication_obj: Medication):
        receipt = self.list_of_receipts.find_receipt_with_appropriate_med_obj(
            medication_obj
        )
        receipt.remove_pair(medication_obj)
