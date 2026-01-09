import functools
from typing import Callable
from datetime import date

from core.facade_logic.facade_dairy_manager import DairyFacade
from core.user.user_body_goals import UserBodyDailyGoals
from core.user.user_info import User
from core.user.user_body_info import UserBodyInfo
from core.health_analysis import HealthDailyAnalyzer, HealthInSomePeriodAnalyzer
from core.specification_for_filter import *
from core.health_diary_container import HealthDiary
from core.medication.medication_objects import MedicationReceipt, Medication
from core.medication.medication_manager import MedicationManager
from core.medication.medication_objects import MedicationReceiptList
from core.activity.activity_type import SpecificActivityType
from core.health_analysis import MedicationAnalyzer
from core.medication.medication_manager import (
    convert_list_of_medication_to_dict_with_status,
)
from core.exceptions import (
    LimitCallsError,
    DateOfDayIsGreaterThanTodayError,
    NotExistingReceiptWithAppropriateMedicationObjectError,
)
from core.dto_objects import (
    DailyObjectDTO,
    MedicationDTO,
    convert_list_of_medications_into_list_of_medication_dto,
    generate_daily_dto_object,
)


class MainFacade:

    def __init__(
        self,
        user_obj: User,
        health_daily: HealthDaily,
        health_diary: HealthDiary,
        health_diary_facade: DairyFacade,
        user_body_info: UserBodyInfo,
        user_body_daily_goals: UserBodyDailyGoals,
        health_daily_analyzer: HealthDailyAnalyzer,
        health_in_some_period_analyzer: HealthInSomePeriodAnalyzer,
        medication_manager: MedicationManager,
    ):
        self.user = user_obj
        self.health_daily = health_daily
        self.health_diary = health_diary
        self.health_diary_facade = health_diary_facade
        self.user_body_info = user_body_info
        self.user_body_daily_goals = user_body_daily_goals
        self.health_daily_analyzer = health_daily_analyzer
        self.health_in_some_period_analyzer = health_in_some_period_analyzer
        self.medication_manager = medication_manager

    def __is_date_of_activity_greater_than_today(self, _date: str) -> bool:
        today = date.today()
        _date_of_activity = date.fromisoformat(_date)
        if _date_of_activity <= today:
            return False
        return True

    def add_activity(
        self, activity: SpecificActivityType, date_of_activity: str
    ) -> None:
        if self.__is_date_of_activity_greater_than_today(date_of_activity):
            raise DateOfDayIsGreaterThanTodayError()
        self.health_diary_facade.add_activity(activity, date_of_activity)

    def add_weight(self, weight_value: float, _date: str) -> None:
        if self.__is_date_of_activity_greater_than_today(_date):
            raise DateOfDayIsGreaterThanTodayError()
        self.user_body_info.set_weight(weight_value)
        self.health_diary_facade.set_weight(weight_value, _date)

    def add_height(self, height_value: float, _date: str) -> None:
        if self.__is_date_of_activity_greater_than_today(_date):
            raise DateOfDayIsGreaterThanTodayError()
        self.user_body_info.set_height(height_value)
        self.health_diary_facade.set_height(height_value, _date)

    def add_fat_percentage(self, fat_percentage_value: float, _date: str) -> None:
        if self.__is_date_of_activity_greater_than_today(_date):
            raise DateOfDayIsGreaterThanTodayError()
        self.user_body_info.set_fat_percentage(fat_percentage_value)
        self.health_diary_facade.set_fat_percentage(fat_percentage_value, _date)

    def add_water(self, drunk_water: float, _date: str) -> None:
        if self.__is_date_of_activity_greater_than_today(_date):
            raise DateOfDayIsGreaterThanTodayError()
        self.health_diary_facade.add_amount_of_drunk_water(drunk_water, _date)

    def add_sleep(self, count_hours_to_sleep: float, _date: str) -> None:
        if self.__is_date_of_activity_greater_than_today(_date):
            raise DateOfDayIsGreaterThanTodayError()
        self.health_diary_facade.add_amount_of_sleep(count_hours_to_sleep, _date)

    def add_count_of_steps(self, count_of_steps: int, _date: str) -> None:
        if self.__is_date_of_activity_greater_than_today(_date):
            raise DateOfDayIsGreaterThanTodayError()
        self.health_diary_facade.add_count_steps(count_of_steps, _date)

    def add_burned_calories(self, burned_calories: float, _date: str) -> None:
        if self.__is_date_of_activity_greater_than_today(_date):
            raise DateOfDayIsGreaterThanTodayError()
        self.health_diary_facade.add_burned_calories(burned_calories, _date)

    def change_age(self, age: int) -> None:
        # validate value of age , if < 15 or > 100 error or if less than curr age
        self.user.set_age(age)

    def add_burned_calories_goal_on_day(self, calories: int):
        self.user_body_daily_goals.set_burned_calories_goal(calories)

    def add_water_goal_on_day(self, water: float):
        self.user_body_daily_goals.set_water_goal(water)

    def add_calories_goal_on_day(self, calories: int):
        self.user_body_daily_goals.set_calories_goal(calories)

    def get_total_time_spent_on_activities_in_minutes_current_day(self) -> float:
        return (
            self.health_daily_analyzer.get_total_time_spent_on_activities_in_minutes_current_day()
        )

    def get_remaining_of_consumed_calories_current_day(self) -> float:
        return self.health_daily_analyzer.get_remaining_of_consumed_calories()

    def get_remaining_of_burned_calories_current_day(self) -> float:
        return self.health_daily_analyzer.get_remaining_of_burned_calories()

    def get_remaining_water_current_day(self) -> float:
        return self.health_daily_analyzer.get_remaining_water()

    def get_total_consumed_calories_current_day(self) -> float:
        return self.health_daily_analyzer.get_consumed_calories()

    def get_total_burned_calories_current_day(self) -> float:
        return self.health_daily_analyzer.get_burned_calories()

    def get_total_consumed_water_current_day(self) -> float:
        return self.health_daily_analyzer.get_consumed_water()

    def get_total_sleep_duration_current_day(self) -> float:
        return self.health_daily_analyzer.get_sleep_duration()

    def get_total_steps_current_day(self) -> float:
        return self.health_daily_analyzer.get_count_of_steps_for_day()

    def get_daily_results(self) -> DailyObjectDTO:
        dict_of_res = self.health_daily_analyzer.get_daily_result()
        return generate_daily_dto_object(dict_of_res)

    def get_total_time_spent_on_activities_in_minutes_for_all_time(self) -> float:
        return (
            self.health_in_some_period_analyzer.get_total_time_spent_on_activities_in_minutes_for_all_time()
        )

    def get_total_consumed_calories_for_all_time(self) -> float:
        return (
            self.health_in_some_period_analyzer.get_total_consumed_calories_for_all_time()
        )

    def get_total_burned_calories_for_all_time(self) -> float:
        return (
            self.health_in_some_period_analyzer.get_total_burned_calories_for_all_time()
        )

    def get_total_steps_for_all_time(self) -> float:
        return self.get_total_steps_for_all_time()

    def get_total_time_spent_on_specific_category_of_activities_for_all_time(
        self, activity_category
    ) -> float:
        return self.health_in_some_period_analyzer.get_total_time_spent_on_specific_category_of_activities_for_all_time(
            activity_category
        )

    def get_day_with_max_consumed_calories_for_all_time(self) -> HealthDaily:
        return (
            self.health_in_some_period_analyzer.get_day_with_max_consumed_calories_for_all_time()
        )

    def get_day_with_max_burned_calories_for_all_time(self) -> HealthDaily:
        return (
            self.health_in_some_period_analyzer.get_day_with_max_burned_calories_for_all_time()
        )

    def get_day_with_max_steps_for_all_time(self) -> HealthDaily:
        return self.health_in_some_period_analyzer.get_day_with_max_steps_for_all_time()

    def get_day_with_max_time_spent_on_activities_for_all_time(self) -> HealthDaily:
        return (
            self.health_in_some_period_analyzer.get_day_with_max_time_spent_on_activities_for_all_time()
        )

    def get_day_with_max_amount_of_drunk_water_for_all_time(self) -> HealthDaily:
        return (
            self.health_in_some_period_analyzer.get_day_with_max_amount_of_drunk_water_for_all_time()
        )

    def get_day_with_max_hours_spent_on_sleep_for_all_time(self) -> HealthDaily:
        return (
            self.health_in_some_period_analyzer.get_day_with_max_hours_spent_on_sleep_for_all_time()
        )

    def get_result_of_analyze_some_period(self) -> str:
        return self.health_in_some_period_analyzer.get_result_of_analyze_some_period()

    def filter(
        self, specification: Specification, list_of_all_days: list[HealthDaily]
    ) -> list[HealthDaily]:
        return [day for day in list_of_all_days if specification.is_satisfy_by(day)]

    def took_medication_object(self, medication_obj: Medication):
        """When user tap "Take" for specific medication object this method is called."""
        if (
            self.medication_manager.list_of_receipts.find_receipt_with_appropriate_med_obj(
                medication_obj
            )
            is None
        ):
            raise NotExistingReceiptWithAppropriateMedicationObjectError(
                f"{medication_obj.__repr__()} does not exist in list of receipts"
            )

        self.health_diary_facade.add_took_medication_object(medication_obj)
        self.medication_manager.took_medication_object(medication_obj)

    def took_medication_object_with_no_today_date(
        self, medication_obj: Medication, date_of_taken: str
    ):
        """This method need for provide scalability way of taken medication object.
        If user forgot mark in app that he took the med_obj he can mark this in any day.
        """

        if (
            self.medication_manager.list_of_receipts.find_receipt_with_appropriate_med_obj(
                medication_obj
            )
            is None
        ):
            raise NotExistingReceiptWithAppropriateMedicationObjectError(
                f"{medication_obj.__repr__()} does not exist in list of receipts"
            )

        self.health_diary_facade.add_took_medication_object_with_no_today_date(
            medication_obj, date_of_taken
        )
        self.medication_manager.took_medication_object_with_no_today_date(
            medication_obj
        )

    def get_medications_that_need_to_take_today(self) -> dict[MedicationDTO, bool]:
        """This method return dict that contains a medication object as key and False as value.
        This dict contains only medication objects that need to take today."""
        return convert_list_of_medication_to_dict_with_status(
            convert_list_of_medications_into_list_of_medication_dto(
                self.medication_manager.get_list_of_medications_that_need_to_take_today()
            )
        )

    def get_list_of_all_available_receipts(self) -> list[MedicationReceipt]:
        """This method return a list of all available medication receipts."""
        return self.medication_manager.get_list_of_all_available_receipts()

    def get_list_of_skipped_medication(self) -> list[tuple[Medication, str]]:
        """This method return list of skipped day when concrete medication object needed to be taken"""
        return self.medication_manager.get_list_of_all_medication_that_user_not_take()

    def add_receipt(self, receipt: MedicationReceipt):
        """This method call "add_medication_receipt(receipt: MedicationReceipt)" method of MedicationManager class to add receipt to list of receipts"""
        self.medication_manager.add_medication_receipt(receipt)

    def get_today_day(self) -> HealthDaily:
        if self.health_diary_facade.is_current_day(str(date.today())):
            return self.health_diary_facade.current_day
        self.health_diary_facade.update_curr_day()
        return self.health_diary_facade.current_day


