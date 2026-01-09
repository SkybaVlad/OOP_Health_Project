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


def calculate_body_mass_index_metrics(weight: float, height: float) -> float:
    if type(weight) != float:
        raise TypeError('weight must be float')
    if type(height) != float:
        raise TypeError('height must be float')
    if weight < 0:
        raise ValueError('weight must be positive')
    if height < 0:
        raise ValueError('height must be positive')
    return weight / math.pow(height / 100, 2)


def calculate_basal_metabolic_rate(
    user_sex: str, weight: float, height: float, age: int
) -> float:
    if type(weight) != float:
        raise TypeError('weight must be float')
    if type(height) != float:
        raise TypeError('height must be float')
    if weight < 0:
        raise ValueError('weight must be positive')
    if height < 0:
        raise ValueError('height must be positive')
    if type(user_sex) != str:
        raise ValueError("user sex must be str")
    if user_sex != 'Male' and user_sex != 'Female':
        raise ValueError("user sex should be 'Male' or 'Female'")
    if type(age) != int:
        raise ValueError("age must be int")
    if age < 0:
        raise ValueError('age must be positive')
    if user_sex == 'Male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161


def calculate_lean_body_mass(weight: float, fat_percentage: float) -> float:
    if type(weight) != float:
        raise TypeError("weight must be float")
    if type(fat_percentage) != float:
        raise TypeError("fat percentage must be float")
    if weight < 0:
        raise ValueError('weight must be positive')
    if fat_percentage < 0:
        raise ValueError("fat percentage must be positive")
    return weight * (1 - fat_percentage / 100)


def calculate_fat_mass(weight: float, lean_body_mass_value: float) -> float | int:
    if type(weight) != float:
        raise TypeError("weight must be float")
    if type(lean_body_mass_value) != float:
        raise TypeError("lean_body_mass_value must be float")
    if weight < 0:
        raise ValueError('weight must be positive')
    if lean_body_mass_value < 0:
        raise ValueError("lean_body_mass_value must be positive")
    return weight - lean_body_mass_value
