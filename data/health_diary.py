from services.health_daily.daily_health import HealthDaily


class HealthDiary:
    def __init__(self):
        self.history_of_all_days = []

    def add_day(self, specific_day: HealthDaily):
        self.history_of_all_days.append(specific_day)

    def get_history_of_days(self) -> list[HealthDaily]:
        return self.history_of_all_days
