from abc import ABC, abstractmethod
from services.validation_user_input.time_validator import (
    time_validator_format_yyyy_mm_dd,
    time_in_period,
)
from datetime import date
from services.health_analysis import MedicationAnalyzer


# frequency -> in specific days | every day | arbitrary time
# interval -> specified by user (01.01.2025 - 01.01.2026) | at all time


class Medication:
    """This class describes a basic medication object that consists of the name of medication,
    form and unit_of_measurements"""

    def __init__(self, name: str, form, unit_of_measurements):
        self.name = name
        self.form = form
        self.unit_of_measurements = unit_of_measurements


class MedicationObjectReceiptCharacteristic:
    """This class describes a characteristics of specific medication object in receipt. One medication object in receipt
    can have a different characteristics.
    This object consist of such fields like dosage of medication per one take, frequency of take medication, list of days
    when need to take medication, interval of taking medication, start_time of interval (YYYY-MM-DD format) and
    end_time of interval (YYYY-MM-DD format)."""

    def __init__(self):
        self.medication_dosage_per_one_take = None
        self.frequency = None
        self.list_of_days = None
        self.interval = None
        self.start_time_of_interval = None
        self.end_time_of_interval = None

    def set_medication_dosage_per_one_take(self, medication_dosage_per_one_take):
        self.medication_dosage_per_one_take = medication_dosage_per_one_take

    def set_frequency(self, frequency):
        self.frequency = frequency

    def set_list_of_days(self, list_of_days):
        self.list_of_days = list_of_days

    def set_interval(self, interval):
        self.interval = interval

    def set_start_time(self, start_time: str):
        self.start_time_of_interval = time_validator_format_yyyy_mm_dd(start_time)
        self.start_time_of_interval = start_time

    def set_end_time(self, end_time: str):
        self.end_time_of_interval = time_validator_format_yyyy_mm_dd(end_time)
        self.end_time_of_interval = end_time


class MedicationReceipt:
    """This class responsible for building medication receipt object. One receipt object has a medication object as key
    and characteristic this medication object within a receipt as value"""

    def __init__(self):
        self.dict_of_medications_in_receipt = {}
        self.medication_object_that_adjust: Medication | None = None
        self.medication_object_characteristic_for_receipt: (
            MedicationObjectReceiptCharacteristic | None
        ) = None

    def create_medication_that_adjust_for_receipt(
        self, name: str, form: str, unit_of_measurements: str
    ):
        self.medication_object_that_adjust = Medication(
            name, form, unit_of_measurements
        )
        self.medication_object_characteristic_for_receipt = (
            MedicationObjectReceiptCharacteristic()
        )
        self.dict_of_medications_in_receipt[self.medication_object_that_adjust] = (
            self.medication_object_characteristic_for_receipt
        )

    def set_medication_dosage_per_one_take_to_specific_medication(
        self, medication_dosage: int
    ) -> None:
        self.medication_object_characteristic_for_receipt.set_medication_dosage_per_one_take(
            medication_dosage
        )

    def set_frequency(self, frequency: str) -> None:
        self.medication_object_characteristic_for_receipt.set_frequency(frequency)

    def set_list_of_days(self, list_of_days: list) -> None:
        self.medication_object_characteristic_for_receipt.set_list_of_days(list_of_days)

    def set_interval(self, interval: str) -> None:
        self.medication_object_characteristic_for_receipt.set_interval(interval)

    def set_start_time(self, start_time: str) -> None:
        time_validator_format_yyyy_mm_dd(start_time)
        self.medication_object_characteristic_for_receipt.set_start_time(start_time)

    def set_end_time(self, end_time: str) -> None:
        time_validator_format_yyyy_mm_dd(end_time)
        self.medication_object_characteristic_for_receipt.set_end_time(end_time)


# did not add set_interval method and set_list_of_days method because
# this methods is optional in some builders this methods do not uses, in some uses.
# In General contract for all builders I added only methods that's common for all builders
class ReceiptBuilderInterface(ABC):
    """This is a Interface class for all receipt Builders"""

    @abstractmethod
    def set_medication_object(self, name: str, form: str, unit_of_measurements: str):
        pass

    @abstractmethod
    def set_medication_dosage_per_one_take(self, medication_dosage: int) -> None:
        pass

    @abstractmethod
    def set_frequency(self, frequency: str) -> None:
        pass

    @abstractmethod
    def set_interval(self, interval: str) -> None:
        pass


