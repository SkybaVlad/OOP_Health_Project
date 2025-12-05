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

    def add_burned_calories(self, calories):
        self.burned_calories_for_day += calories

    def add_consumed_calories(self, calories):
        self.consumed_calories_for_day += calories

    def add_activity(self, activity_object: SpecificActivityType):
        self.list_of_activities_for_day.append(activity_object)

    def add_meals(self, meal: Meal):
        self.list_of_meals_for_day.append(meal)


class HealthDailyAnalyzer:
    def __init__(self, health_diary, user_body_daily_goals):
        self.health_diary = health_diary
        self.user_body_daily_goals = user_body_daily_goals

    def get_total_time_spent_on_activities(self):
        pass

    def get_remaining_calories(self):
        # need a calories goal on the day to calculate a remaining calories
        pass

    def get_remaining_water(self):
        # need a water goal on the day to calculate a remaining calories
        pass

    def get_consumed_calories(self) -> float:
        return self.health_diary.consumed_calories_for_day

    def get_sleep_duration(self) -> float:
        return self.health_diary.sleep_duration

    def get_consumed_water(self) -> float:
        return self.health_diary.drank_water

    def get_body_metrics_values(self):
        pass


class HealthMonthAnalyzer:
    pass