def limit_calls(limit: int):
    def decorator(func: Callable[[User], MainFacade]):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal limit
            if limit == 0:
                raise LimitCallsError("Limit of calling is exhausted")
            res = func(*args, **kwargs)
            limit -= 1
            return res

        return wrapper

    return decorator


# @limit_calls(1)
def create_and_configure_facade_for_start(user_obj: User) -> MainFacade:
    first_day = HealthDaily(str(date.today()))
    health_diary = HealthDiary()
    user_body_info = UserBodyInfo()
    med_receipt_list = MedicationReceiptList()
    user_body_daily_goals = UserBodyDailyGoals()
    medication_manager = MedicationManager(med_receipt_list, health_diary)
    medication_analyzer = MedicationAnalyzer(health_diary, med_receipt_list)
    dairy_facade = DairyFacade(health_diary, first_day, medication_manager)
    health_daily_analyzer = HealthDailyAnalyzer()
    health_in_some_period_analyzer = HealthInSomePeriodAnalyzer()
    medication_manager.set_medication_analyzer(medication_analyzer)

    health_daily_analyzer.set_user_body_daily_goals(user_body_daily_goals)
    health_daily_analyzer.set_user_body_info(user_body_info)
    health_daily_analyzer.set_day_that_need_to_analyze(first_day)
    health_daily_analyzer.set_user_info(user_obj)

    health_in_some_period_analyzer.set_list_of_days(health_diary.get_history_of_days())

    main_facade = MainFacade(
        user_obj,
        first_day,
        health_diary,
        dairy_facade,
        user_body_info,
        user_body_daily_goals,
        health_daily_analyzer,
        health_in_some_period_analyzer,
        medication_manager,
    )

    return main_facade
