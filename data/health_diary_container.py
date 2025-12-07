from services.health_daily.daily_health import HealthDaily


class HealthDiary:
    """This class is a container for HealthDiary objects"""

    def __init__(self):
        self.history_of_all_days: list[HealthDaily] = []

    def add_day(self, specific_day: HealthDaily):
        day = self.find_day(specific_day.date_of_day)
        if day is not None:
            return day
        else:
            self.history_of_all_days.append(specific_day)
            return None

    def find_day(self, date: str) -> HealthDaily | None:
        for day in self.history_of_all_days:
            if day.date_of_day == date:
                return day
        return None

    def sort(self):
        pass

    def get_history_of_days(self) -> list[HealthDaily]:
        return self.history_of_all_days
