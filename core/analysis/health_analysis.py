from abc import ABC, abstractmethod
from datetime import date
from typing import Any

from core.health_diary_container import HealthDiary
from core.body_metrics_calculator import (
    calculate_body_mass_index_metrics,
    calculate_lean_body_mass,
    calculate_fat_mass,
    calculate_basal_metabolic_rate,
)
from core.daily_health import HealthDaily
from core.user.user_body_goals import UserBodyDailyGoals, DefaultUserBodyGoals
from core.user.user_body_info import UserBodyInfo
from core.user.user_info import User
from core.medication.medication_objects import (
    MedicationReceiptList,
    Medication,
    MedicationObjectReceiptCharacteristic,
    Interval,
    Frequency,
)
from core.medication.medication_objects import MedicationReceipt
from core.validation_user_input.time_validator import (
    time_in_period,
)  # move this function
from core.activity.activity_type import SpecificActivityType


def get_list_of_days_is_some_period_and_not_empty_on_actvities(
    start_time: str, end_time: str, list_of_days: list[HealthDaily]
) -> list[HealthDaily]:
    lst_of_days = []
    for day in list_of_days:
        if (
            time_in_period(start_time, end_time, day.date_of_day)
            and len(day.list_of_activities_for_day) != 0
        ):
            lst_of_days.append(day)
    return lst_of_days


