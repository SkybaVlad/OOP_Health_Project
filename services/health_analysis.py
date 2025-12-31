from data.health_diary_container import HealthDiary
from services.body_metrics.body_metrics_calculator import (
    calculate_body_mass_index_metrics,
    calculate_lean_body_mass,
    calculate_fat_mass,
    calculate_basal_metabolic_rate,
)
from services.health_daily.daily_health import HealthDaily
from services.user.user_body_goals import UserBodyDailyGoals
from services.user.user_body_info import UserBodyInfo
from services.user.user_info import User
from services.time_logic import time_converter_minutes_in_hours
from services.medication.medication_objects import (
    MedicationReceiptList,
    Medication,
    MedicationObjectReceiptCharacteristic,
)
from services.medication.medication_objects import MedicationReceipt
from services.time_logic import get_list_of_all_dates_between_start_and_end
from services.validation_user_input.time_validator import (
    time_in_period,
)  # move this function


class HealthDailyAnalyzer:
    """This class responsible for analyze daily health. This class analyze a health_daily object and
    user_body_daily_goals and provide methods that return results of analysis"""

    def __init__(self):
        self.health_daily: HealthDaily | None = None
        self.user_body_daily_goals: UserBodyDailyGoals | None = None
        self.user_body_info: UserBodyInfo | None = None
        self.user: User | None = None

    def set_day_that_need_to_analyze(self, health_daily: HealthDaily):
        self.health_daily = health_daily

    def set_user_body_daily_goals(self, user_body_daily_goals: UserBodyDailyGoals):
        self.user_body_daily_goals = user_body_daily_goals

    def set_user_body_info(self, user_body_info: UserBodyInfo):
        self.user_body_info = user_body_info

    def set_user_info(self, user_info: User):
        self.user = user_info

    def get_total_time_spent_on_activities_in_minutes_current_day(self) -> float:
        return self.health_daily.total_time_spend_on_activities

    def get_remaining_of_consumed_calories(self) -> float:
        return (
            self.user_body_daily_goals.get_consumed_calories_goal()
            - self.health_daily.consumed_calories_for_day
        )

    def get_remaining_of_burned_calories(self) -> float:
        return (
            self.user_body_daily_goals.get_burned_calories_goal()
            - self.health_daily.burned_calories_for_day
        )

    def get_remaining_water(self) -> float:
        return (
            self.user_body_daily_goals.get_water_goal() - self.health_daily.drunk_water
        )

    def get_consumed_calories(self) -> float:
        return self.health_daily.consumed_calories_for_day

    def get_burned_calories(self) -> float:
        return self.health_daily.burned_calories_for_day

    def get_consumed_water(self) -> float:
        return self.health_daily.drunk_water

    def get_sleep_duration(self) -> float:
        return self.health_daily.sleep_duration

    def get_count_of_steps_for_day(self) -> float:
        return self.health_daily.count_of_steps_for_day

    def calculate_body_mass_index(self):
        if self.health_daily.weight is None and self.health_daily.height is not None:
            return calculate_body_mass_index_metrics(
                self.user_body_info.get_weight(), self.health_daily.height
            )
        if self.health_daily.weight is not None and self.health_daily.height is None:
            return calculate_body_mass_index_metrics(
                self.health_daily.weight, self.user_body_info.get_height()
            )
        if self.health_daily.weight is None and self.health_daily.height is None:
            return calculate_body_mass_index_metrics(
                self.user_body_info.get_weight(), self.user_body_info.get_height()
            )
        return calculate_body_mass_index_metrics(
            self.health_daily.weight, self.health_daily.height
        )

    def calculate_basal_metabolic_rate(self):
        if self.health_daily.weight is None and self.health_daily.height is not None:
            return calculate_basal_metabolic_rate(
                self.user.get_sex(),
                self.user_body_info.get_weight(),
                self.health_daily.height,
                self.user.get_age(),
            )
        if self.health_daily.weight is not None and self.health_daily.height is None:
            return calculate_basal_metabolic_rate(
                self.user.get_sex(),
                self.health_daily.weight,
                self.user_body_info.get_height(),
                self.user.get_age(),
            )
        if self.health_daily.weight is None and self.health_daily.height is None:
            return calculate_basal_metabolic_rate(
                self.user.get_sex(),
                self.user_body_info.get_weight(),
                self.user_body_info.get_height(),
                self.user.get_age(),
            )
        return calculate_basal_metabolic_rate(
            self.user.get_sex(),
            self.health_daily.weight,
            self.health_daily.height,
            self.user.get_age(),
        )

    def calculate_lean_body_mass_index(self):
        if (
            self.health_daily.weight is None
            and self.health_daily.fat_percentage is not None
        ):
            return calculate_lean_body_mass(
                self.user_body_info.get_weight(),
                self.user_body_info.get_fat_percentage(),
            )
        if self.health_daily.weight is not None and self.health_daily.height is None:
            return calculate_lean_body_mass(
                self.health_daily.weight, self.user_body_info.get_fat_percentage()
            )
        if (
            self.health_daily.weight is None
            and self.health_daily.fat_percentage is None
        ):
            return calculate_lean_body_mass(
                self.user_body_info.get_weight(),
                self.user_body_info.get_fat_percentage(),
            )
        return calculate_lean_body_mass(
            self.health_daily.weight, self.health_daily.fat_percentage
        )

    def calculate_fat_mass(self):
        lean_body_mass_value = self.calculate_lean_body_mass_index()
        if self.health_daily.weight is None:
            return calculate_fat_mass(
                self.user_body_info.get_weight(), lean_body_mass_value
            )
        return calculate_fat_mass(self.health_daily.weight, lean_body_mass_value)

    def get_daily_result(self):
        return (
            f"Daily result {self.health_daily.date_of_day}"
            f"Total time spent on activities - {self.get_total_time_spent_on_activities_in_minutes_current_day()}"
            f"Total amount of steps - {self.get_count_of_steps_for_day()}"
            f"Total hours of sleep - {self.get_sleep_duration()}"
            f"Total consumed calories - {self.get_consumed_calories()}"
            f"Total consumed water - {self.get_consumed_water()}"
            f"Total burned calories - {self.get_burned_calories()}"
            f"Remaining water - {self.get_remaining_water()}"
            f"Remaining burned calories - {self.get_remaining_of_burned_calories()}"
            f"Remaining consumed calories - {self.get_remaining_of_consumed_calories()}"
            f"Body Mass Metrics - {self.calculate_body_mass_index}"
            f"Basal Metabolic Rate - {self.calculate_basal_metabolic_rate}"
            f"Lean Body Mass Index - {self.calculate_lean_body_mass_index}"
            f"Fat Mass - {self.calculate_fat_mass}"
        )


