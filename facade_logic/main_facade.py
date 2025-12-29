from facade_logic.facade_dairy_manager import DairyFacade
from services.user.user_body_goals import UserBodyDailyGoals
from services.user.user_info import User
from services.user.user_body_info import UserBodyInfo
from services.health_analysis import HealthDailyAnalyzer, HealthInSomePeriodAnalyzer
from services.specification_for_filter import *
from data.health_diary_container import HealthDiary
import time
from services.medication.medication import (
    MedicationReceipt,
    Medication,
    MedicationManager,
)
from services.validation_user_input.user_info_validation import validate_age
from services.medication.medication import MedicationReceiptList
from services.activities.activity_type import SpecificActivityType
from services.time_logic import time_validator_format_yyyy_mm_dd


class MainFacade:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            return super().__new__(cls)
        return cls.__instance

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
        if not hasattr(self, "initialize"):
            self.user = user_obj
            self.health_daily = health_daily
            self.health_diary = health_diary
            self.health_diary_facade = health_diary_facade
            self.user_body_info = user_body_info
            self.user_body_daily_goals = user_body_daily_goals
            self.health_daily_analyzer = health_daily_analyzer
            self.health_in_some_period_analyzer = health_in_some_period_analyzer
            self.medication_manager = medication_manager
            self.initialize = True

    def add_activity(self, activity: SpecificActivityType, date) -> None:
        try:
            time_validator_format_yyyy_mm_dd(date)
        except (ValueError, TypeError):
            pass
        self.health_diary_facade.add_activity(activity, date)

    def add_weight(self, weight_value, date: str) -> None:
        try:
            time_validator_format_yyyy_mm_dd(date)
        except (ValueError, TypeError):
            pass
        self.user_body_info.set_weight(weight_value)
        self.health_diary_facade.set_weight(weight_value, date)

    def add_height(self, height_value, date: str) -> None:
        try:
            time_validator_format_yyyy_mm_dd(date)
        except (ValueError, TypeError):
            pass
        self.user_body_info.set_height(height_value)
        self.health_diary_facade.set_height(height_value, date)

    def add_fat_percentage(self, fat_percentage_value, date: str) -> None:
        try:
            time_validator_format_yyyy_mm_dd(date)
        except (ValueError, TypeError):
            pass
        self.user_body_info.set_fat_percentage(fat_percentage_value)
        self.health_diary_facade.set_fat_percentage(fat_percentage_value, date)

    def change_age(self, age: int) -> None:
        validate_age(age)
        self.user.age = age

    def add_burn_calories_goal_on_day(self, calories: int):
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

    def get_daily_results(self) -> str:
        return self.health_daily_analyzer.get_daily_result()

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

    def add_medication_receipt(self, medication_receipt: MedicationReceipt):
        # validate data
        self.medication_manager.add_medication_receipt(medication_receipt)

    def took_medication_receipt(self, medication_object: Medication):
        self.health_diary_facade.medication_manager.took_medication_object(
            medication_object
        )
        self.health_diary_facade.add_took_medication_object(medication_object)
        self.medication_manager.took_medication_object(medication_object)

    def no_took_medication(self, medication_receipt: MedicationReceipt):
        # medication_receipt with STATUS==NOT_TAKEN
        pass

    def get_medications_that_need_to_take_today(self):
        return self.medication_manager.get_medications_that_need_to_take_today()

    def get_list_of_all_available_receipts(self):
        return self.medication_manager.get_list_of_all_available_receipts()

    def get_list_of_skipped_medication(self):
        pass


def create_and_configure_facade_for_start(user_obj: User) -> MainFacade:
    first_day = HealthDaily(time.strftime("%Y-%m-%d", time.localtime()))
    health_diary = HealthDiary()
    user_body_info = UserBodyInfo()
    med_receipt_list = MedicationReceiptList()
    user_body_daily_goals = UserBodyDailyGoals()
    dairy_facade = DairyFacade(health_diary, first_day, med_receipt_list)
    health_daily_analyzer = HealthDailyAnalyzer()
    health_in_some_period_analyzer = HealthInSomePeriodAnalyzer()

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
    )

    return main_facade


# receipt = building receipt object
# facade.add(receipt)
# facade
#
#
#
#
#
#
#
#
#
#