class HealthDailyAnalyzer:
    """

    This class analyze a health_daily object and
    user_body_daily_goals and provide methods that return results of analysis"""

    def __init__(self):
        self.health_daily: HealthDaily | None = None
        self.user_body_daily_goals: UserBodyDailyGoals | None = None
        self.user_body_info: UserBodyInfo | None = None
        self.user: User | None = None

    def set_day_that_need_to_analyze(self, health_daily: HealthDaily):
        self.health_daily = health_daily

    def set_user_body_daily_goals(self, user_body_daily_goals: UserBodyDailyGoals):
        self.user_body_daily_goals = user_body_daily_goals

    def set_user_body_info(self, user_body_info: UserBodyInfo):
        self.user_body_info = user_body_info

    def set_user_info(self, user_info: User):
        self.user = user_info

    def get_total_time_spent_on_activities_in_minutes_current_day(self) -> float:
        return self.health_daily.total_time_spend_on_activities

    def get_remaining_of_consumed_calories(self) -> float:
        if self.user_body_daily_goals.consumed_calories_goal == 0.0:
            return (
                DefaultUserBodyGoals.consumed_calories
                - self.health_daily.consumed_calories_for_day
            )
        return (
            self.user_body_daily_goals.get_consumed_calories_goal()
            - self.health_daily.consumed_calories_for_day
        )

    def get_remaining_of_burned_calories(self) -> float:
        if self.user_body_daily_goals.burned_calories_goal == 0.0:
            return (
                DefaultUserBodyGoals.burned_calories
                - self.health_daily.burned_calories_for_day
            )
        return (
            self.user_body_daily_goals.get_burned_calories_goal()
            - self.health_daily.burned_calories_for_day
        )

    def get_remaining_water(self) -> float:
        if self.user_body_daily_goals.water_goal == 0.0:
            return DefaultUserBodyGoals.water - self.health_daily.drunk_water
        return (
            self.user_body_daily_goals.get_water_goal() - self.health_daily.drunk_water
        )

    def get_remaining_steps(self) -> float:
        if self.user_body_daily_goals.step_goal == 0.0:
            return (
                DefaultUserBodyGoals.count_of_steps
                - self.health_daily.count_of_steps_for_day
            )
        return (
            self.user_body_daily_goals.step_goal
            - self.health_daily.count_of_steps_for_day
        )

    def get_consumed_calories(self) -> float:
        return self.health_daily.consumed_calories_for_day

    def get_burned_calories(self) -> float:
        return self.health_daily.burned_calories_for_day

    def get_consumed_water(self) -> float:
        return self.health_daily.drunk_water

    def get_sleep_duration(self) -> float:
        return self.health_daily.sleep_duration

    def get_count_of_steps_for_day(self) -> float:
        return self.health_daily.count_of_steps_for_day

    def get_list_of_activities(self) -> list[SpecificActivityType]:
        return [
            activity_obj
            for activity_obj in self.health_daily.list_of_activities_for_day
        ]

    def calculate_body_mass_index(self) -> float | None:
        if (
            self.user_body_info.get_weight() == 0.0
            or self.user_body_info.get_height() == 0
        ):
            return None

        return calculate_body_mass_index_metrics(
            self.user_body_info.get_weight(), self.user_body_info.get_height()
        )

    def calculate_basal_metabolic_rate(self):
        if (
            self.user_body_info.get_weight() == 0.0
            or self.user_body_info.get_height() == 0
        ):
            return None
        return calculate_basal_metabolic_rate(
            self.user.get_sex(),
            self.user_body_info.get_weight(),
            self.user_body_info.get_height(),
            self.user.get_age(),
        )

    def calculate_lean_body_mass_index(self):
        if (
            self.user_body_info.get_weight() == 0.0
            or self.user_body_info.get_fat_percentage() == 0
        ):
            return None
        return calculate_lean_body_mass(
            self.user_body_info.get_weight(),
            self.user_body_info.get_fat_percentage(),
        )

    def calculate_fat_mass(self):
        lean_body_mass_value = self.calculate_lean_body_mass_index()
        if lean_body_mass_value is None or self.user_body_info.get_weight() == 0.0:
            return None
        return calculate_fat_mass(
            self.user_body_info.get_weight(), lean_body_mass_value
        )

    def get_list_of_meals(self):
        return [meal for meal in self.health_daily.list_of_meals_for_day]

    def get_list_of_medication(self):
        return [med_obj for med_obj in self.health_daily.list_of_taken_medication]

    def get_daily_result(self) -> dict:
        # need also activity , medication and meals to return

        return {
            "date": self.health_daily.date_of_day,
            "burned_calories": self.get_burned_calories(),
            "consumed_calories": self.get_consumed_calories(),
            "activity": self.get_list_of_activities(),
            "meal": self.get_list_of_meals(),
            "medication": self.get_list_of_medication(),
            "water": self.get_consumed_water(),
            "sleep_duration": self.get_sleep_duration(),
            "steps": self.get_count_of_steps_for_day(),
            "weight": self.health_daily.weight,
            "height": self.health_daily.height,
            "fat_percentage": self.health_daily.fat_percentage,
            "activity_time": self.get_total_time_spent_on_activities_in_minutes_current_day(),
            "name_of_day": self.health_daily.name_of_day,
            "body_mass_index": self.calculate_body_mass_index(),
            "basal_metabolic_rate": self.calculate_basal_metabolic_rate(),
            "lean_body_mass_index": self.calculate_lean_body_mass_index(),
            "fat_mass": self.calculate_fat_mass(),
        }


