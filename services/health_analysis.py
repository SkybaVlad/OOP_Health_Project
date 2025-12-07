from services.activities.activity_type import ActivityCategory
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
