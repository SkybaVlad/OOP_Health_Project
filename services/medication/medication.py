from abc import ABC, abstractmethod
from services.time_logic import time_validator_format_yyyy_mm_dd


class Medication:
    def __init__(self):
        self.medication_name = None
        self.medication_dosage = None
        self.unit_of_measurements = None
        self.frequency = None
        self.list_of_days = None
        self.start_time = None
        self.end_time = None

    def set_medication_name(self, medication_name: str):
        self.medication_name = medication_name

    def set_medication_dosage(self, medication_dosage: str):
        self.medication_dosage = medication_dosage

    def set_unit_of_measurement(self, unit_of_measurement: str):
        self.unit_of_measurements = unit_of_measurement

    def set_frequency(self, frequency: str):
        self.frequency = frequency

    def set_list_of_days(self, list_of_days: list):
        self.list_of_days = list_of_days

    def set_start_time(self, start_time: str):
        time_validator_format_yyyy_mm_dd(start_time)
        self.start_time = start_time

    def set_end_time(self, end_time: str):
        time_validator_format_yyyy_mm_dd(end_time)
        self.end_time = end_time


class BuilderInterface(ABC):
    @abstractmethod
    def set_medication_name(self, medication_name: str):
        pass

    @abstractmethod
    def set_medication_dosage(self, medication_dosage: str):
        pass

    @abstractmethod
    def set_unit_of_measurement(self, unit_of_measurement: str):
        pass

    @abstractmethod
    def set_frequency(self, frequency: str):
        pass

    @abstractmethod
    def set_list_of_days(self, list_of_days: list):
        pass

    @abstractmethod
    def set_start_time(self, start_time: str):
        pass

    @abstractmethod
    def set_end_time(self, end_time: str):
        pass


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: BuilderInterface):
        self.builder = builder

    def make_product(self):
        if isinstance(self.builder, BuilderForEveryDayFrequency):
            pass
            self.builder.get_result()
        if isinstance(self.builder, BuilderForSpecifiedDaysFrequency):
            pass
            self.builder.get_result()


class BuilderForEveryDayFrequency(BuilderInterface):
    """This class responsible for building Medication product with every day frequency of getting"""

    def __init__(self, medication_product: Medication):
        self.medication_product = medication_product

    def set_medication_name(self, medication_name: str):
        self.medication_product.set_medication_name(medication_name)

    def set_medication_dosage(self, medication_dosage: str):
        self.medication_product.set_medication_dosage(medication_dosage)

    def set_unit_of_measurement(self, unit_of_measurement: str):
        self.medication_product.set_unit_of_measurement(unit_of_measurement)

    def set_frequency(self, frequency: str):
        self.medication_product.set_frequency(frequency)

    def set_list_of_days(self, list_of_days: list):
        self.medication_product.set_list_of_days(list_of_days)

    def set_start_time(self, start_time: str):
        self.medication_product.set_start_time(start_time)

    def set_end_time(self, end_time: str):
        self.medication_product.set_end_time(end_time)

    def get_result(self) -> Medication:
        return self.medication_product


class BuilderForSpecifiedDaysFrequency(BuilderInterface):
    """This class responsible for building Medication product with specific days of getting medication"""

    def __init__(self, medication_product: Medication):
        self.medication_product = medication_product

    def set_medication_name(self, medication_name: str):
        self.medication_product.set_medication_name(medication_name)

    def set_medication_dosage(self, medication_dosage: str):
        self.medication_product.set_medication_dosage(medication_dosage)

    def set_unit_of_measurement(self, unit_of_measurement: str):
        self.medication_product.set_unit_of_measurement(unit_of_measurement)

    def set_frequency(self, frequency: str):
        self.medication_product.set_frequency(frequency)

    def set_list_of_days(self, list_of_days: list):
        self.medication_product.set_list_of_days(list_of_days)

    def set_start_time(self, start_time: str):
        self.medication_product.set_start_time(start_time)

    def set_end_time(self, end_time: str):
        self.medication_product.set_end_time(end_time)

    def get_result(self) -> Medication:
        return self.medication_product


class BuilderForArbitraryFrequency(BuilderInterface):
    """This class responsible for building Medication product with arbitrary frequency of getting medication"""

    def __init__(self, medication_product: Medication):
        self.medication_product = medication_product

    def set_medication_name(self, medication_name: str):
        self.medication_product.set_medication_name(medication_name)

    def set_medication_dosage(self, medication_dosage: str):
        self.medication_product.set_medication_dosage(medication_dosage)

    def set_unit_of_measurement(self, unit_of_measurement: str):
        self.medication_product.set_unit_of_measurement(unit_of_measurement)

    def set_frequency(self, frequency: str):
        self.medication_product.set_frequency(frequency)

    def set_list_of_days(self, list_of_days: list):
        self.medication_product.set_list_of_days(list_of_days)

    def set_start_time(self, start_time: str):
        self.medication_product.set_start_time(start_time)

    def set_end_time(self, end_time: str):
        self.medication_product.set_end_time(end_time)

    def get_result(self) -> Medication:
        return self.medication_product
