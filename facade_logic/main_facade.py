from facade_logic.facade_dairy_manager import DairyFacade
from services.user.user_body_goals import UserBodyDailyGoals
from services.user.user_info import User
from services.user.user_body_info import UserBodyInfo
from services.health_analysis import HealthDailyAnalyzer, HealthInSomePeriodAnalyzer
from services.specification_for_filter import *
from services.time_logic import time_converter_minutes_in_hours
from data.health_diary_container import HealthDiary
import time


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
    ):
        self.user = user_obj
        self.health_daily = health_daily
        self.health_diary = health_diary
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
        date_of_curr_day = self.health_daily_analyzer.health_daily.date_of_day
        return (
            f"Daily result {date_of_curr_day}"
            f"Total time spent on activities - {self.get_total_time_spent_on_activities_in_minutes_current_day()}"
            f"Total amount of steps - {self.get_total_steps_current_day()}"
            f"Total hours of sleep - {self.get_total_sleep_duration_current_day()}"
            f"Total consumed calories - {self.get_total_consumed_calories_current_day()}"
            f"Total consumed water - {self.get_total_consumed_water_current_day()}"
            f"Total burned calories - {self.get_total_burned_calories_current_day()}"
            f"Remaining water - {self.get_remaining_water_current_day()}"
            f"Remaining burned calories - {self.get_remaining_of_burned_calories_current_day()}"
            f"Remaining consumed calories - {self.get_remaining_of_consumed_calories_current_day()}"
            f"Body Mass Metrics - {self.health_daily_analyzer.calculate_body_mass_index}"
            f"Basal Metabolic Rate - {self.health_daily_analyzer.calculate_basal_metabolic_rate}"
            f"Lean Body Mass Index - {self.health_daily_analyzer.calculate_lean_body_mass_index}"
            f"Fat Mass - {self.health_daily_analyzer.calculate_fat_mass}"
        )

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
        day_with_max_consumed_calories = (
            self.get_day_with_max_consumed_calories_for_all_time()
        )
        day_with_max_burned_calories = (
            self.get_day_with_max_burned_calories_for_all_time()
        )
        day_with_max_steps = self.get_day_with_max_steps_for_all_time()
        day_with_max_time_spent_on_activities = (
            self.get_day_with_max_time_spent_on_activities_for_all_time()
        )
        day_with_max_amount_of_drunk_water = (
            self.get_day_with_max_amount_of_drunk_water_for_all_time()
        )
        day_with_max_hours_of_sleep = (
            self.get_day_with_max_hours_spent_on_sleep_for_all_time()
        )
        return (
            f"Statistics from {self.health_in_some_period_analyzer.start_data} to {self.health_in_some_period_analyzer.end_data}"
            f"Total time spent on activities {time_converter_minutes_in_hours(self.get_total_time_spent_on_activities_in_minutes_for_all_time())}"
            f"Total consumed calories {self.get_total_consumed_calories_for_all_time()}"
            f"Total burned calories {self.get_total_burned_calories_for_all_time()}"
            f"Total steps {self.get_total_steps_for_all_time()}"
            f"Total time spent on Cardio activity {self.get_total_time_spent_on_specific_category_of_activities_for_all_time("Cardio")}"
            f"Total time spent on Sport activity {self.get_total_time_spent_on_specific_category_of_activities_for_all_time("Sport")}"
            f"Day with max consumed calories {day_with_max_consumed_calories.date_of_day} - {day_with_max_consumed_calories.consumed_calories_for_day}"
            f"Day with max burned calories {day_with_max_burned_calories.date_of_day} - {day_with_max_burned_calories.burned_calories_for_day}"
            f"Day with max amount of steps {day_with_max_steps.date_of_day} - {day_with_max_steps.count_of_steps_for_day}"
            f"Day with max time spent on activities {day_with_max_time_spent_on_activities.date_of_day} - {day_with_max_time_spent_on_activities.total_time_spend_on_activities}"
            f"Day with max amount of drunk water {day_with_max_amount_of_drunk_water.date_of_day} - {day_with_max_amount_of_drunk_water.drunk_water}"
            f"Day with max hours of sleep {day_with_max_hours_of_sleep.date_of_day} - {day_with_max_hours_of_sleep.sleep_duration}"
        )

    def filter(
        self, specification: Specification, list_of_all_days: list[HealthDaily]
    ) -> list[HealthDaily]:
        return [day for day in list_of_all_days if specification.is_satisfy_by(day)]


def create_and_configure_facade_for_start(user_obj: User) -> MainFacade:
    first_day = HealthDaily(time.strftime("%Y-%m-%d", time.localtime()))
    health_diary = HealthDiary()
    user_body_info = UserBodyInfo()
    user_body_daily_goals = UserBodyDailyGoals()
    dairy_facade = DairyFacade()
    health_daily_analyzer = HealthDailyAnalyzer()
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
        first_day,
        health_diary,
        dairy_facade,
        user_body_info,
        user_body_daily_goals,
        health_daily_analyzer,
        health_in_some_period_analyzer,
    )

    return main_facade


user = User('Vlad', 'Skyba', 19, 'male')
facade = create_and_configure_facade_for_start(user)
facade.add_weight(100, "2025-01-01")
