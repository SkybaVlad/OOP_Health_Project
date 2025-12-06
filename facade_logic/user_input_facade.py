from services.body_metrics.body_metrics_calculator import (
    BodyMetricsType,
)
from services.medication.medication import Medication, MedicationReminder
from services.user.user_body_goals import UserBodyDailyGoals
from services.user.user_info import User
from services.user.user_body_info import UserBodyInfo


class UserInputFacade:
    def __init__(self, user: User):
        self.user_body_info = UserBodyInfo()
        self.medication_reminder = MedicationReminder()
        self.user_body_daily_goals = UserBodyDailyGoals()
        self.user = user

    def get_weight(self):
        return self.user_body_info.get_weight()

    def get_height(self):
        return self.user_body_info.get_height()

    def get_fat_percentage(self):
        return self.user_body_info.get_fat_percentage()

    def get_percentage_of_water_level(self):
        return self.user_body_info.get_percentage_of_water_level()

    def get_body_mass_index(self):
        return self.user_body_info.get_body_mass_index()

    def get_basal_metabolic_rate(self):
        return self.user_body_info.get_basal_metabolic_rate()

    def get_lean_body_mass(self):
        return self.user_body_info.get_lean_body_mass()

    def get_fat_mass(self):
        return self.user_body_info.get_fat_mass()

    def set_weight(self, weight):
        try:
            self.user_body_info.set_weight(weight)
            self.facade_container.add_body_metrics()
        except ValueError as error:
            print(error)

    def set_height(self, height):
        try:
            self.user_body_info.set_height(height)
            self.facade_container.add_body_metrics(
                BodyMetricsType.height.value, height, '04.05.2025'
            )
        except ValueError as error:
            print(error)

    def set_fat_percentage(self, fat_percentage):
        try:
            self.user_body_info.set_fat_percentage(fat_percentage)
            self.facade_container.add_body_metrics(
                BodyMetricsType.fat_percentage.value, fat_percentage, '04.05.2025'
            )
        except ValueError as error:
            print(error)

    def set_percentage_of_water_level(self, percentage_of_water_level):
        try:
            self.user_body_info.set_percentage_of_water_level(percentage_of_water_level)
            self.facade_container.add_body_metrics(
                BodyMetricsType.percentage_of_water_level.value,
                percentage_of_water_level,
                '04.05.2025',
            )
        except ValueError as error:
            print(error)