class HealthInSomePeriodAnalyzer:
    """This class responsible for analyze your metrics in some period that you define.
    Under hood this class iterate through a list of HealthDaily objects and analyze each object.
    This class provide a wide range of methods.
    """

    def __init__(self):
        self.list_health_diary: list[HealthDaily] | None = None
        self.start_data: str | None = None
        self.end_data: str | None = None

    def set_list_of_days(self, list_of_health_diary: list[HealthDaily]):
        self.list_health_diary = list_of_health_diary

    def set_period_of_time(self, start_time_of_period, end_time_of_period):
        self.start_data = start_time_of_period
        self.end_data = end_time_of_period

    def get_total_time_spent_on_activities_in_minutes_for_all_time(self) -> int:
        total_time_spent = 0
        for day in self.list_health_diary:
            for activity in day.list_of_activities_for_day:
                total_time_spent += activity.calculate_activity_duration_in_minutes()
        return total_time_spent

    def get_total_consumed_calories_for_all_time(self) -> float:
        total_consumed_calories = 0.0
        for day in self.list_health_diary:
            total_consumed_calories += day.consumed_calories_for_day
        return total_consumed_calories

    def get_total_burned_calories_for_all_time(self) -> float:
        total_burned_calories = 0.0
        for day in self.list_health_diary:
            total_burned_calories += day.burned_calories_for_day
        return total_burned_calories

    def get_total_steps_for_all_time(self):
        total_steps = 0.0
        for day in self.list_health_diary:
            total_steps += day.count_of_steps_for_day
        return total_steps

    def get_total_time_spent_on_specific_category_of_activities_for_all_time(
        self, activity_category
    ):
        total_time_spent = 0.0
        for day in self.list_health_diary:
            for activity in day.list_of_activities_for_day:
                if activity.get_activity_category() == activity_category:
                    total_time_spent += (
                        activity.calculate_activity_duration_in_minutes()
                    )
        return total_time_spent

    def get_day_with_max_consumed_calories_for_all_time(self) -> HealthDaily | float:
        day_with_max_consumed_calories = self.list_health_diary[0]
        for day in self.list_health_diary:
            if day.consumed_calories_for_day > day_with_max_consumed_calories:
                day_with_max_consumed_calories = day.consumed_calories_for_day
        return day_with_max_consumed_calories

    def get_day_with_max_burned_calories_for_all_time(self) -> HealthDaily | float:
        day_with_max_burned_calories = self.list_health_diary[0]
        for day in self.list_health_diary:
            if day.burned_calories_for_day > day_with_max_burned_calories:
                day_with_max_burned_calories = day.burned_calories_for_day
        return day_with_max_burned_calories

    def get_day_with_max_steps_for_all_time(self) -> HealthDaily | float:
        day_with_max_steps = self.list_health_diary[0]
        for day in self.list_health_diary:
            if day.count_of_steps_for_day > day_with_max_steps:
                day_with_max_steps = day.count_of_steps_for_day
        return day_with_max_steps

    def get_day_with_max_time_spent_on_activities_for_all_time(
        self,
    ) -> HealthDaily | float:

        day_with_max_time_spent_on_activities = self.list_health_diary[0]
        max_total_time_spent_on_activities = (
            day_with_max_time_spent_on_activities.total_time_spend_on_activities
        )

        for day in self.list_health_diary:
            if day.total_time_spent_on_activities > max_total_time_spent_on_activities:
                max_total_time_spent_on_activities = day.total_time_spent_on_activities
                day_with_max_time_spent_on_activities = day
        return day_with_max_time_spent_on_activities

    def get_day_with_max_amount_of_drunk_water_for_all_time(
        self,
    ) -> HealthDaily | float:
        day_with_max_amount_of_drunk_water = self.list_health_diary[0]
        for day in self.list_health_diary:
            if day.drunk_water > day_with_max_amount_of_drunk_water.drunk_water:
                day_with_max_amount_of_drunk_water = day
        return day_with_max_amount_of_drunk_water

    def get_day_with_max_hours_spent_on_sleep_for_all_time(self):
        day_with_max_hours_of_sleep = self.list_health_diary[0]
        for day in self.list_health_diary:
            if day.sleep_duration > day_with_max_hours_of_sleep.sleep_duration:
                day_with_max_hours_of_sleep = day
        return day_with_max_hours_of_sleep

    def get_result_of_analyze_some_period(self) -> dict[str, Any]:
        return {
            "start_date": self.start_data,
            "end_date": self.end_data,
            "total_activity_time": self.get_total_time_spent_on_activities_in_minutes_for_all_time(),
            "total_consumed_calories": self.get_total_consumed_calories_for_all_time(),
            "total_burned_calories": self.get_total_burned_calories_for_all_time(),
            "total_steps": self.get_total_steps_for_all_time(),
        }


