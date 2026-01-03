import datetime
from abc import ABC, abstractmethod
from typing import Self

from services.validation_user_input.time_validator import (
    time_validator_format_yyyy_mm_dd,
)
from services.validation_user_input.time_validator import (
    is_source_time_less_than_target_time,
)
from services.validation_user_input.medication_validation import (
    validate_dosage,
    validate_medication_name,
)
from enum import Enum


class Frequency(Enum):
    SpecificDays = "Choose specific days"
    Every_day = "Every day"


class Interval(Enum):
    SpecificInterval = "Choose specific interval"
    Forever = "Forever"


class Medication:
    """This class describes a basic medication object that consists of the name of medication,
    form and unit_of_measurements. User can input name of medication object but form and unit_of_measurement params
    user can choose from list of available forms and units.

    User can input name attribute of medication object but form and unit_of_measurement params ser can choose from existing
    list of available forms and units."""

    def __init__(self, name: str, form, unit_of_measurements):
        try:
            validate_medication_name(name)
        except ValueError as e:
            pass
        except TypeError as e:
            pass
        self.name = name
        self.form = form
        self.unit_of_measurements = unit_of_measurements

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, Medication):
            return False
        if self.name != other.name:
            return False
        if self.form != other.form:
            return False
        if self.unit_of_measurements != other.unit_of_measurements:
            return False
        return True

    def __hash__(self):
        return hash((self.name, self.form, self.unit_of_measurements))

    def __str__(self):
        return f"{self.name} {self.form} {self.unit_of_measurements}"

    def __repr__(self):
        return f"Medication({self.name}, {self.form}, {self.unit_of_measurements})"


