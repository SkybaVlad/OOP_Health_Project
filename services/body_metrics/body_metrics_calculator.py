import math
from enum import Enum


class BodyMetricsType(Enum):
    body_mass_index_metrics = 'bmi'
    basal_metabolic_rate = 'bmr'
    lean_body_mass = 'lbm'
    fat_mass = 'fm'
    weight = 'weight'
    height = 'height'
    fat_percentage = 'fp'
    percentage_of_water_level = 'fwl'


def calculate_body_mass_index_metrics(weight, height) -> float:
    return weight / math.pow(height / 100, 2)


def calculate_basal_metabolic_rate(user_sex, weight, height, age) -> float:
    if user_sex == 'male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161


def calculate_lean_body_mass(weight, fat_percentage):
    return weight * (1 - fat_percentage / 100)


def calculate_fat_mass(weight, lean_body_mass_value):
    return weight - lean_body_mass_value