class HealthInSomePeriodAnalyzer:
    """This class responsible for analyze a statistics on some period of time. This class analyze list of health_daily objects.
    Constructor accepts a list of health_daily objects and start_data, end_data. Start_data and end_data have next
    the str format YYYY-MM-DD
    """

    def __init__(self):
        self.list_health_diary: list[HealthDaily] | None = None
        self.start_data: str | None = None
        self.end_data: str | None = None

    def set_list_of_days(self, list_of_health_diary: list[HealthDaily]):
        self.list_health_diary = list_of_health_diary

    def set_period_of_time(self, start_time_of_period, end_time_of_period):
        self.start_data = start_time_of_period
        self.end_data = end_time_of_period

    def get_total_time_spent_on_activities_in_minutes_for_all_time(self) -> float:
        total_time_spent = 0.0
        for day in self.list_health_diary:
            for activity in day.list_of_activities_for_day:
                total_time_spent += activity.calculate_activity_duration_in_minutes()
        return total_time_spent

    def get_total_consumed_calories_for_all_time(self) -> float:
        total_consumed_calories = 0.0
        for day in self.list_health_diary:
            total_consumed_calories += day.consumed_calories_for_day
        return total_consumed_calories

    def get_total_burned_calories_for_all_time(self) -> float:
        total_burned_calories = 0.0
        for day in self.list_health_diary:
            total_burned_calories += day.burned_calories_for_day
        return total_burned_calories

    def get_total_steps_for_all_time(self):
        total_steps = 0.0
        for day in self.list_health_diary:
            total_steps += day.count_of_steps_for_day
        return total_steps

    def get_total_time_spent_on_specific_category_of_activities_for_all_time(
        self, activity_category
    ):
        total_time_spent = 0.0
        for day in self.list_health_diary:
            for activity in day.list_of_activities_for_day:
                if activity.get_activity_category() == activity_category:
                    total_time_spent += (
                        activity.calculate_activity_duration_in_minutes()
                    )
        return total_time_spent

    def get_day_with_max_consumed_calories_for_all_time(self) -> HealthDaily | float:
        if len(self.list_health_diary) == 0:
            return 0.0
        day_with_max_consumed_calories = self.list_health_diary[0]
        for day in self.list_health_diary:
            if day.consumed_calories_for_day > day_with_max_consumed_calories:
                day_with_max_consumed_calories = day.consumed_calories_for_day
        return day_with_max_consumed_calories

    def get_day_with_max_burned_calories_for_all_time(self) -> HealthDaily | float:
        if len(self.list_health_diary) == 0:
            return 0.0
        day_with_max_burned_calories = self.list_health_diary[0]
        for day in self.list_health_diary:
            if day.burned_calories_for_day > day_with_max_burned_calories:
                day_with_max_burned_calories = day.burned_calories_for_day
        return day_with_max_burned_calories

    def get_day_with_max_steps_for_all_time(self) -> HealthDaily | float:
        if len(self.list_health_diary) == 0:
            return 0.0
        day_with_max_steps = self.list_health_diary[0]
        for day in self.list_health_diary:
            if day.count_of_steps_for_day > day_with_max_steps:
                day_with_max_steps = day.count_of_steps_for_day
        return day_with_max_steps

    def get_day_with_max_time_spent_on_activities_for_all_time(
        self,
    ) -> HealthDaily | float:
        if len(self.list_health_diary) == 0:
            return 0.0
        day_with_max_time_spent_on_activities = self.list_health_diary[0]
        max_total_time_spent_on_activities = 0.0
        for (
            activity
        ) in day_with_max_time_spent_on_activities.list_of_activities_for_day:
            max_total_time_spent_on_activities += (
                activity.calculate_activity_duration_in_minutes()
            )
        total_time_spent_on_activities = 0.0
        for day in self.list_health_diary:
            for activity in day.list_of_activities_for_day:
                total_time_spent_on_activities += (
                    activity.calculate_activity_duration_in_minutes()
                )
            if total_time_spent_on_activities > max_total_time_spent_on_activities:
                max_total_time_spent_on_activities = total_time_spent_on_activities
                day_with_max_time_spent_on_activities = day
        return day_with_max_time_spent_on_activities

    def get_day_with_max_amount_of_drunk_water_for_all_time(
        self,
    ) -> HealthDaily | float:
        if len(self.list_health_diary) == 0:
            return 0.0
        day_with_max_amount_of_drunk_water = self.list_health_diary[0]
        for day in self.list_health_diary:
            if day.drunk_water > day_with_max_amount_of_drunk_water.drunk_water:
                day_with_max_amount_of_drunk_water = day
        return day_with_max_amount_of_drunk_water

    def get_day_with_max_hours_spent_on_sleep_for_all_time(self):
        if len(self.list_health_diary) == 0:
            return 0.0
        day_with_max_hours_of_sleep = self.list_health_diary[0]
        for day in self.list_health_diary:
            if day.sleep_duration > day_with_max_hours_of_sleep.sleep_duration:
                day_with_max_hours_of_sleep = day
        return day_with_max_hours_of_sleep

    def get_result_of_analyze_some_period(self) -> str:
        day_with_max_consumed_calories = (
            self.get_day_with_max_consumed_calories_for_all_time()
        )
        day_with_max_burned_calories = (
            self.get_day_with_max_burned_calories_for_all_time()
        )
        day_with_max_steps = self.get_day_with_max_steps_for_all_time()
        day_with_max_time_spent_on_activities = (
            self.get_day_with_max_time_spent_on_activities_for_all_time()
        )
        day_with_max_amount_of_drunk_water = (
            self.get_day_with_max_amount_of_drunk_water_for_all_time()
        )
        day_with_max_hours_of_sleep = (
            self.get_day_with_max_hours_spent_on_sleep_for_all_time()
        )
        return (
            f"Statistics from {self.start_data} to {self.end_data}"
            f"Total time spent on activities {time_converter_minutes_in_hours(self.get_total_time_spent_on_activities_in_minutes_for_all_time())}"
            f"Total consumed calories {self.get_total_consumed_calories_for_all_time()}"
            f"Total burned calories {self.get_total_burned_calories_for_all_time()}"
            f"Total steps {self.get_total_steps_for_all_time()}"
            f"Total time spent on Cardio activity {self.get_total_time_spent_on_specific_category_of_activities_for_all_time("Cardio")}"
            f"Total time spent on Sport activity {self.get_total_time_spent_on_specific_category_of_activities_for_all_time("Sport")}"
            f"Day with max consumed calories {day_with_max_consumed_calories.date_of_day} - {day_with_max_consumed_calories.consumed_calories_for_day}"
            f"Day with max burned calories {day_with_max_burned_calories.date_of_day} - {day_with_max_burned_calories.burned_calories_for_day}"
            f"Day with max amount of steps {day_with_max_steps.date_of_day} - {day_with_max_steps.count_of_steps_for_day}"
            f"Day with max time spent on activities {day_with_max_time_spent_on_activities.date_of_day} - {day_with_max_time_spent_on_activities.total_time_spend_on_activities}"
            f"Day with max amount of drunk water {day_with_max_amount_of_drunk_water.date_of_day} - {day_with_max_amount_of_drunk_water.drunk_water}"
            f"Day with max hours of sleep {day_with_max_hours_of_sleep.date_of_day} - {day_with_max_hours_of_sleep.sleep_duration}"
        )


