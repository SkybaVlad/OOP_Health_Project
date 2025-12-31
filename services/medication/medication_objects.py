from abc import ABC, abstractmethod
from datetime import date

from services.validation_user_input.time_validator import (
    time_validator_format_yyyy_mm_dd,
    time_in_period,
)
from services import health_analysis
from services.validation_user_input.time_validator import (
    is_source_time_less_than_target_time,
)
from services.validation_user_input.medication_validation import (
    validate_dosage,
    validate_medication_name,
)


class Medication:
    """This class describes a basic medication object that consists of the name of medication,
    form and unit_of_measurements. User can input name of medication object but form and unit_of_measurement params
    user can choose from list of available forms and units.

    User can input name attribute of medication object but form and unit_of_measurement params ser can choose from existing
    list of available forms and units."""

    def __init__(self, name: str, form, unit_of_measurements):
        self.name = name
        self.form = form
        self.unit_of_measurements = unit_of_measurements

    def __str__(self):
        return f"{self.name} {self.form} {self.unit_of_measurements}"

    def __repr__(self):
        return f"Medication({self.name}, {self.form}, {self.unit_of_measurements})"


class MedicationObjectReceiptCharacteristic:
    """This class describes a characteristics of specific medication object in receipt. One medication object in receipt
    can have a different characteristics.
    This object consist of such fields like dosage of medication per one take, frequency of take medication, list of days
    when need to take medication, interval of taking medication, start_time of interval (YYYY-MM-DD format) and
    end_time of interval (YYYY-MM-DD format).
    Some of this attribute like medication_dosage_per_one_take user need to input manually user need input manually but
    such attributes as frequency, list_of_days, interval user can only choose from existing list of values.

    For example for frequency -> ["Every day","Specific days"]

    For list_of_days -> ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    For interval -> ["Forever","Choose specific interval"]"""

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

    def __str__(self):
        return (
            f"Characteristic of concrete medication object with such property like "
            f"frequency of taking medication={self.frequency},"
            f"dosage that need to take per one time={self.medication_dosage_per_one_take},"
            f"days when need to take medication={",".join(self.list_of_days)},"
            f"interval of receipt = {self.interval},"
            f"start_time_of_interval={self.start_time_of_interval},"
            f"end_time_of_interval={self.end_time_of_interval}"
        )


class MedicationReceipt:
    """This class responsible for building medication receipt object. This object has next attribute like dict_of_medications_in_receipt
    in which store medication object (Medication) as key and object of MedicationObjectReceiptCharacteristic class as value

    dict_of_medications_in_receipt = {Medication: MedicationObjectReceiptCharacteristic}

    dict_of_medications_in_receipt = {Medication: MedicationObjectReceiptCharacteristic}

    Next attributes of this class it's the object of Medication class and object of MedicationObjectReceiptCharacteristic class

    In dict attribute we can have several Medication object with several MedicationObjectReceiptCharacteristic objects
    """

    def __init__(self):
        self.dict_of_medications_in_receipt: dict[
            Medication, MedicationObjectReceiptCharacteristic
        ] = {}
        self.last_added_med_obj_characteristic_for_receipt: (
            MedicationObjectReceiptCharacteristic | None
        ) = None

    def add_medication_that_adjust_for_receipt(
        self, name: str, form: str, unit_of_measurements: str
    ):
        medication_obj = Medication(name, form, unit_of_measurements)
        self.last_added_med_obj_characteristic_for_receipt = (
            MedicationObjectReceiptCharacteristic()
        )
        self.dict_of_medications_in_receipt[medication_obj] = (
            self.last_added_med_obj_characteristic_for_receipt
        )

    def set_medication_dosage_per_one_take_to_specific_medication(
        self, medication_dosage: int
    ) -> None:
        self.last_added_med_obj_characteristic_for_receipt.set_medication_dosage_per_one_take(
            medication_dosage
        )

    def set_frequency(self, frequency: str) -> None:
        self.last_added_med_obj_characteristic_for_receipt.set_frequency(frequency)

    def set_list_of_days(self, list_of_days: list) -> None:
        self.last_added_med_obj_characteristic_for_receipt.set_list_of_days(
            list_of_days
        )

    def set_interval(self, interval: str) -> None:
        self.last_added_med_obj_characteristic_for_receipt.set_interval(interval)

    def set_start_time(self, start_time: str) -> None:
        time_validator_format_yyyy_mm_dd(start_time)
        self.last_added_med_obj_characteristic_for_receipt.set_start_time(start_time)

    def set_end_time(self, end_time: str) -> None:
        time_validator_format_yyyy_mm_dd(end_time)
        self.last_added_med_obj_characteristic_for_receipt.set_end_time(end_time)

    def __str__(self):
        return f""

    def __repr__(self):
        pass


class ReceiptBuilderInterface(ABC):
    """This is the Interface class for all receipt builders"""

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
        """we don't need to validate "form" param because user can't input this param manually only can choose from
        existing list of available values. It's also concern a unit_of_measurements param
        """
        try:
            validate_medication_name(medication_name)
        except TypeError:
            pass
        except ValueError:
            pass
        self.receipt.add_medication_that_adjust_for_receipt(
            medication_name, form, unit_of_measurements
        )

    def set_medication_dosage_per_one_take(self, medication_dosage: int) -> None:
        try:
            validate_dosage(medication_dosage)
        except TypeError:
            pass
        except ValueError:
            pass
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
        if not is_source_time_less_than_target_time(
            self.receipt.last_added_med_obj_characteristic_for_receipt.start_time_of_interval,
            end_time,
        ):
            raise ValueError(
                "Start time of taking receipt can not be less than end time"
            )
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
