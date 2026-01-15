from core.exceptions import NotExistingDayInListOfDaysWithThisDateError
from core.health_diary_container import HealthDiary
from core.user.user_info import User
from core.activity.activity_type import SpecificActivityType
from core.analysis.medication_analysis import MedicationAnalyzer
from core.analysis.activity_analysis import ActivityAnalyzer
from core.analysis.daily_analysis import HealthDailyAnalyzer
from core.analysis.some_period_analysis import HealthInSomePeriodAnalyzer
from core.daily_health import HealthDaily
from core.medication.medication_objects import MedicationReceiptList
from core.user.user_body_goals import UserBodyDailyGoals
from core.user.user_body_info import UserBodyInfo
from core.validation_user_input.time_validator import time_in_period


class FacadeAnalysis:
    def __init__(self):
        self.daily_analyzer: HealthDailyAnalyzer | None = None
        self.some_period_analyzer: HealthInSomePeriodAnalyzer | None = None
        self.activity_analyzer: ActivityAnalyzer | None = None
        self.medication_analyzer: MedicationAnalyzer | None = None
        self.days_container: HealthDiary | None = None

    def initialize(
        self,
        start_time: str,
        end_time: str,
        list_of_days: list[HealthDaily],
        first_day: HealthDaily,
        list_of_receipts: MedicationReceiptList,
        user_body_daily_goals: UserBodyDailyGoals,
        user_body_info: UserBodyInfo,
        user_obj: User,
        health_diary: HealthDiary,
    ):
        self.daily_analyzer = HealthDailyAnalyzer()
        self.daily_analyzer.set_day_that_need_to_analyze(first_day)
        self.daily_analyzer.set_user_body_daily_goals(user_body_daily_goals)
        self.daily_analyzer.set_user_body_info(user_body_info)
        self.daily_analyzer.set_user_info(user_obj)

        self.activity_analyzer = ActivityAnalyzer()
        self.activity_analyzer.load_default_values_to_initialize(
            start_time,
            end_time,
            get_list_of_activities_from_days(
                get_list_of_days_in_some_period(start_time, end_time, list_of_days)
            ),
        )

        self.days_container = health_diary

        self.medication_analyzer = MedicationAnalyzer(health_diary, list_of_receipts)

        self.some_period_analyzer = HealthInSomePeriodAnalyzer()
        self.some_period_analyzer.load_default_values_to_initialize(
            start_time,
            end_time,
            get_list_of_days_in_some_period(start_time, end_time, list_of_days),
            self.activity_analyzer,
            self.medication_analyzer,
        )

    def get_daily_results(self):
        return self.daily_analyzer.get_daily_result()

    def get_result_of_analyze_some_period(self, start_time: str, end_time: str):
        return self.some_period_analyzer.get_result_of_analyze_some_period()

    def get_daily_result_of_another_day(self, date_of_day: str):
        day = self.days_container.find_day(date_of_day)
        if day is None:
            raise NotExistingDayInListOfDaysWithThisDateError(
                f"Day with {date_of_day} does not exist"
            )
        self.daily_analyzer.set_day_that_need_to_analyze(day)
        dict_of_res = self.daily_analyzer.get_daily_result()
        return dict_of_res

    def set_day_that_need_to_analyze_for_daily_results(self, day: HealthDaily):
        self.daily_analyzer.set_day_that_need_to_analyze(day)


def get_list_of_days_in_some_period(
    start_time: str, end_time: str, list_of_days: list[HealthDaily]
) -> list[HealthDaily]:
    lst_of_days = []
    for day in list_of_days:
        if time_in_period(start_time, end_time, day.date_of_day):
            lst_of_days.append(day)
    return lst_of_days


def get_list_of_activities_from_days(
    list_of_days: list[HealthDaily],
) -> list[SpecificActivityType]:
    lst_of_activities = []
    for day in list_of_days:
        for activity in day.list_of_activities_for_day:
            lst_of_activities.append(activity)
    return lst_of_activities