class MedicationAnalyzer:
    """This class intended for analyze receipts amd medications object. Also this class implement methods
    that manages a list of receipts. For example if concrete receipt is end, we need delete this receipt from
    list of receipts"""

    def __init__(self, health_diary: HealthDiary):
        self.health_diary = health_diary
        self.list_of_receipts: MedicationReceiptList | None = None

    def set_list_of_receipts(self, list_of_receipts: MedicationReceiptList) -> None:
        self.list_of_receipts = list_of_receipts

    def concrete_med_obj_in_receipt_is_completed(
        self, med_obj: Medication, characteristic: MedicationObjectReceiptCharacteristic
    ) -> bool:
        """This method check if concrete med_obj is completed inside a dict {med_obj : characteristic, ... , med_obj : characteristic
        if med_obj is completed -> delete this pair from receipt}"""
        if characteristic.interval == "Forever":
            return False
        if characteristic.interval == "Choose specific interval":
            if characteristic.frequency == "Every day":
                for day in self.health_diary.get_history_of_days():
                    if time_in_period(
                        characteristic.start_time_of_interval,
                        characteristic.end_time_of_interval,
                        day.date_of_day,
                    ):
                        if med_obj not in day.list_of_taken_medication:
                            return False
            elif characteristic.frequency == "Specific days":
                for day in self.health_diary.get_history_of_days():
                    if day.name_of_day in characteristic.list_of_days:
                        if time_in_period(
                            characteristic.start_time_of_interval,
                            characteristic.end_time_of_interval,
                            day.date_of_day,
                        ):
                            if med_obj not in day.list_of_taken_medication:
                                return False
        return True

    def receipt_is_completed(self, receipt_obj: MedicationReceipt) -> bool:
        """This method checks if receipt (MedicationReceipt object) is completed."""
        for med_obj in receipt_obj.dict_of_medications_in_receipt.keys():
            characteristic = receipt_obj.dict_of_medications_in_receipt[med_obj]
            if characteristic.interval == "Forever":
                return False
        for med_obj in receipt_obj.dict_of_medications_in_receipt.keys():
            characteristic = receipt_obj.dict_of_medications_in_receipt[med_obj]
            if characteristic.frequency == "Everyday":
                for day in self.health_diary.get_history_of_days():
                    if time_in_period(
                        characteristic.start_time_of_interval,
                        characteristic.end_time_of_interval,
                        day.date_of_day,
                    ):
                        if med_obj not in day.list_of_taken_medication:
                            return False
            elif characteristic.frequency == "Specific days":
                for day in self.health_diary.get_history_of_days():
                    if day.name_of_day not in characteristic.list_of_days:
                        if time_in_period(
                            characteristic.start_time_of_interval,
                            characteristic.end_time_of_interval,
                            day.date_of_day,
                        ):
                            if med_obj not in day.list_of_taken_medication:
                                return False
        return True
