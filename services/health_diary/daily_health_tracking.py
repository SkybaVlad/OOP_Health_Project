from services.body_metrics.body_metrics import StrategyBodyMetricsInterface
from services.activities.activity_type import SpecificActivityType
from services.nutrition.meal import Meal
import time


class HealthDaily:
    def __init__(self):
        self.day: str = time.strftime("%Y-%m-%d", time.localtime())
        self.burned_calories_for_day: float = 0.0
        self.consumed_calories_for_day: float = 0.0
        self.list_of_activities_for_day: list = []
        self.list_of_meals_for_day: list = []
        self.drank_water: float = 0.0
        self.sleep_duration: float = 0.0

    def add_burned_calories(self, calories) -> None:
        self.burned_calories_for_day += calories

    def add_activity(self, activity_object: SpecificActivityType) -> None:
        self.list_of_activities_for_day.append(activity_object)
        self.burned_calories_for_day += activity_object.get_burned_calories()

    # add method add burned calories to allow user enter burned calories (maybe)

    def add_meals(self, meal: Meal) -> None:
        self.list_of_meals_for_day.append(meal)
        self.consumed_calories_for_day += meal.calories


class HealthDailyAnalyzer:
    """This class responsible for analyze daily health. This class analyze a health_diary object and
    user_body_daily_goals and provide methods that return results of analysis"""
    def __init__(self, health_diary, user_body_daily_goals):
        self.health_diary = health_diary
        self.user_body_daily_goals = user_body_daily_goals

    def get_total_time_spent_on_activities_in_minutes(self) -> float:
        total_time_spent = 0.0
        for activity in self.health_diary.list_of_activities_for_day:
            total_time_spent += activity.get_total_time_spent_on_activities_in_minutes()
        return total_time_spent

    def get_remaining_of_consumed_calories(self) -> float:
        return self.user_body_daily_goals.get_consumed_calories_goal() - self.health_diary.consumed_calories_for_day

    def get_remaining_of_burned_calories(self) -> float:
        return self.user_body_daily_goals.get_burned_calories_goal() - self.health_diary.burned_calories_for_day

    def get_remaining_water(self) -> float:
        return self.user_body_daily_goals.get_water_goal() - self.health_diary.drank_water

    def get_consumed_calories(self) -> float:
        return self.health_diary.consumed_calories_for_day

    def get_burned_calories(self) -> float:
        return self.health_diary.burned_calories_for_day

    def get_consumed_water(self) -> float:
        return self.health_diary.drank_water

    def get_body_metrics_values(self):
        pass

    def get_sleep_duration(self) -> float:
        return self.health_diary.sleep_duration


class HealthMonthAnalyzer:
    """This class responsible for analyze a month statistics. This class analyze list of health_diary objects"""
    pass
