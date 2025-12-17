from facade_logic.facade_dairy_manager import DairyFacade
from services.user.user_body_goals import UserBodyDailyGoals
from services.user.user_info import User
from services.user.user_body_info import UserBodyInfo
from services.health_analysis import HealthDailyAnalyzer, HealthInSomePeriodAnalyzer
from services.specification_for_filter import *
from data.health_diary_container import HealthDiary
import time
from services.activities.activity_type import SpecificActivityType


class MainFacade:

    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(
        self,
        user_obj: User,
        health_diary_facade: DairyFacade,
        user_body_info: UserBodyInfo,
        user_body_daily_goals: UserBodyDailyGoals,
        health_daily_analyzer: HealthDailyAnalyzer,
        health_in_some_period_analyzer: HealthInSomePeriodAnalyzer,
    ):
        self.user = user_obj
        self.health_diary_facade = health_diary_facade
        self.user_body_info = user_body_info
        self.user_body_daily_goals = user_body_daily_goals
        self.health_daily_analyzer = health_daily_analyzer
        self.health_in_some_period_analyzer = health_in_some_period_analyzer

    def add_weight(self, weight_value, date: str) -> None:
        self.user_body_info.set_weight(weight_value)
        self.health_diary_facade.set_weight(weight_value, date)

    def add_height(self, height_value, date: str) -> None:
        self.user_body_info.set_height(height_value)
        self.health_diary_facade.set_height(height_value, date)

    def add_fat_percentage(self, fat_percentage_value, date: str) -> None:
        self.user_body_info.set_fat_percentage(fat_percentage_value)
        self.health_diary_facade.set_fat_percentage(fat_percentage_value, date)

    def get_total_time_spent_on_activities_in_minutes_current_day(self) -> float:
        self.health_daily_analyzer.set_day_that_need_to_analyze(
            self.health_diary_facade.current_day
        )
        return (
            self.health_daily_analyzer.get_total_time_spent_on_activities_in_minutes_current_day()
        )

    def get_remaining_of_consumed_calories_current_day(self) -> float:
        self.health_daily_analyzer.set_day_that_need_to_analyze(
            self.health_diary_facade.current_day
        )
        return self.health_daily_analyzer.get_remaining_of_consumed_calories()

    def get_remaining_of_burned_calories_current_day(self) -> float:
        self.health_daily_analyzer.set_day_that_need_to_analyze(
            self.health_diary_facade.current_day
        )
        return self.health_daily_analyzer.get_remaining_of_burned_calories()

    def get_remaining_water_current_day(self) -> float:
        self.health_daily_analyzer.set_day_that_need_to_analyze(
            self.health_diary_facade.current_day
        )
        return self.health_daily_analyzer.get_remaining_water()

    def get_total_consumed_calories_current_day(self) -> float:
        self.health_daily_analyzer.set_day_that_need_to_analyze(
            self.health_diary_facade.current_day
        )
        return self.health_daily_analyzer.get_consumed_calories()

    def get_total_burned_calories_current_day(self) -> float:
        self.health_daily_analyzer.set_day_that_need_to_analyze(
            self.health_diary_facade.current_day
        )
        return self.health_daily_analyzer.get_burned_calories()

    def get_total_consumed_water_current_day(self) -> float:
        self.health_daily_analyzer.set_day_that_need_to_analyze(
            self.health_diary_facade.current_day
        )
        return self.health_daily_analyzer.get_consumed_water()

    def get_total_sleep_duration_current_day(self) -> float:
        self.health_daily_analyzer.set_day_that_need_to_analyze(
            self.health_diary_facade.current_day
        )
        return self.health_daily_analyzer.get_sleep_duration()

    def get_total_steps_current_day(self) -> float:
        self.health_daily_analyzer.set_day_that_need_to_analyze(
            self.health_diary_facade.current_day
        )
        return self.health_daily_analyzer.get_count_of_steps_for_day()

    def get_daily_results(self) -> str:
        self.health_daily_analyzer.set_day_that_need_to_analyze(
            self.health_diary_facade.current_day
        )
        return self.health_daily_analyzer.get_daily_results()

    def get_total_time_spent_on_activities_in_minutes_for_period_of_time(
        self, start_data: str, end_data: str
    ) -> int:
        self.health_in_some_period_analyzer.set_period_of_time(start_data, end_data)
        return (
            self.health_in_some_period_analyzer.get_total_time_spent_on_activities_in_minutes_for_period_of_time()
        )

    def get_total_consumed_calories_for_period_of_time(
        self, start_data: str, end_data: str
    ) -> float:
        self.health_in_some_period_analyzer.set_period_of_time(start_data, end_data)
        return (
            self.health_in_some_period_analyzer.get_total_consumed_calories_for_period_of_time()
        )

    def get_total_burned_calories_for_period_of_time(
        self, start_data: str, end_data: str
    ) -> float:
        self.health_in_some_period_analyzer.set_period_of_time(start_data, end_data)
        return (
            self.health_in_some_period_analyzer.get_total_burned_calories_for_period_of_time()
        )

    def get_total_steps_for_period_of_time(
        self, start_data: str, end_data: str
    ) -> float:
        self.health_in_some_period_analyzer.set_period_of_time(start_data, end_data)
        return self.health_in_some_period_analyzer.get_total_steps_for_period_of_time()

    def get_total_time_spent_on_specific_category_of_activities_for_period_of_time(
        self, activity_category, start_data: str, end_data: str
    ) -> float:
        self.health_in_some_period_analyzer.set_period_of_time(start_data, end_data)
        return self.health_in_some_period_analyzer.get_total_time_spent_on_specific_category_of_activities_for_period_of_time(
            activity_category
        )

    def get_day_with_max_consumed_calories_for_period_of_time(
        self, start_data: str, end_data: str
    ) -> HealthDaily:
        self.health_in_some_period_analyzer.set_period_of_time(start_data, end_data)
        return (
            self.health_in_some_period_analyzer.get_day_with_max_consumed_calories_for_period_of_time()
        )

    def get_day_with_max_burned_calories_for_period_of_time(
        self, start_data: str, end_data: str
    ) -> HealthDaily:
        self.health_in_some_period_analyzer.set_period_of_time(start_data, end_data)
        return (
            self.health_in_some_period_analyzer.get_day_with_max_burned_calories_for_period_of_time()
        )

    def get_day_with_max_steps_for_period_of_time(
        self, start_data: str, end_data: str
    ) -> HealthDaily:
        self.health_in_some_period_analyzer.set_period_of_time(start_data, end_data)
        return (
            self.health_in_some_period_analyzer.get_day_with_max_steps_for_period_of_time()
        )

    def get_day_with_max_time_spent_on_activities_for_period_of_time(
        self, start_data: str, end_data: str
    ) -> HealthDaily:
        self.health_in_some_period_analyzer.set_period_of_time(start_data, end_data)
        return (
            self.health_in_some_period_analyzer.get_day_with_max_time_spent_on_activities_for_period_of_time()
        )

    def get_day_with_max_amount_of_drunk_water_for_period_of_time(
        self, start_data: str, end_data: str
    ) -> HealthDaily:
        self.health_in_some_period_analyzer.set_period_of_time(start_data, end_data)
        return (
            self.health_in_some_period_analyzer.get_day_with_max_amount_of_drunk_water_for_period_of_time()
        )

    def get_day_with_max_hours_spent_on_sleep_for_period_of_time(
        self, start_data: str, end_data: str
    ) -> HealthDaily:
        self.health_in_some_period_analyzer.set_period_of_time(start_data, end_data)
        return (
            self.health_in_some_period_analyzer.get_day_with_max_hours_spent_on_sleep_for_period_of_time()
        )

    def get_result_of_analyze_some_period(self, start_data: str, end_data: str) -> str:
        self.health_in_some_period_analyzer.set_period_of_time(start_data, end_data)
        self.health_in_some_period_analyzer.set_period_of_time(start_data, end_data)
        return self.health_in_some_period_analyzer.get_result_of_analyze_some_period()

    def filter(
        self, specification: Specification, list_of_all_days: list[HealthDaily]
    ) -> list[HealthDaily]:
        return [day for day in list_of_all_days if specification.is_satisfy_by(day)]

    def add_activity(
        self, activity_obj: SpecificActivityType, data_of_activity: str
    ) -> None:
        self.health_diary_facade.add_activity(activity_obj, data_of_activity)

    def get_list_of_days_in_sorted_order(self):
        return self.health_diary_facade.health_diary.get_sorted_list_of_days()


