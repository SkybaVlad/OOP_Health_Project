from services.activities.activity_type import ActivityCategory
from services.body_metrics.body_metrics import BodyMetricsCalculator
from services.health_daily_track.daily_health_tracking import HealthDaily
from services.time_logic import time_in_period
from services.user.user_body_goals import UserBodyDailyGoals
from services.user.user_body_info import UserBodyInfo
from services.user.user_info import User
from data.health_diary import HealthDiary


class HealthDailyAnalyzer:
    """This class responsible for analyze daily health. This class analyze a health_daily_track object and
    user_body_daily_goals and provide methods that return results of analysis"""

    def __init__(
        self,
        health_daily: HealthDaily,
        user_body_daily_goals: UserBodyDailyGoals,
        user_body_info: UserBodyInfo,
        user_info: User,
    ):
        self.health_daily = health_daily
        self.user_body_daily_goals = user_body_daily_goals
        self.body_metrics_calculator = BodyMetricsCalculator(user_body_info, user_info)

    def get_total_time_spent_on_activities_in_minutes(self) -> float:
        total_time_spent = 0.0
        for activity in self.health_daily.list_of_activities_for_day:
            total_time_spent += activity.calculate_activity_duration_in_minutes()
        return total_time_spent

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
        return self.body_metrics_calculator.calculate_body_mass_index_metrics()

    def calculate_basal_metabolic_rate(self):
        return self.body_metrics_calculator.calculate_basal_metabolic_rate()

    def calculate_lean_body_mass_index(self):
        return self.body_metrics_calculator.calculate_lean_body_mass()

    def calculate_fat_mass(self):
        return self.body_metrics_calculator.calculate_fat_mass()


class HealthAnalyzerInSomePeriod:
    """This class responsible for analyze a statistics on some period of time. This class analyze list of health_daily_track objects.
    Constructor accepts a list of health_daily_track objects and start_data, end_data. Start_data and end_data have next
    the str format YYYY-MM-DD
    """

    def __init__(self, health_diary: HealthDiary, start_data: str, end_data: str):
        self.list_health_diary = health_diary.get_history_of_days()
        self.start_data = start_data
        self.end_data = end_data

    def get_total_time_spent_on_activities_in_minutes(self) -> float:
        total_time_spent = 0.0
        for day in self.list_health_diary:
            for activity in day.list_of_activities_for_day:
                total_time_spent += activity.calculate_activity_duration_in_minutes()
        return total_time_spent

    def get_total_consumed_calories(self) -> float:
        total_consumed_calories = 0.0
        for day in self.list_health_diary:
            total_consumed_calories += day.consumed_calories_for_day
        return total_consumed_calories

    def get_total_burned_calories(self) -> float:
        total_burned_calories = 0.0
        for day in self.list_health_diary:
            total_burned_calories += day.burned_calories_for_day
        return total_burned_calories

    def get_total_steps(self):
        total_steps = 0.0
        for day in self.list_health_diary:
            total_steps += day.count_of_steps_for_day
        return total_steps

    def get_total_time_spent_on_cardio_activities(self):
        total_time_spent = 0.0
        for day in self.list_health_diary:
            for activity in day.list_of_activities_for_day:
                if activity.activity_category == ActivityCategory.Cardio.value:
                    total_time_spent += (
                        activity.calculate_activity_duration_in_minutes()
                    )
        return total_time_spent

    def get_total_time_spent_on_strength_activities(self):
        total_time_spent = 0.0
        for day in self.list_health_diary:
            for activity in day.list_of_activities_for_day:
                if activity.activity_category == ActivityCategory.Strength.value:
                    total_time_spent += (
                        activity.calculate_activity_duration_in_minutes()
                    )
        return total_time_spent

    def get_total_time_spent_on_sport_activities(self):
        total_time_spent = 0.0
        for day in self.list_health_diary:
            for activity in day.list_of_activities_for_day:
                if activity.activity_category == ActivityCategory.Sport.value:
                    total_time_spent += (
                        activity.calculate_activity_duration_in_minutes()
                    )
        return total_time_spent

    def get_day_with_max_consumed_calories(self) -> HealthDaily | float:
        if len(self.list_health_diary) == 0:
            return 0.0
        day_with_max_consumed_calories = self.list_health_diary[0]
        for day in self.list_health_diary:
            if day.consumed_calories_for_day > day_with_max_consumed_calories:
                day_with_max_consumed_calories = day.consumed_calories_for_day
        return day_with_max_consumed_calories

    def get_day_with_max_burned_calories(self) -> HealthDaily | float:
        if len(self.list_health_diary) == 0:
            return 0.0
        day_with_max_burned_calories = self.list_health_diary[0]
        for day in self.list_health_diary:
            if day.burned_calories_for_day > day_with_max_burned_calories:
                day_with_max_burned_calories = day.burned_calories_for_day
        return day_with_max_burned_calories

    def get_day_with_max_steps(self) -> HealthDaily | float:
        if len(self.list_health_diary) == 0:
            return 0.0
        day_with_max_steps = self.list_health_diary[0]
        for day in self.list_health_diary:
            if day.count_of_steps_for_day > day_with_max_steps:
                day_with_max_steps = day.count_of_steps_for_day
        return day_with_max_steps

    def get_day_with_max_time_spent_on_activities(self) -> HealthDaily | float:
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

    def get_day_with_max_amount_of_drunk_water(self) -> HealthDaily | float:
        if len(self.list_health_diary) == 0:
            return 0.0
        day_with_max_amount_of_drunk_water = self.list_health_diary[0]
        for day in self.list_health_diary:
            if day.drunk_water > day_with_max_amount_of_drunk_water.drunk_water:
                day_with_max_amount_of_drunk_water = day
        return day_with_max_amount_of_drunk_water

    def get_day_with_max_hours_spent_on_sleep(self):
        if len(self.list_health_diary) == 0:
            return 0.0
        day_with_max_hours_of_sleep = self.list_health_diary[0]
        for day in self.list_health_diary:
            if day.sleep_duration > day_with_max_hours_of_sleep.sleep_duration:
                day_with_max_hours_of_sleep = day
        return day_with_max_hours_of_sleep
