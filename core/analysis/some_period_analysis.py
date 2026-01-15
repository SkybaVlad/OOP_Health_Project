from typing import Any

from core.analysis.activity_analysis import ActivityAnalyzer
from core.analysis.medication_analysis import MedicationAnalyzer
from core.daily_health import HealthDaily
from core.validation_user_input.time_validator import (
    time_in_period,
)  # move this function
from core.activity.activity_type import SpecificActivityType


class HealthInSomePeriodAnalyzer:
    """This class responsible for analyze your metrics in some period that you define.
    Under hood this class iterate through a list of HealthDaily objects and analyze each object.
    This class provide a wide range of methods.

    - 1 day (set as default, when user registered at first)

    - 1 week

    - 1 month

    - 1 year

    - user_defined period
    """

    def __init__(self):
        self.list_of_days_that_in_period: list[HealthDaily] | None = None
        # need to know only about days that in period
        self.start_time: str | None = None
        self.end_time: str | None = None
        self.activity_analyzer: ActivityAnalyzer | None = None
        self.medication_analyzer: MedicationAnalyzer | None = None
        self.nutrition_analyzer: None = None

    def load_default_values_to_initialize(
        self,
        start_time: str,
        end_time: str,
        list_of_days_that_in_period: list[HealthDaily],
        activity_analyzer: ActivityAnalyzer,
        medication_analyzer: MedicationAnalyzer,
    ):
        self.list_of_days_that_in_period: list[HealthDaily] = (
            list_of_days_that_in_period
        )
        self.start_time = start_time
        self.end_time = end_time
        self.activity_analyzer = activity_analyzer
        self.medication_analyzer = medication_analyzer

    def set_list_of_days(self, list_of_health_diary: list[HealthDaily]):
        """"""
        self.list_of_days_that_in_period = get_list_of_days_in_some_period(
            self.start_time, self.end_time, list_of_health_diary
        )

    def set_period_of_time(self, start_time_of_period: str, end_time_of_period: str):
        self.start_time = start_time_of_period
        self.end_time = end_time_of_period

    def get_total_time_spent_on_activities_in_minutes_for_all_time(self) -> int:
        total_time_spent = 0
        for day in self.list_of_days_that_in_period:
            for activity in day.list_of_activities_for_day:
                total_time_spent += activity.calculate_activity_duration_in_minutes()
        return total_time_spent

    def get_total_consumed_calories_for_all_time(self) -> float:
        total_consumed_calories = 0.0
        for day in self.list_of_days_that_in_period:
            total_consumed_calories += day.consumed_calories_for_day
        return total_consumed_calories

    def get_total_burned_calories_for_all_time(self) -> float:
        total_burned_calories = 0.0
        for day in self.list_of_days_that_in_period:
            total_burned_calories += day.burned_calories_for_day
        return total_burned_calories

    def get_total_steps_for_all_time(self):
        total_steps = 0.0
        for day in self.list_of_days_that_in_period:
            total_steps += day.count_of_steps_for_day
        return total_steps

    def get_total_time_spent_on_specific_category_of_activities_for_all_time(
        self, activity_category
    ):
        total_time_spent = 0.0
        for day in self.list_of_days_that_in_period:
            for activity in day.list_of_activities_for_day:
                if activity.get_activity_category() == activity_category:
                    total_time_spent += (
                        activity.calculate_activity_duration_in_minutes()
                    )
        return total_time_spent

    def get_day_with_max_consumed_calories_for_all_time(self) -> HealthDaily | float:
        day_with_max_consumed_calories = self.list_of_days_that_in_period[0]
        for day in self.list_of_days_that_in_period:
            if day.consumed_calories_for_day > day_with_max_consumed_calories:
                day_with_max_consumed_calories = day.consumed_calories_for_day
        return day_with_max_consumed_calories

    def get_day_with_max_burned_calories_for_all_time(self) -> HealthDaily | float:
        day_with_max_burned_calories = self.list_of_days_that_in_period[0]
        for day in self.list_of_days_that_in_period:
            if day.burned_calories_for_day > day_with_max_burned_calories:
                day_with_max_burned_calories = day.burned_calories_for_day
        return day_with_max_burned_calories

    def get_day_with_max_steps_for_all_time(self) -> HealthDaily | float:
        day_with_max_steps = self.list_of_days_that_in_period[0]
        for day in self.list_of_days_that_in_period:
            if day.count_of_steps_for_day > day_with_max_steps:
                day_with_max_steps = day.count_of_steps_for_day
        return day_with_max_steps

    def get_day_with_max_time_spent_on_activities_for_all_time(
        self,
    ) -> HealthDaily | float:

        day_with_max_time_spent_on_activities = self.list_of_days_that_in_period[0]
        max_total_time_spent_on_activities = (
            day_with_max_time_spent_on_activities.total_time_spend_on_activities
        )

        for day in self.list_of_days_that_in_period:
            if day.total_time_spent_on_activities > max_total_time_spent_on_activities:
                max_total_time_spent_on_activities = day.total_time_spent_on_activities
                day_with_max_time_spent_on_activities = day
        return day_with_max_time_spent_on_activities

    def get_day_with_max_amount_of_drunk_water_for_some_period(
        self,
    ) -> HealthDaily | float:
        day_with_max_amount_of_drunk_water = self.list_of_days_that_in_period[0]
        for day in self.list_of_days_that_in_period:
            if day.drunk_water > day_with_max_amount_of_drunk_water.drunk_water:
                day_with_max_amount_of_drunk_water = day
        return day_with_max_amount_of_drunk_water

    def get_day_with_max_hours_spent_on_sleep_for_some_period(self):
        day_with_max_hours_of_sleep = self.list_of_days_that_in_period[0]
        for day in self.list_of_days_that_in_period:
            if day.sleep_duration > day_with_max_hours_of_sleep.sleep_duration:
                day_with_max_hours_of_sleep = day
        return day_with_max_hours_of_sleep

    def get_result_of_analyze_some_period(self) -> dict[str, Any]:
        return {
            "start_date": self.start_data,
            "end_date": self.end_data,
            "total_activity_time": self.get_total_time_spent_on_activities_in_minutes_for_all_time(),
            "total_consumed_calories": self.get_total_consumed_calories_for_all_time(),
            "total_burned_calories": self.get_total_burned_calories_for_all_time(),
            "total_steps": self.get_total_steps_for_all_time(),
        }
