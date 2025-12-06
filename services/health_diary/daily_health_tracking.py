from services.body_metrics.body_metrics import BodyMetricsCalculator
from services.user.user_body_info import UserBodyInfo
from services.activities.activity_type import SpecificActivityType
from services.nutrition.meal import Meal
import time
from services.time_logic import time_in_period
from services.user.user_info import User
from services.user.user_body_goals import UserBodyDailyGoals


class HealthDaily:
    def __init__(self):
        self.day: str = time.strftime("%Y-%m-%d", time.localtime())
        self.burned_calories_for_day: float = 0.0
        self.consumed_calories_for_day: float = 0.0
        self.list_of_activities_for_day: list = []
        self.list_of_meals_for_day: list = []
        self.drunk_water: float = 0.0
        self.sleep_duration: float = 0.0

    def add_burned_calories(self, calories) -> None:
        self.burned_calories_for_day += calories

    def add_activity(self, activity_object: SpecificActivityType) -> None:
        self.list_of_activities_for_day.append(activity_object)
        self.burned_calories_for_day += activity_object.get_burned_calories()

    # add method add_burned_calories, add_consumed_calories to allow user enter burned calories (maybe)

    def add_drunk(self, amount_of_drunk_water) -> None:
        self.drunk_water += amount_of_drunk_water

    def add_sleep(self, amount_of_sleep) -> None:
        self.sleep_duration += amount_of_sleep

    def add_meals(self, meal: Meal) -> None:
        self.list_of_meals_for_day.append(meal)
        self.consumed_calories_for_day += meal.calories


class HealthDailyAnalyzer:
    """This class responsible for analyze daily health. This class analyze a health_diary object and
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
            total_time_spent += activity.get_total_time_spent_on_activities_in_minutes()
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

    def get_body_metrics_values(self):
        pass

    def get_sleep_duration(self) -> float:
        return self.health_daily.sleep_duration

    def calculate_body_mass_index(self):
        return self.body_metrics_calculator.calculate_body_mass_index_metrics()

    def calculate_basal_metabolic_rate(self):
        return self.body_metrics_calculator.calculate_basal_metabolic_rate()

    def calculate_lean_body_mass_index(self):
        return self.body_metrics_calculator.calculate_lean_body_mass()

    def calculate_fat_mass(self):
        return self.body_metrics_calculator.calculate_fat_mass()


class HealthAnalyzerInSomePeriod:
    """This class responsible for analyze a statistics on some period of time. This class analyze list of health_diary objects.
    Constructor accepts a list of health_diary objects and start_data, end_data. Start_data and end_data have next
    the str format YYYY-MM-DD
    """

    def __init__(self, list_of_health_diary: list, start_data: str, end_data: str):
        self.list_of_health_diary = list_of_health_diary
        self.start_data = start_data
        self.end_data = end_data

    def get_total_time_spent_on_activities_in_minutes(self) -> float:
        total_time_spent = 0.0
        for activity in self.list_of_health_diary:
            if time_in_period(
                self.start_data, self.end_data, activity.date_of_activity
            ):
                total_time_spent += activity.calculate_activity_duration_in_minutes()
        return total_time_spent

    def get_total_consumed_calories(self) -> float:
        total_consumed_calories = 0.0
        for day in self.list_of_health_diary:
            total_consumed_calories += day.consumed_calories_for_day
        return total_consumed_calories

    def get_total_burned_calories(self) -> float:
        total_burned_calories = 0.0
        for day in self.list_of_health_diary:
            total_burned_calories += day.burned_calories_for_day
        return total_burned_calories