class MedicationAnalyzer:
    """This class intended for analyze receipts amd medications object. Also this class implement methods
    that manages a list of receipts. For example if concrete receipt is end, we need delete this receipt from
    list of receipts"""

    def __init__(
        self, health_diary: HealthDiary, list_of_receipts: MedicationReceiptList
    ):
        self.health_diary = health_diary
        self.list_of_receipts: MedicationReceiptList | None = list_of_receipts

    def concrete_med_obj_in_receipt_is_completed(
        self, med_obj: Medication, characteristic: MedicationObjectReceiptCharacteristic
    ) -> bool:
        """This method check if concrete med_obj is completed inside a dict {med_obj : characteristic, ... , med_obj : characteristic
        if med_obj is completed -> delete this pair from receipt}"""
        if characteristic.interval == Interval.Forever.value:
            return False
        if characteristic.frequency == Frequency.Every_day.value:
            for day in self.health_diary.get_history_of_days():
                if time_in_period(
                    characteristic.start_time_of_interval,
                    characteristic.end_time_of_interval,
                    day.date_of_day,
                ):
                    if med_obj not in day.list_of_taken_medication:
                        return False
        elif characteristic.frequency == Frequency.SpecificDays.value:
            for day in self.health_diary.get_history_of_days():
                if day.name_of_day in characteristic.list_of_days:
                    if time_in_period(
                        characteristic.start_time_of_interval,
                        characteristic.end_time_of_interval,
                        day.date_of_day,
                    ):
                        if med_obj not in day.list_of_taken_medication:
                            return False
        return True

    def receipt_is_completed(self, receipt_obj: MedicationReceipt) -> bool:
        """This method checks if receipt (MedicationReceipt object) is completed. Is completed
        means that interval of all subreceipts is end and all medication inside subreceipts is taken in one time. Subreceipt means one pair
        (key (Medication): value (MedicationObjectReceiptCharacteristic)) inside receipt obj in dict_of_medications_in_receipt attribute.
        Subreceipts that has MedicationObjectReceiptCharacteristic object with interval = "Forever" never will end.
        """
        for med_obj in receipt_obj.dict_of_medications_in_receipt.keys():
            characteristic = receipt_obj.dict_of_medications_in_receipt[med_obj]
            if characteristic.interval == Interval.Forever.value:
                return False
        for med_obj in receipt_obj.dict_of_medications_in_receipt.keys():
            characteristic = receipt_obj.dict_of_medications_in_receipt[med_obj]
            if not characteristic.interval_is_end():
                return False
            if characteristic.frequency == Frequency.Every_day.value:
                for day in self.health_diary.get_history_of_days():
                    if time_in_period(
                        characteristic.start_time_of_interval,
                        characteristic.end_time_of_interval,
                        day.date_of_day,
                    ):
                        if med_obj not in day.list_of_taken_medication:
                            return False
            elif characteristic.frequency == Frequency.SpecificDays.value:
                for day in self.health_diary.get_history_of_days():
                    if day.name_of_day not in characteristic.list_of_days:
                        if time_in_period(
                            characteristic.start_time_of_interval,
                            characteristic.end_time_of_interval,
                            day.date_of_day,
                        ):
                            if med_obj not in day.list_of_taken_medication:
                                return False
        return True

    def get_list_of_medications_that_need_to_take_today(self) -> list[Medication]:
        """This method filter all meds objects (Medication class)
        from list_of_receipts object if data of curr day enter in interval of take this medication
        For example [{med_obj : characteristic}] if curr date in interval of characteristic (start_date: end_date)
        and frequency (for example if frequency = list of days, we need to check the current day name) is fitting
        """
        lst_of_med_objs_that_need_to_take_today = []
        for (
            medication_receipt_obj
        ) in self.list_of_receipts.get_list_of_all_available_receipts():
            for med_obj in medication_receipt_obj.dict_of_medications_in_receipt.keys():
                if not medication_receipt_obj.dict_of_medications_in_receipt[
                    med_obj
                ].interval_is_end():
                    if (
                        medication_receipt_obj.dict_of_medications_in_receipt[
                            med_obj
                        ].frequency
                        == Frequency.Every_day.value
                    ):
                        lst_of_med_objs_that_need_to_take_today.append(med_obj)
                    else:
                        if medication_receipt_obj.dict_of_medications_in_receipt[
                            med_obj
                        ].day_in_list_of_days(date.today().strftime("%A")):
                            lst_of_med_objs_that_need_to_take_today.append(med_obj)
        return lst_of_med_objs_that_need_to_take_today

    def get_list_of_all_medication_that_user_not_take(
        self,
    ) -> list[tuple[Medication, str]]:
        """This method return list of tuples, where each tuple is contains with medication
        object and data when this medication object user do not take."""
        lst: list[tuple[Medication, str]] = []
        for receipt in self.list_of_receipts.receipts:
            for med_obj in receipt.dict_of_medications_in_receipt:
                for day in self.health_diary.get_history_of_days():
                    date_of_day = date.fromisoformat(day.date_of_day)
                    name_of_day = date_of_day.strftime("%A")
                    if (
                        receipt.dict_of_medications_in_receipt[med_obj].frequency
                        == Frequency.Every_day.value
                        and med_obj not in day.list_of_taken_medication
                    ):
                        lst.append((med_obj, day.date_of_day))
                    elif (
                        receipt.dict_of_medications_in_receipt[med_obj].frequency
                        == Frequency.SpecificDays.value
                    ):
                        if (
                            name_of_day
                            in receipt.dict_of_medications_in_receipt[
                                med_obj
                            ].list_of_days
                            and med_obj not in day.list_of_taken_medication
                        ):
                            lst.append((med_obj, day.date_of_day))
        return lst


