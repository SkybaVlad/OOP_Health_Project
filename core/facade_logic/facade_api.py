import functools
from typing import Callable, Any
from datetime import date

from core.facade_logic.facade_dairy_manager import DairyFacade
from core.user.user_body_goals import UserBodyDailyGoals
from core.user.user_info import User
from core.user.user_body_info import UserBodyInfo
from core.specification_for_filter import *
from core.health_diary_container import HealthDiary
from core.medication.medication_objects import MedicationReceipt, Medication
from core.medication.medication_manager import MedicationManager
from core.medication.medication_objects import MedicationReceiptList
from core.activity.activity_type import SpecificActivityType
from core.medication.medication_manager import (
    convert_list_of_medication_to_dict_with_status,
)
from core.exceptions import (
    LimitCallsError,
    NotExistingReceiptWithAppropriateMedicationObjectError,
)
from core.dto_objects import (
    DailyObjectDTO,
    MedicationDTO,
    convert_list_of_medications_into_list_of_medication_dto,
    generate_daily_dto_object,
)
from core.facade_logic.facade_analysis import FacadeAnalysis


class MainFacade:
    """MainFacade class is a class that provide API for interacting with complex
    health system."""

    def __init__(
        self,
        user_obj: User,
        health_daily: HealthDaily,
        health_diary: HealthDiary,
        health_diary_facade: DairyFacade,
        user_body_info: UserBodyInfo,
        user_body_daily_goals: UserBodyDailyGoals,
        facade_analysis: FacadeAnalysis,
        medication_manager: MedicationManager,
    ):
        self.user = user_obj
        self.health_daily = health_daily
        self.health_diary = health_diary
        self.health_diary_facade = health_diary_facade
        self.user_body_info = user_body_info
        self.user_body_daily_goals = user_body_daily_goals
        self.facade_analysis = facade_analysis
        self.medication_manager = medication_manager

    def add_activity(
        self, activity: SpecificActivityType, date_of_activity: str
    ) -> None:
        """This method add activity object to day with "date_of_activity" date. If day with
        "date_of_activity" date does not exist in list of days, this will be created.
        If _date > str(datetime.date.today()) the DateOfDayIsGreaterThanTodayError() will be raised.
        """
        self.health_diary_facade.add_activity(activity, date_of_activity)

    def add_weight(self, weight_value: float, _date: str) -> None:
        """This method set weight value in UserBodyInfo class ((if _date == str(datetime.date.today())))
        and in Health Daily class with _date date.
        If _date > str(datetime.date.today()) the DateOfDayIsGreaterThanTodayError() will be raised.
        """
        if _date == str(date.today()):  # also need allow if its first add
            self.user_body_info.set_weight(weight_value)
        self.health_diary_facade.set_weight(weight_value, _date)

    def add_height(self, height_value: float, _date: str) -> None:
        """This method set height value in UserBodyInfo class ((if _date == str(datetime.date.today())))
        and in Health Daily class with _date date.
        If _date > str(datetime.date.today()) the DateOfDayIsGreaterThanTodayError() will be raised.
        """
        if _date == str(date.today()):  # also need allow if its first add
            self.user_body_info.set_height(height_value)
        self.health_diary_facade.set_height(height_value, _date)

    def add_fat_percentage(self, fat_percentage_value: float, _date: str) -> None:
        """This method set fat percentage value in UserBodyInfo class (if _date == str(datetime.date.today()))
        and in Health Daily class with _date date.
        If _date > str(datetime.date.today()) the DateOfDayIsGreaterThanTodayError() will be raised.
        """
        if _date == str(date.today()):  # also need allow if its first add
            self.user_body_info.set_fat_percentage(fat_percentage_value)
        self.health_diary_facade.set_fat_percentage(fat_percentage_value, _date)

    def add_water(self, drunk_water: float, _date: str) -> None:
        """This method add count of drunk litres of water to Health Daily object with _date date.
        If _date > str(datetime.date.today()) the DateOfDayIsGreaterThanTodayError() will be raised.
        """
        self.health_diary_facade.add_amount_of_drunk_water(drunk_water, _date)

    def add_sleep(self, count_hours_to_sleep: float, _date: str) -> None:
        """This method add count of sleep hours to Health Daily object with _date date.
        If _date > str(datetime.date.today()) the DateOfDayIsGreaterThanTodayError() will be raised.
        """
        self.health_diary_facade.add_amount_of_sleep(count_hours_to_sleep, _date)

    def add_count_of_steps(self, count_of_steps: int, _date: str) -> None:
        """This method add count of steps to Health Daily object with _date date.
        If _date > str(datetime.date.today()) the DateOfDayIsGreaterThanTodayError() will be raised.
        """
        self.health_diary_facade.add_count_steps(count_of_steps, _date)

    def add_consumed_calories(self, consumed_calories: int, _date: str) -> None:
        self.health_diary_facade.add_consumed_calories(consumed_calories, _date)

    def add_burned_calories(self, burned_calories: float, _date: str) -> None:
        """This method add count of burned calories to Health Daily object with _date date.
        If _date > str(datetime.date.today()) the DateOfDayIsGreaterThanTodayError() will be raised.
        """
        self.health_diary_facade.add_burned_calories(burned_calories, _date)

    def change_age(self, age: int) -> None:
        """This method change user age in User class"""
        # validate value of age , if < 15 or > 100 error or if less than curr age
        self.user.set_age(age)

    def set_burned_calories_goal(self, calories: int):
        """This method set user-defined value of burned calories goal. This
        value will be used in daily analyzer class to analyze daily result"""
        self.user_body_daily_goals.set_burned_calories_goal(calories)
        self.health_diary_facade.current_day.set_burned_calories_goal_on_day(calories)

    def set_water_goal(self, water: float):
        """This method set user-defined value of water goal. This
        value will be used in daily analyzer class to analyze daily result.
        Water goal means count of litres that user need to drink every day."""
        self.user_body_daily_goals.set_water_goal(water)
        self.health_diary_facade.current_day.set_water_goal_on_day(water)

    def set_consumed_calories_goal(self, calories: int):
        """This method set user-defined value of burned goal. This
        value will be used in daily analyzer class to analyze daily result.
        Calories goal means how much calories user need to eat every day."""
        self.user_body_daily_goals.set_consumed_calories_goal(calories)
        self.health_diary_facade.current_day.set_consumed_calories_goal_on_day(calories)

    def set_step_goal(self, step_goal: float):
        """This method set user-defined value of burned calories goal. This
        value will be used in daily analyzer class to analyze daily result"""
        self.user_body_daily_goals.set_step_goal(step_goal)
        self.health_diary_facade.current_day.set_step_goal_on_day(step_goal)

    def get_today_results(self) -> DailyObjectDTO:
        """This method responsible for analyze metrics of current day (current day that in DairyFacade class).
        If current day != str(datetime.date.today()) day in DairyFacade class will be updated otherwise it will
        be analyzed and DailyObjectDTO will be returned."""
        if not self.health_diary_facade.is_current_day(str(date.today())):
            self.health_diary_facade.update_curr_day()
        return generate_daily_dto_object(
            self.facade_analysis.get_result_of_day(self.health_diary_facade.current_day)
        )

    def get_result_of_analyze_some_period(
        self, start_period: str, end_period: str
    ) -> dict[str, Any]:
        return self.facade_analysis.get_result_of_analyze_some_period(
            start_period, end_period
        )

    def get_result_of_another_day(self, date_of_day: str) -> DailyObjectDTO:
        """This method responsible for analyze metrics of any date with "date_of_day" date.
        If "date_of_day" is greater than str(datetime.date.today()) the
        NotExistingDayInListOfDaysWithThisDateError() will be raised otherwise DailyObjectDTO object will
        be returned."""
        dict_of_res = self.facade_analysis.get_daily_result_of_another_day(date_of_day)
        return generate_daily_dto_object(dict_of_res)

    def get_result_of_activity_analysis(
        self, start_time: str | None = None, end_time: str | None = None
    ):
        """By default, period is all time (first day - today)

        This method used on activity page"""
        return self.facade_analysis.get_result_of_activity_analysis(
            start_time, end_time
        )

    def get_result_of_medication_analysis(
        self, start_time: str | None = None, end_time: str | None = None
    ):
        return self.facade_analysis.get_result_of_medication_analysis(
            start_time, end_time
        )

    def get_result_of_nutrition_analysis(
        self, start_time: str | None = None, end_time: str | None = None
    ):
        raise NotImplementedError()

    def get_result_of_water_analysis(self):
        raise NotImplementedError()

    def get_result_of_sleep_analysis(self):
        raise NotImplementedError()

    def filter(
        self, specification: Specification, list_of_all_days: list[HealthDaily]
    ) -> list[HealthDaily]:
        return [day for day in list_of_all_days if specification.is_satisfy_by(day)]

    def took_medication_object(self, medication_obj: Medication):
        """When user tap "Take" for specific medication object this method is called.
        This method responsible for process medication object. If receipt with appropriate
        medication object does not exist "NotExistingReceiptWithAppropriateMedicationObjectError()" will be raised.
        Under hood this medication object added to list of taken medications in current day. Also
        in MedicationManager class відбувається перевірка ...."""

        _receipt_with_med_obj = self.medication_manager.list_of_receipts.find_receipt_with_appropriate_med_obj(
            medication_obj
        )

        if _receipt_with_med_obj is None:
            raise NotExistingReceiptWithAppropriateMedicationObjectError(
                f"{medication_obj.__repr__()} does not exist in list of receipts"
            )
        else:
            self.health_diary_facade.add_took_medication_object(medication_obj)
            self.medication_manager.took_medication_object(
                medication_obj, _receipt_with_med_obj
            )

    def took_medication_object_with_no_today_date(
        self, medication_obj: Medication, date_of_taken: str
    ):
        """This method need for provide scalability way of taken medication object.
        If user forgot mark in app that he took the med_obj he can mark this in any day.
        Under hood this medication object added to list of taken medications in day with "date_of_taken" date.
        If receipt with appropriate medication object does not exist, the
        "NotExistingReceiptWithAppropriateMedicationObjectError()" will be raised."
        """

        self.medication_manager.took_medication_object_with_no_today_date(
            medication_obj
        )
        self.health_diary_facade.add_took_medication_object_with_no_today_date(
            medication_obj, date_of_taken
        )

    def get_medications_that_need_to_take_today(self) -> dict[MedicationDTO, bool]:
        """This method return dict that contains a MedicationDTO object as key and False as value.
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
        """This method return list of skipped day when user do not take appropriates medications.
        Returned value has the next format [(MedicationDTO, date_when_skipped),...,...]
        """
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
    """This function need to be called if you want to interact with health system,
    because this function responsible for configure all settings needed to correctly
    working system."""
    first_day = HealthDaily(str(date.today()))
    container_of_days = HealthDiary()

    med_receipt_list = MedicationReceiptList()
    medication_manager = MedicationManager(med_receipt_list)

    user_body_info = UserBodyInfo()
    user_body_daily_goals = UserBodyDailyGoals()

    dairy_facade = DairyFacade()
    dairy_facade.initialize(
        container_of_days,
        first_day,
        medication_manager,
        user_body_daily_goals,
        user_obj,
    )
    dairy_facade.load_goals_on_day(first_day)

    facade_analysis = FacadeAnalysis()
    facade_analysis.initialize(
        str(date.today()),
        str(date.today()),
        dairy_facade.health_diary.history_of_all_days,
        first_day,
        med_receipt_list,
        user_body_daily_goals,
        user_body_info,
        user_obj,
        container_of_days,
    )

    medication_manager.set_medication_analyzer(facade_analysis.medication_analyzer)

    main_facade = MainFacade(
        user_obj,
        first_day,
        container_of_days,
        dairy_facade,
        user_body_info,
        user_body_daily_goals,
        facade_analysis,
        medication_manager,
    )

    return main_facade
