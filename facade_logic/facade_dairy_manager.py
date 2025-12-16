from services.activities.activity_type import SpecificActivityType
from services.nutrition.meal import Meal
from data.health_diary_container import HealthDiary
import time
from services.specification_for_filter import *
from services.time_logic import time_validator_format_yyyy_mm_dd


class DairyFacade:
    """This facade class provide a wide range of methods that works with diary of days and days objects"""

    def __init__(self):
        self.health_diary: HealthDiary | None = None
        self.current_day: HealthDaily | None = None

    def set_health_diary(self, health_diary: HealthDiary):
        self.health_diary = health_diary

    def set_health_daily(self, first_day: HealthDaily):
        self.current_day = first_day

    def add_activity(
        self, activity_object: SpecificActivityType, provided_time_value
    ) -> None:
        time_validator_format_yyyy_mm_dd(provided_time_value)
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if not self.is_current_day(time_value):
            day = self.__create_new_health_daily(time_value)
            self.current_day = day
            self.health_diary.add_day(day)

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.add_activity(activity_object)
            else:
                created_day = self.__create_new_health_daily(provided_time_value)
                created_day.add_activity(activity_object)
                self.health_diary.add_day(created_day)
            return

        self.current_day.add_activity(activity_object)

    def __find_daily_health_with_specific_data(self, data: str) -> HealthDaily | None:
        return self.health_diary.find_day(data)

    def add_meal(self, meal: Meal, provided_time_value) -> None:
        time_validator_format_yyyy_mm_dd(provided_time_value)
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if not self.is_current_day(time_value):
            day = self.__create_new_health_daily(time_value)
            self.current_day = day
            self.health_diary.add_day(day)

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.add_meals(meal)
            else:
                created_day = self.__create_new_health_daily(provided_time_value)
                created_day.add_meals(meal)
                self.health_diary.add_day(created_day)
            return

        self.current_day.add_meals(meal)

    def add_amount_of_drunk_water(
        self, amount_of_drunk_water: float, provided_time_value
    ) -> None:
        time_validator_format_yyyy_mm_dd(provided_time_value)
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if not self.is_current_day(time_value):
            day = self.__create_new_health_daily(time_value)
            self.current_day = day
            self.health_diary.add_day(day)

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.add_drunk(amount_of_drunk_water)
            else:
                created_day = self.__create_new_health_daily(provided_time_value)
                created_day.add_drunk(amount_of_drunk_water)
                self.health_diary.add_day(created_day)
            return

        self.current_day.add_drunk(amount_of_drunk_water)

    def add_amount_of_sleep(self, amount_of_sleep: float, provided_time_value) -> None:
        time_validator_format_yyyy_mm_dd(provided_time_value)
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if not self.is_current_day(time_value):
            day = self.__create_new_health_daily(time_value)
            self.current_day = day
            self.health_diary.add_day(day)

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.add_sleep(amount_of_sleep)
            else:
                created_day = self.__create_new_health_daily(provided_time_value)
                created_day.add_sleep(amount_of_sleep)
                self.health_diary.add_day(created_day)
            return

        self.current_day.add_sleep(amount_of_sleep)

    def add_count_steps(self, count_of_steps: float, provided_time_value) -> None:
        time_validator_format_yyyy_mm_dd(provided_time_value)
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if not self.is_current_day(time_value):
            day = self.__create_new_health_daily(time_value)
            self.current_day = day
            self.health_diary.add_day(day)

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.add_count_of_steps(count_of_steps)
            else:
                created_day = self.__create_new_health_daily(provided_time_value)
                created_day.add_count_of_steps(count_of_steps)
                self.health_diary.add_day(created_day)
            return

        self.current_day.add_count_of_steps(count_of_steps)

    def set_weight(self, weight_value: float, provided_time_value) -> None:
        time_validator_format_yyyy_mm_dd(provided_time_value)
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if not self.is_current_day(time_value):
            day = self.__create_new_health_daily(time_value)
            self.current_day = day
            self.health_diary.add_day(day)

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.set_weight(weight_value)
            else:
                created_day = self.__create_new_health_daily(provided_time_value)
                created_day.set_weight(weight_value)
                self.health_diary.add_day(created_day)
            return

        self.current_day.set_weight(weight_value)

    def set_height(self, height_value: float, provided_time_value) -> None:
        time_validator_format_yyyy_mm_dd(provided_time_value)
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if not self.is_current_day(time_value):
            day = self.__create_new_health_daily(time_value)
            self.current_day = day
            self.health_diary.add_day(day)

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.set_height(height_value)
            else:
                created_day = self.__create_new_health_daily(provided_time_value)
                created_day.set_height(height_value)
                self.health_diary.add_day(created_day)
            return

        self.current_day.set_height(height_value)

    def set_fat_percentage(
        self, fat_percentage_value: float, provided_time_value
    ) -> None:
        time_validator_format_yyyy_mm_dd(provided_time_value)
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if not self.is_current_day(time_value):
            day = self.__create_new_health_daily(time_value)
            self.current_day = day
            self.health_diary.add_day(day)

        if provided_time_value != self.current_day.date_of_day:
            found_day = self.__find_daily_health_with_specific_data(provided_time_value)
            if found_day:
                found_day.set_fat_percentage(fat_percentage_value)
            else:
                created_day = self.__create_new_health_daily(provided_time_value)
                created_day.set_fat_percentage(fat_percentage_value)
                self.health_diary.add_day(created_day)
            return

        self.current_day.set_fat_percentage(fat_percentage_value)

    def is_current_day(self, time_value) -> bool:
        if time_value == self.current_day.date_of_day:
            return True
        return False

    def __create_new_health_daily(self, date_of_day) -> HealthDaily:
        day = HealthDaily(date_of_day)
        return day

    def get_list_of_all_days(self):
        return self.health_diary.get_history_of_days()