class MedicationObjectReceiptCharacteristic:
    """
    This class describes a characteristics of specific medication object in receipt. One medication object in receipt
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

    def interval_is_end(self) -> bool:
        date_obj_of_end_time_of_interval = datetime.date.fromisoformat(
            self.end_time_of_interval
        )
        if self.interval == Interval.Forever.value:
            return False
        if datetime.date.today() <= date_obj_of_end_time_of_interval:
            return False
        return True

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, MedicationObjectReceiptCharacteristic):
            return False
        if (
            self.medication_dosage_per_one_take == other.medication_dosage_per_one_take
            and self.frequency == other.frequency
            and self.list_of_days == other.list_of_days
            and self.interval == other.interval
            and self.start_time_of_interval == other.start_time_of_interval
            and self.end_time_of_interval == other.end_time_of_interval
        ):
            return True
        return False

    def __hash__(self):
        return hash(
            (
                self.medication_dosage_per_one_take,
                self.frequency,
                self.list_of_days,
                self.interval,
                self.start_time_of_interval,
                self.end_time_of_interval,
            )
        )

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

    def add_pair_to_receipt(
        self,
        medication_obj: Medication,
        medication_chars: MedicationObjectReceiptCharacteristic,
    ):
        if medication_obj not in self.dict_of_medications_in_receipt:
            self.dict_of_medications_in_receipt[medication_obj] = medication_chars
        else:
            self.dict_of_medications_in_receipt[medication_obj] = medication_chars

    def find_medication_chars(
        self, medication_obj: Medication
    ) -> MedicationObjectReceiptCharacteristic | None:
        for med_obj in self.dict_of_medications_in_receipt:
            if medication_obj == med_obj:
                return self.dict_of_medications_in_receipt[med_obj]
        return None

    def remove_pair(self, medication_obj: Medication):
        """This method remove medication and appropriate medication_chars from receipt"""
        if self.is_empty():
            del self
            return
        if self.is_exist_med_obj(medication_obj):
            self.dict_of_medications_in_receipt.pop(medication_obj)

    def is_exist_med_obj(self, _med_obj: Medication) -> bool:
        for med_obj in self.dict_of_medications_in_receipt.keys():
            if med_obj == _med_obj:
                return True
        return False

    def is_empty(self) -> bool:
        if len(self.dict_of_medications_in_receipt) == 0:
            return True
        return False

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, MedicationReceipt):
            return False
        if len(self.dict_of_medications_in_receipt) != len(
            other.dict_of_medications_in_receipt
        ):
            return False

        if self.dict_of_medications_in_receipt != other.dict_of_medications_in_receipt:
            return False
        return True

    def __hash__(self) -> int:
        raise NotImplementedError()

    def __str__(self):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()


class MedicationCharacteristicBuilderInterface(ABC):
    """This is the Interface class for all medication characteristic builders."""

    @abstractmethod
    def set_medication_dosage_per_one_take(self, medication_dosage: int) -> None:
        pass

    @abstractmethod
    def set_frequency(self, frequency: str) -> None:
        pass

    @abstractmethod
    def set_interval(self, interval: str) -> None:
        pass


class MedicationCharacteristicBuilder(MedicationCharacteristicBuilderInterface):
    """This is a builder class that responsible for building characteristic of medication.
    As each medication object has different characteristic (different days , different interval) - we
    need to provide an elasticity way to create characteristic of medication. For example if
    frequency = "Every day" -> we do not need to provide a list_of_days"""

    def __init__(self):
        self.med_chars: MedicationObjectReceiptCharacteristic = (
            MedicationObjectReceiptCharacteristic()
        )

    def reset(self) -> Self:
        self.med_chars = MedicationObjectReceiptCharacteristic()
        return self

    def set_medication_dosage_per_one_take(self, dosage: int) -> Self:
        try:
            validate_dosage(dosage)
        except ValueError as e:
            pass
        except TypeError as e:
            pass
        self.med_chars.set_medication_dosage_per_one_take(dosage)
        return self

    def set_frequency(self, frequency: str) -> Self:
        self.med_chars.set_frequency(frequency)
        return self

    def set_list_of_days(self, list_of_days: list) -> Self:
        self.med_chars.set_list_of_days(list_of_days)
        return self

    def set_interval(self, interval: str) -> Self:
        self.med_chars.set_interval(interval)
        return self

    def set_start_time(self, start_time: str) -> Self:
        try:
            time_validator_format_yyyy_mm_dd(start_time)
        except TypeError:
            pass
        except ValueError:
            pass
        self.med_chars.set_start_time(start_time)
        return self

    def set_end_time(self, end_time: str) -> Self:
        try:
            time_validator_format_yyyy_mm_dd(end_time)
        except TypeError:
            pass
        except ValueError:
            pass
        if not is_source_time_less_than_target_time(
            self.med_chars.start_time_of_interval,
            end_time,
        ):
            raise ValueError(
                "Start time of taking receipt can not be less than end time"
            )
        self.med_chars.set_end_time(end_time)
        return self

    def get_result(self) -> MedicationObjectReceiptCharacteristic:
        return self.med_chars


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

    def is_exist_receipt(self, receipt: MedicationReceipt) -> bool:
        """This method check whether receipt exists in receipt list"""
        for _receipt in self.receipts:
            if _receipt == receipt:
                return True
        return False

    def add_receipt(self, _receipt: MedicationReceipt):
        """This method add receipt to receipt list"""
        self.receipts.append(_receipt)

    def delete_receipt(self, receipt_obj: MedicationReceipt):
        """This method delete receipt from receipt list"""
        if self.is_exist_receipt(receipt_obj):
            self.receipts.remove(receipt_obj)

    def find_receipt_with_appropriate_med_obj(
        self, _med_obj: Medication
    ) -> MedicationReceipt | None:
        """This method find receipt with concrete med_object as key in dict and
        return receipt object from list of receipts"""
        for _receipt in self.receipts:
            if _med_obj in _receipt.dict_of_medications_in_receipt:
                return _receipt
        return None

    def get_list_of_all_available_receipts(
        self,
    ) -> list[MedicationReceipt]:
        """This method return list of all available receipts. Available means
        that either interval of receipt is end or not all medication inside receipt is taken
        """
        return self.receipts
