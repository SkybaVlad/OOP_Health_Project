import math
from services.user.user_info import User
from enum import Enum
from services.user.user_body_info import UserBodyInfo


class BodyMetricsType(Enum):
    body_mass_index_metrics = 'bmi'
    basal_metabolic_rate = 'bmr'
    lean_body_mass = 'lbm'
    fat_mass = 'fm'
    weight = 'weight'
    height = 'height'
    fat_percentage = 'fp'
    percentage_of_water_level = 'fwl'


class BodyMetricsCalculator:
    def __init__(self, user_body_info: UserBodyInfo, user_info: User):
        self.user_body_info = user_body_info
        self.user_info = user_info

    def calculate_body_mass_index_metrics(self):
        return self.user_body_info.get_height() / math.pow(
            self.user_body_info.get_height() / 100, 2
        )

    def calculate_basal_metabolic_rate(self):
        if self.user_info.get_sex() == 'male':
            return (
                10 * self.user_body_info.get_weight()
                + 6.25 * self.user_body_info.get_height()
                - 5 * self.user_info.get_age()
                + 5
            )
        else:
            return (
                10 * self.user_body_info.get_weight()
                + 6.25 * self.user_body_info.get_height()
                - 5 * self.user_info.get_age()
                - 161
            )

    def calculate_lean_body_mass(self):
        return self.user_body_info.get_weight() * (
            1 - self.user_body_info.get_fat_percentage() / 100
        )

    def calculate_fat_mass(self):
        lean_body_mass_value = self.calculate_lean_body_mass()
        return self.user_body_info.get_weight() - lean_body_mass_value
