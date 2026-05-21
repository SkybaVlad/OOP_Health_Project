from core import User
from core.activity.activity_type import SpecificActivityType
from core.body_metrics_calculator import (
    calculate_body_mass_index_metrics,
    calculate_basal_metabolic_rate,
    calculate_lean_body_mass,
    calculate_fat_mass,
)
from core.daily_health import HealthDaily
from core.user.user_body_goals import UserBodyDailyGoals
from core.user.user_body_info import UserBodyInfo


class HealthDailyAnalyzer:
    """
    This class analyze a health_daily object and
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
        if self.user_body_daily_goals.consumed_calories_goal == 0.0:
            return (
                self.health_daily.consumed_calories_goal_on_day
                - self.health_daily.consumed_calories_for_day
            )
        return (
            self.user_body_daily_goals.get_consumed_calories_goal()
            - self.health_daily.consumed_calories_for_day
        )

    def get_remaining_of_burned_calories(self) -> float:
        if self.user_body_daily_goals.burned_calories_goal == 0.0:
            return (
                self.health_daily.burned_calories_goal_on_day
                - self.health_daily.burned_calories_for_day
            )
        return (
            self.user_body_daily_goals.get_burned_calories_goal()
            - self.health_daily.burned_calories_for_day
        )

    def get_remaining_water(self) -> float:
        if self.user_body_daily_goals.water_goal == 0.0:
            return self.health_daily.water_goal_on_day - self.health_daily.drunk_water
        return (
            self.user_body_daily_goals.get_water_goal() - self.health_daily.drunk_water
        )

    def get_remaining_steps(self) -> float:
        if self.user_body_daily_goals.step_goal == 0.0:
            return (
                self.health_daily.step_goal_on_day
                - self.health_daily.count_of_steps_for_day
            )
        return (
            self.user_body_daily_goals.step_goal
            - self.health_daily.count_of_steps_for_day
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

    def get_list_of_activities(self) -> list[SpecificActivityType]:
        return [
            activity_obj
            for activity_obj in self.health_daily.list_of_activities_for_day
        ]

    def calculate_body_mass_index(self) -> float | None:
        if (
            self.user_body_info.get_weight() == 0.0
            or self.user_body_info.get_height() == 0
        ):
            return None

        return calculate_body_mass_index_metrics(
            self.user_body_info.get_weight(), self.user_body_info.get_height()
        )

    def calculate_basal_metabolic_rate(self):
        if (
            self.user_body_info.get_weight() == 0.0
            or self.user_body_info.get_height() == 0
        ):
            return None
        return calculate_basal_metabolic_rate(
            self.user.get_sex(),
            self.user_body_info.get_weight(),
            self.user_body_info.get_height(),
            self.user.get_age(),
        )

    def calculate_lean_body_mass_index(self):
        if (
            self.user_body_info.get_weight() == 0.0
            or self.user_body_info.get_fat_percentage() == 0
        ):
            return None
        return calculate_lean_body_mass(
            self.user_body_info.get_weight(),
            self.user_body_info.get_fat_percentage(),
        )

    def calculate_fat_mass(self):
        lean_body_mass_value = self.calculate_lean_body_mass_index()
        if lean_body_mass_value is None or self.user_body_info.get_weight() == 0.0:
            return None
        return calculate_fat_mass(
            self.user_body_info.get_weight(), lean_body_mass_value
        )

    def get_list_of_meals(self):
        return [meal for meal in self.health_daily.list_of_meals_for_day]

    def get_list_of_medication(self):
        return [med_obj for med_obj in self.health_daily.list_of_taken_medication]

    def get_daily_result(self) -> dict:
        # need also activity , medication and meals to return

        return {
            "date": self.health_daily.date_of_day,
            "burned_calories": self.get_burned_calories(),
            "consumed_calories": self.get_consumed_calories(),
            "activity": self.get_list_of_activities(),
            "meal": self.get_list_of_meals(),
            "medication": self.get_list_of_medication(),
            "water": self.get_consumed_water(),
            "sleep_duration": self.get_sleep_duration(),
            "steps": self.get_count_of_steps_for_day(),
            "weight": self.health_daily.weight,
            "height": self.health_daily.height,
            "fat_percentage": self.health_daily.fat_percentage,
            "activity_time": self.get_total_time_spent_on_activities_in_minutes_current_day(),
            "name_of_day": self.health_daily.name_of_day,
            "body_mass_index": self.calculate_body_mass_index(),
            "basal_metabolic_rate": self.calculate_basal_metabolic_rate(),
            "lean_body_mass_index": self.calculate_lean_body_mass_index(),
            "fat_mass": self.calculate_fat_mass(),
            "water_goal": self.health_daily.water_goal_on_day,
            "step_goal": self.health_daily.step_goal_on_day,
            "burned_calories_goal": self.health_daily.burned_calories_goal_on_day,
            "consumed_calories_goal": self.health_daily.consumed_calories_goal_on_day,
            "sleep_duration_goal": self.health_daily.sleep_duration_goal_on_day,
            "activity_time_goal": self.health_daily.activity_time_goal_on_day,
        }