class ActivityAnalyzer:
    """This class responsible for analyze general metrics about activity
    in some period of time."""

    def __init__(self, start_time: str, end_time: str, list_of_days: list[HealthDaily]):
        self.start_time = start_time
        self.end_time = end_time
        self.list_of_days = get_list_of_days_is_some_period_and_not_empty_on_actvities(
            start_time, end_time, list_of_days
        )

    def set_period_of_time(self, start_period: str, end_period: str):
        self.start_time = start_period
        self.end_time = end_period

    def get_total_spend_on_activity(self) -> float:
        total_time = 0.0
        for day in self.list_of_days:
            for activity in day.list_of_activities_for_day:
                total_time += activity.calculate_activity_duration_in_minutes()
        return total_time

    def get_total_burned_calories_with_activity(self):
        total_burned_calories = 0.0
        for day in self.list_of_days:
            for activity in day.list_of_activities_for_day:
                total_burned_calories += activity.burned_calories
        return total_burned_calories


class ActivityTypeAnalyzer(ActivityAnalyzer):
    def __init__(self, start_time: str, end_time: str, list_of_days: list[HealthDaily]):
        super().__init__(
            start_time, end_time, list_of_days
        )  # super(ActivityTypeAnalyzer, self).init(...)

    def get_list_of_activities_names_that_exist_in_period(self) -> list[str]:
        lst_of_activities_names = []
        for day in self.list_of_days:
            for activity in day.list_of_activities_for_day:
                lst_of_activities_names.append(activity.activity_name)
        return lst_of_activities_names

    def get_list_of_activities_categories_that_exist_in_period(self) -> list[str]:
        lst_of_activities_categories = []
        for day in self.list_of_days:
            for activity in day.list_of_activities_for_day:
                lst_of_activities_categories.append(activity.activity_name)
        return lst_of_activities_categories

    def get_time_spend_on_activities_categories(self):
        dict_of_activities_categories = {}
        for day in self.list_of_days:
            for activity in day.list_of_activities_for_day:
                if (
                    dict_of_activities_categories.get(activity.activity_category, None)
                    is None
                ):
                    dict_of_activities_categories[activity.activity_category] = (
                        activity.calculate_activity_duration_in_minutes()
                    )
                else:
                    dict_of_activities_categories[
                        activity.activity_category
                    ] += activity.calculate_activity_duration_in_minutes()
        return dict_of_activities_categories

    def get_most_popular_activity_category_and_time_spend_on_this_activity(self):
        pass

    def get_most_popular_activity_name_and_time_spend_on_this_category(self):
        pass
