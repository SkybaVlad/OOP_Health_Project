from services.health_analysis import HealthDailyAnalyzer, HealthInSomePeriodAnalyzer
from services.health_daily.daily_health import HealthDaily
from services.specification_for_filter import Specification


class AnalysisFacade:
    def __init__(self):
        self.health_daily_analyzer: HealthDailyAnalyzer = HealthDailyAnalyzer()
        self.health_analyzer_some_period: HealthInSomePeriodAnalyzer = (
            HealthInSomePeriodAnalyzer()
        )

    def set_list_of_days_that_need_analyze(self, list_of_all_days: list[HealthDaily]):
        self.health_analyzer_some_period.set_list_of_days(list_of_all_days)

    def set_period_of_time_that_need_analyze(
        self, start_period_of_time: str, end_period_of_time: str
    ):
        self.health_analyzer_some_period.set_period_of_time(
            start_period_of_time, end_period_of_time
        )

    def get_result_of_analyze_some_period(self):
        pass

    def get_daily_results(self):
        pass

    def filter(self, specification: Specification):
        pass
