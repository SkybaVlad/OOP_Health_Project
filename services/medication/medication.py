from abc import ABC, abstractmethod
from services.time_logic import time_validator_format_yyyy_mm_dd


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
        self, name, form, unit_of_measurements
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
    def set_medication_object(self, name, form, unit_of_measurements):
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
    Sometimes a receipts deleted from this list if user complete a plan"""

    def __init__(self):
        self.receipts = []

    def add_receipt(self, receipt: MedicationReceipt):
        self.receipts.append(receipt)

    def delete_receipt(self):
        pass


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