class ReceiptBuilder(ReceiptBuilderInterface):
    """This is a builder class that responsible for building receipt. The receipt object has the next format
    [{med_obj_1: characteristics_1},...,{med_obj_n: characteristics_n}].
    So one receipt object has a different meds_objects and
    concrete meds_objects has own characteristic
    (characteristic is about how to take med, in which time and period like doctor said)
    where type(med_objs) is Medication class and type(characteristics) is MedicationReceipt class
    """

    def __init__(self):
        self.receipt = MedicationReceipt()

    def set_medication_object(
        self, medication_name: str, form: str, unit_of_measurements: str
    ) -> None:
        self.receipt.create_medication_that_adjust_for_receipt(
            medication_name, form, unit_of_measurements
        )

    def set_medication_dosage_per_one_take(self, medication_dosage: int) -> None:
        self.receipt.set_medication_dosage_per_one_take_to_specific_medication(
            medication_dosage
        )

    def set_frequency(self, frequency: str) -> None:
        self.receipt.set_frequency(frequency)

    def set_list_of_days(self, list_of_days: list) -> None:
        self.receipt.set_list_of_days(list_of_days)

    def set_interval(self, interval: str) -> None:
        self.receipt.set_interval(interval)

    def set_start_time(self, start_time: str) -> None:
        time_validator_format_yyyy_mm_dd(start_time)
        self.receipt.set_start_time(start_time)

    def set_end_time(self, end_time: str) -> None:
        time_validator_format_yyyy_mm_dd(end_time)
        self.receipt.set_end_time(end_time)

    def get_result(self) -> MedicationReceipt:
        return self.receipt


class MedicationReceiptList:
    """This class responsible for storage all receipts.
    Sometimes a receipts deleted from this list if user complete a plan
    List of receipts have the next format [{Medication_obj: MedicationObjectReceiptCharacteristic}, ..., ]
    """

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, "initialize"):
            self.receipts: list[MedicationReceipt] = []
            self.initialize = True

    def add_receipt(self, _receipt: MedicationReceipt):
        self.receipts.append(_receipt)

    def delete_receipt(self):
        pass

    def get_list_of_all_available_receipts(
        self,
    ) -> list[MedicationReceipt]:
        return self.receipts


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
        date_obj = date.fromisoformat(today_date)
        number_of_day = date_obj.weekday()
        today_day_name = dict_for_days[number_of_day]
        lst_of_med_objs_that_need_to_take_today = []
        for (
            medication_receipt_obj
        ) in self.list_of_receipts.get_list_of_all_available_receipts():
            med_obj = list(
                medication_receipt_obj.dict_of_medications_in_receipt.keys()
            )[0]
            if (
                receipt.dict_of_medications_in_receipt[med_obj].frequency == "everyday"
                and receipt.dict_of_medications_in_receipt[med_obj].interval == "always"
                or time_in_period(
                    receipt.dict_of_medications_in_receipt[
                        med_obj
                    ].start_time_of_interval,
                    receipt.dict_of_medications_in_receipt[
                        med_obj
                    ].end_time_of_interval,
                    today_date,
                )
            ):
                lst_of_med_objs_that_need_to_take_today.append(med_obj)
            elif (
                len(receipt.dict_of_medications_in_receipt[med_obj].list_of_days) != 0
                and receipt.dict_of_medications_in_receipt[med_obj].interval == "always"
                or time_in_period(
                    receipt.dict_of_medications_in_receipt[
                        med_obj
                    ].start_time_of_interval,
                    receipt.dict_of_medications_in_receipt[
                        med_obj
                    ].end_time_of_interval,
                    today_date,
                )
            ):
                if (
                    today_day_name
                    in receipt.dict_of_medications_in_receipt[med_obj].list_of_days
                ):
                    lst_of_med_objs_that_need_to_take_today.append(med_obj)
            elif (
                receipt.dict_of_medications_in_receipt[med_obj].frequency == "arbitrary"
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


dict_for_days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

if __name__ == '__main__':
    receipt_builder = ReceiptBuilder()
    receipt_builder.set_medication_object("Aspirin", "Capsule", "ml")
    receipt_builder.set_medication_dosage_per_one_take(200)
    receipt_builder.set_frequency("everyday")
    receipt_builder.set_interval("specific period")
    receipt_builder.set_start_time("2025-12-26")
    receipt_builder.set_end_time("2025-12-27")
    receipt_builder.set_medication_object("Paracetomol", "Tablet", "kg")
    receipt_builder.set_medication_dosage_per_one_take(100)
    receipt_builder.set_frequency("specific days")
    receipt_builder.set_list_of_days(["Monday", "Friday"])
    receipt_builder.set_interval("always")
    receipt_builder.set_medication_object("No-Spa", "Capsule", "ml")
    receipt_builder.set_frequency("arbitrary")
    receipt = receipt_builder.get_result()
