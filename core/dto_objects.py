from dataclasses import dataclass

from core.activity.activity_type import SpecificActivityType
from core.medication.medication_objects import Medication


@dataclass(frozen=True)
class ActivityTypeDTO:
    activity_category: str
    activity_name: str
    burned_calories: int
    start_time_of_activity: str
    end_time_of_activity: str


@dataclass(frozen=True)
class MedicationDTO:
    name: str
    form: str
    unit_of_measurements: str


@dataclass(frozen=True)
class DailyObjectDTO:
    date: str
    burned_calories: float
    consumed_calories: float
    activity: list[ActivityTypeDTO]  # -> specific activity type dto
    meal: list
    medication: list[MedicationDTO]  # medication dto
    water: float
    sleep_duration: float
    steps: float
    weight: float
    height: float
    fat_percentage: float
    activity_time: float
    name_of_day: str
    body_mass_index: float
    basal_metabolic_rate: float
    lean_body_mass_index: float
    fat_mass: float
    water_goal: float
    step_goal: float
    burned_calories_goal: float
    consumed_calories_goal: float


class SomePeriodAnalyzer:
    pass


def transfer_medication_obj_into_dict(medication_obj) -> dict:
    return {name: medication_obj.__dict__[name] for name in medication_obj.__dict__}


def generate_medication_dto_object(
    dict_info,
) -> MedicationDTO:  # {MedicationObj : False, ... , ....}
    return MedicationDTO(**dict_info)


def convert_medication_obj_into_medication_obj(medication_obj) -> MedicationDTO:
    return generate_medication_dto_object(
        transfer_medication_obj_into_dict(medication_obj)
    )


def convert_list_of_medications_into_list_of_medication_dto(
    list_of_medication: list[Medication],
) -> list[MedicationDTO]:
    return [
        convert_medication_obj_into_medication_obj(medication_obj)
        for medication_obj in list_of_medication
    ]


def transform_activity_obj_into_dict(activity_obj: SpecificActivityType) -> dict:
    return {name: activity_obj.__dict__[name] for name in activity_obj.__dict__}


def generate_activity_dto_object(dict_info) -> ActivityTypeDTO:
    return ActivityTypeDTO(**dict_info)


def convert_activity_obj_into_activity_dto(activity_obj) -> ActivityTypeDTO:
    return generate_activity_dto_object(transform_activity_obj_into_dict(activity_obj))


def generate_daily_dto_object(dict_info) -> DailyObjectDTO:
    # med_objs , activity_objs , meal_objs need convert into DTO types
    if len(dict_info["medication"]) != 0:
        dict_info["medication"] = [
            convert_medication_obj_into_medication_obj(med_obj)
            for med_obj in dict_info["medication"]
        ]
    if len(dict_info["activity"]) != 0:
        dict_info["activity"] = [
            convert_activity_obj_into_activity_dto(activity_obj)
            for activity_obj in dict_info["activity"]  # [activity obj, ... , ] error
        ]
    return DailyObjectDTO(**dict_info)
