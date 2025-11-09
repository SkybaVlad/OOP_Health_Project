from services.body_metrics.body_metrics import BodyMetrics
from services.medication.medication import Medication, MedicationReminder
from data.body_metrics_container import BodyMetricsContainer
from data.body_metrics_container import BodyMetricsType
from services.user.user_body_goals import UserBodyGoals
from services.user.user_info import User
from services.activities.activity_type import SpecificActivityType
from data.activity_container import ActivityContainer
from services.user.user_body_info import UserBodyInfo


class Facade:
    def __init__(self, user: User):
        self.user_body_info = UserBodyInfo()
        self.body_metrics = BodyMetrics()
        self.body_metrics_container = BodyMetricsContainer()
        self.medication_reminder = MedicationReminder()
        self.activity_container = ActivityContainer()
        self.user_body_goals = UserBodyGoals(self.user_body_info, user)
        self.user = user
        # self.nutrition = Nutrition(total_calories)
        # self.sleep = Sleep(woke_up, went_to_sleep)

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

    def __add_body_metrics_to_container(self, metrics_type, metrics_value, data):
        self.body_metrics_container.add_body_metrics(metrics_type, metrics_value, data)

    def get_sleep_duration(self):
        return self.sleep.get_sleep_duration()

    def eat(self, calories, meal_name):
        self.nutrition.add_meals(calories, meal_name)

        consumed_calories = self.nutrition.get_consumed_calories()
        total_calories = self.nutrition.get_total_calories()

        if consumed_calories > total_calories:
            status = "Overate"  # add status to patient/user
            weight_to_add = (consumed_calories - total_calories) / 7700
            self.weight.add_weight(weight_to_add)
        else:
            status = "Eaten"  # add status to patient/user

    def get_consumed_calories(self):
        return self.nutrition.get_consumed_calories()

    def get_remaining_calories(self):
        return self.nutrition.get_remaining_calories()

    def add_activity(self, activity_name, burned_calories, start_time, end_time, date):
        activity_type_object = SpecificActivityType(
            activity_name, burned_calories, start_time, end_time
        )
        self.activity_container.add_activity(activity_type_object, date)

    def get_activities_in_specific_date(self, date_of_activities) -> list:
        return self.activity_container.get_activity_in_specific_date(date_of_activities)

    def get_history_of_all_activities(self) -> list:
        return self.activity_container.get_all_activities()

    def drink_water(self, amount_of_water):
        self.water.add_water(amount_of_water)

        consumed = self.water.get_consumed()
        total_goal = self.water.get_total_goal()

        if consumed > total_goal:
            status = "Overhydrated"  # add status to patient/user
        else:
            status = "Drinking"  # add status to patient/user

    def get_consumed_water(self):
        return self.water.get_consumed()

    def get_remaining_water(self):
        return self.water.get_remaining()

    # maybe add load_medicine_recipe()

    # def get_body_mass_index_metrics(self) -> float:
    #     return self.body_metrics.calculate_body_mass_index_metrics(
    #         self.user_body_info.get_weight(), self.user_body_info.get_height()
    #     )
    #
    # def get_basal_metabolic_rate_metrics(self) -> float:
    #     return self.body_metrics.calculate_basal_metabolic_rate_metrics(
    #         self.user_body_info.get_weight(),
    #         self.user_body_info.get_height(),
    #         self.user.get_age(),
    #         self.user.get_sex(),
    #     )
    #
    # def get_lean_body_mass_metrics(self) -> float:
    #     return self.body_metrics.calculate_lean_body_mass_metrics(
    #         self.user_body_info.get_weight(), self.user_body_info.get_fat_percentage()
    #     )
    #
    # def get_fat_mass_metrics(self) -> float:
    #     return self.body_metrics.calculate_fat_mass_metrics(
    #         self.user_body_info.get_weight(), self.user_body_info.get_fat_percentage()
    #     )

    def get_history_of_specific_metrics(self, metrics_type):
        pass

    def get_history_of_specific_metrics_in_some_period(
        self, metrics_type, start_date, end_date
    ) -> list:
        pass

    def get_history_of_specific_metrics_in_all_periods(
        self, metrics_type, start_date, end_date
    ) -> list:
        pass

    def add_medication(self, medicine_name, medication_dosage, time_to_take_medication):
        medication_object = Medication(medicine_name, medication_dosage)
        self.medication_reminder.add_to_journal_of_medication(
            medication_object, time_to_take_medication
        )
