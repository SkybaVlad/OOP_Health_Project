from services.activities.activity_type import SpecificActivityType
from services.nutrition.meal import Meal
from data.health_diary_container import HealthDiary
import time
from services.health_daily.daily_health import HealthDaily
from services.specification_for_filter import *


class DairyFacade:
    """This facade class provide a wide range of methods that works with diary of days"""

    def __init__(self):
        self.health_diary: HealthDiary = HealthDiary()
        self.health_daily: HealthDaily | None = None

    def add_activity(
        self, activity_object: SpecificActivityType, provided_time_value
    ) -> None:
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if provided_time_value != time_value:
            specific_day: HealthDaily = self.__find_daily_health_with_specific_data(
                provided_time_value
            )
            if specific_day is not None:
                specific_day.add_activity(activity_object)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.add_activity(activity_object)
        else:
            if provided_time_value == self.health_daily.date_of_day:
                self.health_daily.add_activity(activity_object)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.add_activity(activity_object)

    def __find_daily_health_with_specific_data(self, data: str) -> HealthDaily | None:
        return self.health_diary.find_day(data)

    def add_meal(self, meal: Meal, provided_time_value) -> None:
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if provided_time_value != time_value:
            specific_day: HealthDaily = self.__find_daily_health_with_specific_data(
                provided_time_value
            )
            if specific_day is not None:
                specific_day.add_meals(meal)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.add_meals(meal)
        else:
            if provided_time_value == self.health_daily.date_of_day:
                self.health_daily.add_meals(meal)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.add_meals(meal)

    def add_amount_of_drunk_water(
        self, amount_of_drunk_water: float, provided_time_value
    ) -> None:
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if provided_time_value != time_value:
            specific_day: HealthDaily = self.__find_daily_health_with_specific_data(
                provided_time_value
            )
            if specific_day is not None:
                specific_day.add_drunk(amount_of_drunk_water)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.add_drunk(amount_of_drunk_water)
        else:
            if provided_time_value == self.health_daily.date_of_day:
                self.health_daily.add_drunk(amount_of_drunk_water)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.add_drunk(amount_of_drunk_water)

    def add_amount_of_sleep(self, amount_of_sleep: float, provided_time_value) -> None:
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if provided_time_value != time_value:
            specific_day: HealthDaily = self.__find_daily_health_with_specific_data(
                provided_time_value
            )
            if specific_day is not None:
                specific_day.add_sleep(amount_of_sleep)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.add_sleep(amount_of_sleep)
        else:
            if provided_time_value == self.health_daily.date_of_day:
                self.health_daily.add_sleep(amount_of_sleep)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.add_sleep(amount_of_sleep)

    def add_count_steps(self, count_of_steps: float, provided_time_value) -> None:
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if provided_time_value != time_value:
            specific_day: HealthDaily = self.__find_daily_health_with_specific_data(
                provided_time_value
            )
            if specific_day is not None:
                specific_day.add_count_of_steps(count_of_steps)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.add_count_of_steps(count_of_steps)
        else:
            if provided_time_value == self.health_daily.date_of_day:
                self.health_daily.add_count_of_steps(count_of_steps)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.add_count_of_steps(count_of_steps)

    def set_weight(self, weight_value: float, provided_time_value) -> None:
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if provided_time_value != time_value:
            specific_day: HealthDaily = self.__find_daily_health_with_specific_data(
                provided_time_value
            )
            if specific_day is not None:
                specific_day.set_weight(weight_value)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.set_weight(weight_value)
        else:
            if provided_time_value == self.health_daily.date_of_day:
                self.health_daily.set_weight(weight_value)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.set_weight(weight_value)

    def set_height(self, height_value: float, provided_time_value) -> None:
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if provided_time_value != time_value:
            specific_day: HealthDaily = self.__find_daily_health_with_specific_data(
                provided_time_value
            )
            if specific_day is not None:
                specific_day.set_height(height_value)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.set_height(height_value)
        else:
            if provided_time_value == self.health_daily.date_of_day:
                self.health_daily.set_height(height_value)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.set_height(height_value)

    def set_fat_percentage(
        self, fat_percentage_value: float, provided_time_value
    ) -> None:
        time_value = time.strftime("%Y-%m-%d", time.localtime())
        if provided_time_value != time_value:
            specific_day: HealthDaily = self.__find_daily_health_with_specific_data(
                provided_time_value
            )
            if specific_day is not None:
                specific_day.set_fat_percentage(fat_percentage_value)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.set_fat_percentage(fat_percentage_value)
        else:
            if provided_time_value == self.health_daily.date_of_day:
                self.health_daily.set_fat_percentage(fat_percentage_value)
            else:
                self.__create_new_health_daily(provided_time_value)
                self.health_daily.set_fat_percentage(fat_percentage_value)

    def day_validator(self, time_value) -> bool:
        if time_value == self.health_daily.date_of_day:
            return True
        return False

    def __create_new_health_daily(self, date_of_day) -> None:
        self.health_daily = HealthDaily(date_of_day)
        self.health_diary.add_day(self.health_daily)

    def get_list_of_all_days(self):
        return self.health_diary.get_history_of_days()
