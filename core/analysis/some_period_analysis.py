from typing import Any

from core.analysis.activity_analysis import ActivityAnalyzer
from core.analysis.medication_analysis import MedicationAnalyzer
from core.daily_health import HealthDaily
from core.analysis.function import get_list_of_days_in_some_period
from core.body_metrics_calculator import (
    calculate_body_mass_index_metrics,
    calculate_fat_mass,
    calculate_lean_body_mass,
    calculate_basal_metabolic_rate,
)


def sort_days(list_of_days_in_period: list[HealthDaily]):
    return sorted(list_of_days_in_period, key=lambda day: day.date_of_day)


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

        list_of_days_in_some_period = get_list_of_days_in_some_period(
            self.start_time, self.end_time, list_of_health_diary
        )
        self.list_of_days_that_in_period = list_of_days_in_some_period

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

    def get_total_drunk_water_for_all_time(self) -> float:
        total_drunk_water = 0
        for day in self.list_of_days_that_in_period:
            total_drunk_water += day.drunk_water
        return total_drunk_water

    def get_total_sleep_time_for_all_time(self) -> float:
        total_sleep_time = 0
        for day in self.list_of_days_that_in_period:
            total_sleep_time += day.sleep_duration
        return total_sleep_time

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

    def get_burned_calories_for_each_day_in_period(self):
        burned_calories_for_each_day = []
        for day in self.list_of_days_that_in_period:
            burned_calories_for_each_day.append(day.burned_calories_for_day)
        return burned_calories_for_each_day

    def get_total_activity_for_each_day_in_period(self):
        total_activity_for_each_day = []
        for day in self.list_of_days_that_in_period:
            total_activity_for_each_day.append(day.total_time_spend_on_activities)
        return total_activity_for_each_day

    def get_consumed_calories_for_each_day_in_period(self):
        consumed_calories_for_each_day = []
        for day in self.list_of_days_that_in_period:
            consumed_calories_for_each_day.append(day.consumed_calories_for_day)

        return consumed_calories_for_each_day

    def get_steps_value_for_each_day_in_period(self):
        steps_value_for_each_day = []
        for day in self.list_of_days_that_in_period:
            steps_value_for_each_day.append(day.count_of_steps_for_day)
        return steps_value_for_each_day

    def get_drunk_water_for_each_day_in_period(self):
        drunk_water_value_for_each_day_in_period = []
        for day in self.list_of_days_that_in_period:
            drunk_water_value_for_each_day_in_period.append(day.drunk_water)

        return drunk_water_value_for_each_day_in_period

    def get_sleep_time_for_each_day_in_period(self):
        sleep_time_for_each_day_in_period = []
        for day in self.list_of_days_that_in_period:
            sleep_time_for_each_day_in_period.append(day.sleep_duration)
        return sleep_time_for_each_day_in_period

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

    def is_empty_list(self):
        if len(self.list_of_days_that_in_period) == 0:
            return True
        return False

    def get_avg_burned_calories(self):
        if self.is_empty_list():
            return 0
        return self.get_total_burned_calories_for_all_time() / len(
            self.list_of_days_that_in_period
        )

    def get_avg_consumed_calories(self):
        if self.is_empty_list():
            return 0
        return self.get_total_consumed_calories_for_all_time() / len(
            self.list_of_days_that_in_period
        )

    def get_avg_steps(self):
        if self.is_empty_list():
            return 0
        return self.get_total_steps_for_all_time() / len(
            self.list_of_days_that_in_period
        )

    def get_avg_drunk_water(self):
        if self.is_empty_list():
            return 0
        return self.get_total_drunk_water_for_all_time() / len(
            self.list_of_days_that_in_period
        )

    def get_avg_sleep_duration(self):
        if self.is_empty_list():
            return 0
        return self.get_total_sleep_time_for_all_time() / len(
            self.list_of_days_that_in_period
        )

    def get_avg_activity_time(self):
        if self.is_empty_list():
            return 0
        return self.get_total_time_spent_on_activities_in_minutes_for_all_time() / len(
            self.list_of_days_that_in_period
        )

    def get_avg_weight(self):
        if self.is_empty_list():
            return 0
        array = []
        for day in self.list_of_days_that_in_period:
            if day.weight != 0:
                array.append(day.weight)
        if len(array) == 0:
            return 0
        return sum(array) / len(array)

    def get_avg_height(self):
        if self.is_empty_list():
            return 0
        array = []
        for day in self.list_of_days_that_in_period:
            if day.height != 0:
                array.append(day.height)
        if len(array) == 0:
            return 0
        return sum(array) / len(array)

    def get_avg_fat_percentage(self):
        if self.is_empty_list():
            return 0
        array = []
        for day in self.list_of_days_that_in_period:
            if day.fat_percentage != 0:
                array.append(day.fat_percentage)

        if len(array) == 0:
            return 0
        return sum(array) / len(array)

    def get_avg_bmi(self):
        if self.is_empty_list():
            return 0
        array = []
        for day in self.list_of_days_that_in_period:
            if day.weight != 0 and day.height != 0:
                array.append(calculate_body_mass_index_metrics(day.weight, day.height))
        if len(array) == 0:
            return 0
        return sum(array) / len(array)

    def get_days_labels(self):
        list_of_days = sort_days(self.list_of_days_that_in_period)

        result = []

        for day in list_of_days:
            date_value = day.date_of_day

            if isinstance(date_value, str):
                result.append(date_value[5:])
            else:
                result.append(date_value.strftime("%b %d"))

        return result

    def get_weight_for_each_day_in_period(self):
        result = []

        for day in sort_days(self.list_of_days_that_in_period):
            result.append(day.weight)

        return result

    def get_bmi_for_each_day_in_period(self):
        result = []

        for day in sort_days(self.list_of_days_that_in_period):
            if day.weight != 0 and day.height != 0:
                bmi = calculate_body_mass_index_metrics(day.weight, day.height)
                result.append(bmi)
            else:
                result.append(0)

        return result

    # def get_avg_bmr(self):
    #     array = []
    #     for day in self.list_of_days_that_in_period:
    #         if day.weight != 0 and day.height != 0:
    #             day.append(calculate_lean_body_mass(day.weight, day.height))
    #     return sum(array) / len(array)

    def get_result_of_analyze_some_period(self) -> dict[str, Any]:
        return {
            "start_date": self.start_time,
            "end_date": self.end_time,
            "days_labels": self.get_days_labels(),
            "total_activity_time": self.get_total_time_spent_on_activities_in_minutes_for_all_time(),
            "total_consumed_calories": self.get_total_consumed_calories_for_all_time(),
            "total_burned_calories": self.get_total_burned_calories_for_all_time(),
            "total_steps": self.get_total_steps_for_all_time(),
            "total_drunk_water": self.get_total_drunk_water_for_all_time(),
            "total_sleep_hours": self.get_total_sleep_time_for_all_time(),
            "burned_calories_value_for_each_day": self.get_burned_calories_for_each_day_in_period(),
            "consumed_calories_value_for_each_day": self.get_consumed_calories_for_each_day_in_period(),
            "steps_value_for_each_day": self.get_steps_value_for_each_day_in_period(),
            "drunk_water_value_for_each_day": self.get_drunk_water_for_each_day_in_period(),
            "sleep_duration_value_for_each_day": self.get_sleep_time_for_each_day_in_period(),
            "activity_time_value_for_each_day": self.get_total_activity_for_each_day_in_period(),
            "weight_value_for_each_day": self.get_weight_for_each_day_in_period(),
            "bmi_value_for_each_day": self.get_bmi_for_each_day_in_period(),
            "avg_burned_calories": self.get_avg_burned_calories(),
            "avg_consumed_calories": self.get_avg_consumed_calories(),
            "avg_steps": self.get_avg_steps(),
            "avg_drunk_water": self.get_avg_drunk_water(),
            "avg_sleep_hours": self.get_avg_sleep_duration(),
            "avg_activity_time": self.get_avg_activity_time(),
            "avg_weight": self.get_avg_weight(),
            "avg_height": self.get_avg_height(),
            "avg_fat_percentage": self.get_avg_fat_percentage(),
            "avg_bmi": self.get_avg_bmi(),
            "avg_bmr": 1680,
            "avg_burned_calories_percent": 72,
            "total_burned_calories_percent": 65,
            "steps_change_percent": 12,
            "activity_time_change_percent": 18,
            "burned_calories_change_percent": 10,
            "consumed_calories_change_percent": -5,
            "water_change_percent": 7,
            "sleep_change_percent": -4,
            "day_streak": 14,
        }
