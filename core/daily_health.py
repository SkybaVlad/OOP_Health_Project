from core.activity.activity_type import SpecificActivityType
from core.nutrition.meal import Meal
from core.time_logic import calculate_duration_of_activity
from core.medication.medication_objects import Medication
import datetime


class HealthDaily:
    def __init__(self, date_of_day: str):
        """This class contain all characteristic about day.


        Goals value set as default value but user can define own goals"""
        self.date_of_day: str = date_of_day
        self.burned_calories_for_day: float = 0.0
        self.consumed_calories_for_day: float = 0.0
        self.list_of_activities_for_day: list[SpecificActivityType] = []
        self.list_of_meals_for_day: list = []
        self.list_of_taken_medication: list[Medication] = []
        self.drunk_water: float = 0.0
        self.sleep_duration: float = 0.0
        self.count_of_steps_for_day: float = 0.0
        self.weight: float = 0.0
        self.height: float = 0.0
        self.fat_percentage: float = 0.0
        self.total_time_spend_on_activities: float = 0.0
        self.name_of_day: str = self.generate_name_of_day()
        self.water_goal_on_day: float = 0.0
        self.burned_calories_goal_on_day: float = 0.0
        self.consumed_calories_goal_on_day: float = 0.0
        self.step_goal_on_day: float = 0.0

    def add_activity(self, activity_object: SpecificActivityType) -> None:
        self.list_of_activities_for_day.append(activity_object)
        self.burned_calories_for_day += activity_object.get_burned_calories()
        self.total_time_spend_on_activities += calculate_duration_of_activity(
            activity_object.get_start_time_of_specific_activity(),
            activity_object.get_end_time_of_specific_activity(),
        )

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

    def add_medication_that_took_today(self, medication_obj) -> None:
        self.list_of_taken_medication.append(medication_obj)

    def add_burned_calories(self, burned_calories: float) -> None:
        self.burned_calories_for_day += burned_calories

    def set_water_goal_on_day(self, water_goal_on_day: float) -> None:
        self.water_goal_on_day = water_goal_on_day

    def set_burned_calories_goal_on_day(
        self, burned_calories_goal_for_day: float
    ) -> None:
        self.burned_calories_goal_on_day = burned_calories_goal_for_day

    def set_consumed_calories_goal_on_day(
        self, consumed_calories_goal_for_day: float
    ) -> None:
        self.consumed_calories_goal_on_day = consumed_calories_goal_for_day

    def set_step_goal_on_day(self, step_goal_on_day: float) -> None:
        self.step_goal_on_day = step_goal_on_day

    def generate_name_of_day(self) -> str:
        lst = self.date_of_day.split("-")
        date = datetime.date(int(lst[0]), int(lst[1]), int(lst[2]))
        return date.strftime("%A")

    def __eq__(self, other) -> bool:
        return self.date_of_day == other.date_of_day

    def __hash__(self) -> int:
        return hash(self.date_of_day)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.date_of_day})"
