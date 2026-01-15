from core import User
from core.activity.activity_type import SpecificActivityType
from core.nutrition.meal import Meal
from core.health_diary_container import HealthDiary
from core.specification_for_filter import *
from core.medication.medication_objects import (
    Medication,
)
from datetime import date
from core.medication.medication_manager import MedicationManager
from core.user.user_body_goals import UserBodyDailyGoals


class DairyFacade:
    """This facade class provide a wide range of methods
    that works with diary of days and days objects"""

    def __init__(self):
        self.health_diary: HealthDiary | None = None
        self.current_day: HealthDaily | None = None
        self.medication_manager: MedicationManager | None = None
        self.user_body_daily_goals: UserBodyDailyGoals | None = None
        self.user: User | None = None

    def initialize(
        self,
        health_diary: HealthDiary,
        current_day: HealthDaily,
        medication_manager: MedicationManager,
        user_body_daily_goals: UserBodyDailyGoals,
        user: User,
    ):
        self.health_diary = health_diary
        self.current_day = current_day
        self.medication_manager = medication_manager
        self.health_diary.add_day(current_day)
        self.user_body_daily_goals = user_body_daily_goals
        self.user = user

    def set_health_diary(self, health_diary: HealthDiary):
        self.health_diary = health_diary

    def set_health_daily(self, first_day: HealthDaily):
        self.current_day = first_day

    def set_user_body_daily_goals(self, user_body_daily_goals: UserBodyDailyGoals):
        self.user_body_daily_goals = user_body_daily_goals

    def add_activity(
        self, activity_object: SpecificActivityType, provided_time_value: str
    ) -> None:

        # if actual date of day is changed -> need to update current_day attribute
        if not self.is_current_day(str(date.today())):
            self.update_curr_day()

        # if provided_time from user not equal current date of day -> need find
        # day with this date or create day object and add to list
        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            # if day with this date exist in list of days objects
            if found_day:
                found_day.add_activity(activity_object)
            else:
                created_day = self.create_new_health_daily(provided_time_value)
                created_day.add_activity(activity_object)
                self.health_diary.add_day(created_day)
            return None

        # if provided_time_value == today date
        self.current_day.add_activity(activity_object)

    def update_curr_day(self):
        day = self.create_new_health_daily(str(date.today()))
        self.load_goals_on_day(day)
        self.current_day = day
        self.health_diary.add_day(self.current_day)

    def __find_daily_health_with_specific_data(self, data: str) -> HealthDaily | None:
        return self.health_diary.find_day(data)

    def add_meal(self, meal: Meal, provided_time_value: str) -> None:
        if not self.is_current_day(str(date.today())):
            self.update_curr_day()

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.add_meals(meal)
            else:
                created_day = self.create_new_health_daily(provided_time_value)
                created_day.add_meals(meal)
                self.health_diary.add_day(created_day)
            return

        self.current_day.add_meals(meal)

    def add_amount_of_drunk_water(
        self, amount_of_drunk_water: float, provided_time_value: str
    ) -> None:
        if not self.is_current_day(str(date.today())):
            self.update_curr_day()

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.add_drunk(amount_of_drunk_water)
            else:
                created_day = self.create_new_health_daily(provided_time_value)
                created_day.add_drunk(amount_of_drunk_water)
                self.health_diary.add_day(created_day)
            return

        self.current_day.add_drunk(amount_of_drunk_water)

    def add_amount_of_sleep(
        self, amount_of_sleep: float, provided_time_value: str
    ) -> None:
        if not self.is_current_day(str(date.today())):
            self.update_curr_day()

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.add_sleep(amount_of_sleep)
            else:
                created_day = self.create_new_health_daily(provided_time_value)
                created_day.add_sleep(amount_of_sleep)
                self.health_diary.add_day(created_day)
            return

        self.current_day.add_sleep(amount_of_sleep)

    def add_count_steps(self, count_of_steps: int, provided_time_value: str) -> None:
        if not self.is_current_day(str(date.today())):
            self.update_curr_day()

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.add_count_of_steps(count_of_steps)
            else:
                created_day = self.create_new_health_daily(provided_time_value)
                created_day.add_count_of_steps(count_of_steps)
                self.health_diary.add_day(created_day)
            return

        self.current_day.add_count_of_steps(count_of_steps)

    def set_weight(self, weight_value: float, provided_time_value: str) -> None:
        if not self.is_current_day(str(date.today())):
            self.update_curr_day()

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.set_weight(weight_value)
            else:
                created_day = self.create_new_health_daily(provided_time_value)
                created_day.set_weight(weight_value)
                self.health_diary.add_day(created_day)
            return

        self.current_day.set_weight(weight_value)

    def set_height(self, height_value: float, provided_time_value: str) -> None:
        if not self.is_current_day(str(date.today())):
            self.update_curr_day()

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.set_height(height_value)
            else:
                created_day = self.create_new_health_daily(provided_time_value)
                created_day.set_height(height_value)
                self.health_diary.add_day(created_day)
            return

        self.current_day.set_height(height_value)

    def set_fat_percentage(
        self, fat_percentage_value: float, provided_time_value: str
    ) -> None:
        if not self.is_current_day(str(date.today())):
            self.update_curr_day()

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.set_fat_percentage(fat_percentage_value)
            else:
                created_day = self.create_new_health_daily(provided_time_value)
                created_day.set_fat_percentage(fat_percentage_value)
                self.health_diary.add_day(created_day)
            return

        self.current_day.set_fat_percentage(fat_percentage_value)

    def add_burned_calories(
        self, burned_calories: float, provided_time_value: str
    ) -> None:
        if not self.is_current_day(str(date.today())):
            self.update_curr_day()

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.add_burned_calories(burned_calories)
            else:
                created_day = self.create_new_health_daily(provided_time_value)
                created_day.add_burned_calories(burned_calories)
                self.health_diary.add_day(created_day)
            return

        self.current_day.add_burned_calories(burned_calories)

    def is_current_day(self, time_value: str) -> bool:
        if time_value == self.current_day.date_of_day:
            return True
        return False

    def create_new_health_daily(self, date_of_day: str) -> HealthDaily:
        day = HealthDaily(date_of_day)
        return day

    def get_list_of_all_days_in_history(self) -> list[HealthDaily]:
        return self.health_diary.get_history_of_days()

    def add_took_medication_object(self, medication_object: Medication):
        self.current_day.add_medication_that_took_today(medication_object)

    def add_took_medication_object_with_no_today_date(
        self, medication_obj: Medication, date_of_taken: str
    ):
        day = self.__find_daily_health_with_specific_data(date_of_taken)
        if day is None:
            created_day = self.create_new_health_daily(date_of_taken)
            self.health_diary.add_day(created_day)
            created_day.list_of_taken_medication.append(medication_obj)
        else:
            day.list_of_taken_medication.append(medication_obj)

    def load_goals_on_day(self, day: HealthDaily):
        if self.user_body_daily_goals.step_goal == 0:
            if self.user.get_age() >= 65:
                day.set_step_goal_on_day(5500)
            elif 18 <= self.user.get_age() < 65:
                day.set_step_goal_on_day(7000)
            elif 10 <= self.user.get_age() < 18:
                day.set_step_goal_on_day(9000)
        else:
            day.set_step_goal_on_day(self.user_body_daily_goals.step_goal)

        if self.user_body_daily_goals.water_goal == 0:
            if self.user.get_age() >= 65:
                day.set_water_goal_on_day(1.8)
            elif 18 <= self.user.get_age() < 65:
                day.set_water_goal_on_day(2.0)
            elif 10 <= self.user.get_age() < 18:
                day.set_water_goal_on_day(1.8)
        else:
            day.set_water_goal_on_day(self.user_body_daily_goals.water_goal)

        if self.user_body_daily_goals.burned_calories_goal == 0:
            if self.user.get_age() >= 65:
                day.set_burned_calories_goal_on_day(300.0)
            elif 18 <= self.user.get_age() < 65:
                day.set_burned_calories_goal_on_day(400.0)
            elif 10 <= self.user.get_age() < 18:
                day.set_burned_calories_goal_on_day(350.0)
        else:
            day.set_burned_calories_goal_on_day(
                self.user_body_daily_goals.burned_calories_goal
            )
        if self.user_body_daily_goals.consumed_calories_goal == 0:
            if self.user.get_age() >= 65:
                day.set_consumed_calories_goal_on_day(1800.0)
            elif 18 <= self.user.get_age() < 65:
                day.set_consumed_calories_goal_on_day(2000.0)
            elif 10 <= self.user.get_age() < 18:
                day.set_consumed_calories_goal_on_day(2000.0)
        else:
            day.set_consumed_calories_goal_on_day(
                self.user_body_daily_goals.consumed_calories_goal
            )


if __name__ == "__main__":
    pass