def create_and_configure_facade_for_start(user_obj: User) -> MainFacade:
    """This function uses for configuration a program objects and correcting initialization of all classes
    This function accepts user object and creating all needed object for correcting start of the program.
    """
    first_day = HealthDaily(time.strftime("%Y-%m-%d", time.localtime()))
    health_diary = HealthDiary()
    user_body_info = UserBodyInfo()
    user_body_daily_goals = UserBodyDailyGoals()
    dairy_facade = DairyFacade()
    health_daily_analyzer = HealthDailyAnalyzer(first_day)
    health_in_some_period_analyzer = HealthInSomePeriodAnalyzer()

    dairy_facade.set_health_daily(first_day)
    dairy_facade.set_health_diary(health_diary)

    health_daily_analyzer.set_user_body_daily_goals(user_body_daily_goals)
    health_daily_analyzer.set_user_body_info(user_body_info)
    health_daily_analyzer.set_day_that_need_to_analyze(first_day)
    health_daily_analyzer.set_user_info(user)

    health_diary.add_day(first_day)

    health_in_some_period_analyzer.set_list_of_days(health_diary.get_history_of_days())

    main_facade = MainFacade(
        user_obj,
        dairy_facade,
        user_body_info,
        user_body_daily_goals,
        health_daily_analyzer,
        health_in_some_period_analyzer,
    )

    return main_facade


user = User('Vlad', 'Skyba', 19, 'male')
facade = create_and_configure_facade_for_start(user)
