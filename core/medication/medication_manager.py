from core.dto_objects import MedicationDTO
from core.analysis.some_period_analysis import MedicationAnalyzer
from core.exceptions import NotExistingReceiptWithAppropriateMedicationObjectError
from core.medication.medication_objects import (
    MedicationReceiptList,
    MedicationReceipt,
    Medication,
)


def convert_list_of_medication_to_dict_with_status(
    list_of_medications: list[MedicationDTO],
) -> dict[MedicationDTO, bool]:
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

    def __init__(self, list_of_receipts: MedicationReceiptList):
        self.list_of_receipts: MedicationReceiptList = list_of_receipts
        self.medication_analyzer: MedicationAnalyzer | None = None

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

    def took_medication_object(
        self, medication_object: Medication, _receipt_with_med_obj: MedicationReceipt
    ) -> None:
        """This method accept medication object that user is took and check that
        receipt is end. If yes - need delete receipt or if concrete interval of take some medication
        is end - need to delete this inside a receipt"""
        if self.medication_obj_inside_receipt_is_completed(
            medication_object, _receipt_with_med_obj
        ):
            self.delete_med_obj_inside_receipt(medication_object)
        if self.receipt_is_completed(_receipt_with_med_obj):
            self.delete_receipt(_receipt_with_med_obj)

    def get_list_of_all_medication_that_user_not_take(
        self,
    ) -> list[tuple[Medication, str]]:
        return self.medication_analyzer.get_list_of_all_medication_that_user_not_take()

    def took_medication_object_with_no_today_date(self, medication_obj: Medication):
        _receipt_with_med_obj = (
            self.list_of_receipts.find_receipt_with_appropriate_med_obj(medication_obj)
        )

        if _receipt_with_med_obj is None:
            raise NotExistingReceiptWithAppropriateMedicationObjectError(
                f"{medication_obj.__repr__()} does not exist in list of receipts"
            )

        if self.medication_obj_inside_receipt_is_completed(
            medication_obj, _receipt_with_med_obj
        ):
            self.delete_med_obj_inside_receipt(medication_obj)
        if self.receipt_is_completed(_receipt_with_med_obj):
            self.delete_receipt(_receipt_with_med_obj)

    def medication_obj_inside_receipt_is_completed(
        self, medication_obj: Medication, receipt_: MedicationReceipt
    ) -> bool:
        return self.medication_analyzer.concrete_med_obj_in_receipt_is_completed(
            medication_obj, receipt_.dict_of_medications_in_receipt[medication_obj]
        )

    def receipt_is_completed(self, receipt_obj: MedicationReceipt) -> bool:
        """This method return result of MedicationAnalyzer.receipt_is_completed method"""
        return self.medication_analyzer.receipt_is_completed(receipt_obj)

    def delete_receipt(self, _receipt_obj: MedicationReceipt):
        self.list_of_receipts.delete_receipt(_receipt_obj)

    def delete_med_obj_inside_receipt(self, medication_obj: Medication):
        receipt = self.find_receipt_with_appropriate_med_obj(medication_obj)
        receipt.remove_pair(medication_obj)

    def find_receipt_with_appropriate_med_obj(
        self, medication_obj: Medication
    ) -> MedicationReceipt:
        return self.list_of_receipts.find_receipt_with_appropriate_med_obj(
            medication_obj
        )
