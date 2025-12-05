from facade_logic.facade_container import FacadeContainer
from services.activities.activity_type import SpecificActivityType
from services.body_metrics.body_metrics import (
    StrategyBodyMetricsInterface,
    Context,
    StrategyBMICalculator,
    StrategyBMRCalculator,
    StrategyLeanBodyMassCalculator,
    StrategyFatMassCalculator,
    BodyMetricsType,
)
from services.medication.medication import Medication, MedicationReminder
from services.user.user_body_goals import UserBodyDailyGoals
from services.user.user_info import User
from services.user.user_body_info import UserBodyInfo
from services.nutrition.meal import Meal
from services.health_diary.daily_health_tracking import HealthDaily


class Facade:
    def __init__(self, user: User):
        self.user_body_info = UserBodyInfo()
        self.facade_container = FacadeContainer()
        self.strategy_context_body_metrics = Context()
        self.medication_reminder = MedicationReminder()
        self.user_body_goals = UserBodyDailyGoals()
        self.user = user
        self.health_diary = HealthDaily()

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

    # maybe add load_medicine_recipe()

    def add_activity(
        self, activity_object: SpecificActivityType, data_of_activity: str
    ) -> None:
        self.facade_container.activity_container.add_activity(
            activity_object, data_of_activity
        )
        # add activity object to the daily lists of activities
        # add burned calories to the daily burned calories

    def add_meal(self, meal: Meal, data):
        self.facade_container.meal_container.add_meal(meal, data)
        # add calories of meal to daily consumed calories
        # add meal to the daily meals
        # add meals to the meals container

    def add_body_metrics(self, metrics_type, value, data) -> None:
        self.facade_container.body_metrics_container.add_body_metrics(
            metrics_type, value, data
        )

    def add_medication(self, medicine_name, medication_dosage, time_to_take_medication):
        medication_object = Medication(medicine_name, medication_dosage)
        self.medication_reminder.add_to_journal_of_medication(
            medication_object, time_to_take_medication
        )

    def calculate_metrics(
        self,
        strategy_of_calculation_body_metrics: StrategyBodyMetricsInterface,
    ):
        self.strategy_context_body_metrics.set_strategy(
            strategy_of_calculation_body_metrics
        )
        return self.strategy_context_body_metrics.calculate()

    def get_daily_results(self):
        self.health_diary.

    def create_new_health_dairy(self):
        self.health_diary = HealthDaily()
