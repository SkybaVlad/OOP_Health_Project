from services.activities.activity_type import SpecificActivityType
from services.nutrition.meal import Meal
from data.health_diary import HealthDiary
import time
from services.health_daily_track.daily_health_tracking import HealthDaily


class DairyFacade:
    def __init__(self):
        self.health_diary = HealthDiary()
        self.health_daily: None | HealthDaily = None

    def add_activity(
        self,
        activity_object: SpecificActivityType,
        provided_time_value=None,
        time_value=time.strftime("%Y-%m-%d", time.localtime()),
    ) -> None:
        if provided_time_value:
            specific_day: HealthDaily = self.__find_daily_health_with_specific_data(
                provided_time_value
            )
            if specific_day:
                specific_day.add_activity(activity_object)
        if self.day_validator(time_value) and provided_time_value is None:
            self.health_daily.add_activity(activity_object)
        if not self.day_validator(time_value):
            self.__create_new_health_daily()
            self.health_daily.add_activity(activity_object)

    def __find_daily_health_with_specific_data(self, data):
        for daily_health_object in self.health_diary.get_history_of_days():
            if daily_health_object.day == data.day:
                return daily_health_object
        return None

    def add_meal(
        self,
        meal: Meal,
        provided_time_value=None,
        time_value=time.strftime("%Y-%m-%d", time.localtime()),
    ) -> None:
        if provided_time_value:
            specific_day: HealthDaily = self.__find_daily_health_with_specific_data(
                provided_time_value
            )
            if specific_day:
                specific_day.add_meals(meal)
        if self.day_validator(time_value) and provided_time_value is None:
            self.health_daily.add_meals(meal)
        if not self.day_validator(time_value):
            self.__create_new_health_daily()
            self.health_daily.add_meals(meal)

    def add_daily_amount_of_drunk_water(
        self,
        amount_of_drunk_water: float,
        provided_time_value=None,
        time_value=time.strftime("%Y-%m-%d", time.localtime()),
    ) -> None:
        if provided_time_value:
            specific_day: HealthDaily = self.__find_daily_health_with_specific_data(
                provided_time_value
            )
            if specific_day:
                specific_day.add_drunk(amount_of_drunk_water)
        if self.day_validator(time_value) and provided_time_value is None:
            self.health_daily.add_drunk(amount_of_drunk_water)
        if not self.day_validator(time_value):
            self.__create_new_health_daily()
            self.health_daily.add_drunk(amount_of_drunk_water)

    def add_daily_amount_of_sleep(
        self,
        amount_of_sleep: float,
        provided_time_value=None,
        time_value=time.strftime("%Y-%m-%d", time.localtime()),
    ) -> None:
        if provided_time_value:
            specific_day: HealthDaily = self.__find_daily_health_with_specific_data(
                provided_time_value
            )
            if specific_day:
                specific_day.add_sleep(amount_of_sleep)
        if self.day_validator(time_value) and provided_time_value is None:
            self.health_daily.add_sleep(amount_of_sleep)
        if not self.day_validator(time_value):
            self.__create_new_health_daily()
            self.health_daily.add_sleep(amount_of_sleep)

    def add_body_metrics(self, metrics_type, value, data) -> None:
        self.body_metrics_container.add_body_metrics(metrics_type, value, data)

    def day_validator(self, time_value) -> bool:
        if time_value == self.health_daily.day:
            return True
        return False

    def __create_new_health_daily(self) -> None:
        self.health_daily = HealthDaily()
        self.health_diary.add_day(self.health_daily)
