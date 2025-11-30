from buisness.facade_container import FacadeContainer
from services.body_metrics.body_metrics import (
    StrategyBodyMetricsInterface,
    Context,
    StrategyBMICalculator,
    StrategyBMRCalculator,
    StrategyLeanBodyMassCalculator,
    StrategyFatMassCalculator,
)
from services.medication.medication import Medication, MedicationReminder
from services.user.user_body_goals import UserBodyGoals
from services.user.user_info import User
from services.user.user_body_info import UserBodyInfo
from services.nutrition.meal import Meal


class Facade:
    def __init__(self, user: User):
        self.user_body_info = UserBodyInfo()
        self.facade_container = FacadeContainer()
        self.strategy_context_body_metrics = Context()
        self.medication_reminder = MedicationReminder()
        self.user_body_goals = UserBodyGoals()
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
            self.__add_body_metrics_to_container(
                BodyMetricsType.weight.value, weight, '03.05.2025'
            )
        except ValueError as error:
            print(error)

    def set_height(self, height):
        try:
            self.user_body_info.set_height(height)
            self.__add_body_metrics_to_container(
                BodyMetricsType.height.value, height, '04.05.2025'
            )
        except ValueError as error:
            print(error)

    def set_fat_percentage(self, fat_percentage):
        try:
            self.user_body_info.set_fat_percentage(fat_percentage)
            self.__add_body_metrics_to_container(
                BodyMetricsType.fat_percentage.value, fat_percentage, '04.05.2025'
            )
        except ValueError as error:
            print(error)

    def set_percentage_of_water_level(self, percentage_of_water_level):
        try:
            self.user_body_info.set_percentage_of_water_level(percentage_of_water_level)
            self.__add_body_metrics_to_container(
                BodyMetricsType.percentage_of_water_level.value,
                percentage_of_water_level,
                '04.05.2025',
            )
        except ValueError as error:
            print(error)

    def get_sleep_duration(self):
        return self.sleep.get_sleep_duration()

    def add_meal(self, meal: Meal, data):
        self.meal_container.add_meals(meal, data)

    def get_consumed_calories(self):
        return self.nutrition.get_consumed_calories()

    def get_remaining_calories(self):
        return self.nutrition.get_remaining_calories()

    def get_consumed_water(self):
        return self.water.get_consumed()

    def get_remaining_water(self):
        return self.water.get_remaining()

    # maybe add load_medicine_recipe()

    def add_medication(self, medicine_name, medication_dosage, time_to_take_medication):
        medication_object = Medication(medicine_name, medication_dosage)
        self.medication_reminder.add_to_journal_of_medication(
            medication_object, time_to_take_medication
        )

    def calculate_matric(
        self,
        strategy_of_calculation_body_metrics: StrategyBodyMetricsInterface,
    ):
        self.strategy_context_body_metrics.set_strategy(
            strategy_of_calculation_body_metrics
        )
        return self.strategy_context_body_metrics.calculate()
