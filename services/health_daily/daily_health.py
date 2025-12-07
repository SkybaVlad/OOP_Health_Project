from services.activities.activity_type import SpecificActivityType
from services.nutrition.meal import Meal
import time


class HealthDaily:
    def __init__(self, date_of_day):
        self.date_of_day: str = date_of_day
        self.burned_calories_for_day: float = 0.0
        self.consumed_calories_for_day: float = 0.0
        self.list_of_activities_for_day: list[SpecificActivityType] = []
        self.list_of_meals_for_day: list = []
        self.drunk_water: float = 0.0
        self.sleep_duration: float = 0.0
        self.count_of_steps_for_day: float = 0.0
        self.weight: float = 0.0
        self.height: float = 0.0
        self.fat_percentage: float = 0.0

    def add_activity(self, activity_object: SpecificActivityType) -> None:
        self.list_of_activities_for_day.append(activity_object)
        self.burned_calories_for_day += activity_object.get_burned_calories()

    def add_meals(self, meal: Meal) -> None:
        self.list_of_meals_for_day.append(meal)
        self.consumed_calories_for_day += meal.calories

    def add_drunk(self, amount_of_drunk_water) -> None:
        self.drunk_water += amount_of_drunk_water

    def add_sleep(self, amount_of_sleep) -> None:
        self.sleep_duration += amount_of_sleep

    def add_count_of_steps(self, count_of_steps: float) -> None:
        self.count_of_steps_for_day += count_of_steps

    def set_weight(self, weight_value) -> None:
        self.weight = weight_value

    def set_height(self, height_value) -> None:
        self.height = height_value

    def set_fat_percentage(self, percentage_value) -> None:
        self.fat_percentage = percentage_value
