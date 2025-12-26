import datetime

from services.activities.activity_type import SpecificActivityType
from services.medication.medication import (
    MedicationReceipt,
    MedicationObjectReceiptCharacteristic,
)
from services.nutrition.meal import Meal
from data.health_diary_container import HealthDiary
import time
from services.specification_for_filter import *
from services.time_logic import time_validator_format_yyyy_mm_dd, time_in_period
from services.medication.medication import (
    Medication,
    MedicationReceipt,
    MedicationReceiptList,
)
from datetime import date


class DairyFacade:
    """This facade class provide a wide range of methods that works with diary of days and days objects"""

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, "initialize"):
            self.health_diary: HealthDiary | None = None
            self.current_day: HealthDaily | None = None
            self.list_of_receipts: MedicationReceiptList | None = None
            self.initialize = True

    def set_health_diary(self, health_diary: HealthDiary):
        self.health_diary = health_diary

    def set_health_daily(self, first_day: HealthDaily):
        self.current_day = first_day

    def set_list_of_receipts(self, list_of_receipts: MedicationReceiptList):
        self.list_of_receipts = list_of_receipts

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

    def get_list_of_all_days_in_history(self):
        return self.health_diary.get_history_of_days()

    def add_medication_receipt(self, receipt: MedicationReceipt):
        self.list_of_receipts.add_receipt(receipt)

    def get_list_of_all_receipts(self) -> list:
        return self.list_of_receipts.receipts

    def get_list_of_medications_that_need_to_take_today(self) -> list[Medication]:
        """This function filter all meds objects (Medication class)
        from list_of_receipts object if data of curr day enter in interval of take this medication
        For example [{med_obj : characteristic}] if curr date in interval of characteristic (start_date: end_date)
        and frequency (for example if frequency = list of days, we need to check the current day name) is fitting
        """
        today_date = str(date.today())
        date_obj = date.fromisoformat(today_date)
        number_of_day = date_obj.weekday()
        today_day_name = dict_for_days[number_of_day]
        lst_of_med_objs_that_need_to_take_today = []
        for receipt in self.list_of_receipts.get_list_of_receipt():
            for med_obj in receipt:
                if (
                    receipt[med_obj].frequency == "everyday"
                    and receipt[med_obj].interval == "always"
                    or time_in_period(
                        receipt[med_obj].start_time_of_interval,
                        receipt[med_obj].end_time_of_interval,
                        today_date,
                    )
                ):
                    lst_of_med_objs_that_need_to_take_today.append(med_obj)
                elif (
                    len(receipt[med_obj].list_of_days) != 0
                    and receipt[med_obj].interval == "always"
                    or time_in_period(
                        receipt[med_obj].start_time_of_interval,
                        receipt[med_obj].end_time_of_interval,
                        today_date,
                    )
                ):
                    if today_day_name in receipt[med_obj].list_of_days:
                        lst_of_med_objs_that_need_to_take_today.append(med_obj)
                elif receipt[med_obj].frequency == "arbitrary":
                    lst_of_med_objs_that_need_to_take_today.append(med_obj)
        return lst_of_med_objs_that_need_to_take_today

    def took_medicine_receipt(self, medication_receipt: MedicationReceipt):
        pass

    def delete_receipts_if_interval_of_taking_is_end(self):
        pass


dict_for_days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}


if __name__ == "__main__":
    pass
