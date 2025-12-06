from services.health_daily_track.health_analysis import HealthDailyAnalyzer, HealthAnalyzerInSomePeriod


class AnalysisFacade:
    def __init__(self):
        self.health_daily_analyzer = HealthDailyAnalyzer()
        self.health_analyzer = HealthAnalyzerInSomePeriod()

    def get_daily_results(self):
        health_analyzer = HealthDailyAnalyzer(
            self.health_diary, self.user_body_daily_goals
        )
        return (
            health_analyzer.get_burned_calories(),
            health_analyzer.get_remaining_of_burned_calories(),
            health_analyzer.get_remaining_of_consumed_calories(),
            # body_metrics
            health_analyzer.get_consumed_calories(),
            health_analyzer.get_consumed_water(),
            health_analyzer.get_remaining_water(),
            health_analyzer.get_sleep_duration(),
            health_analyzer.get_total_time_spent_on_activities_in_minutes(),
        )
