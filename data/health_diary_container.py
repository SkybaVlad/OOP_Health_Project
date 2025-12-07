from services.health_daily.daily_health import HealthDaily
from services.time_logic import convert_data_from_string_to_number


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

    def get_sorted_list_of_days(self):
        return sorted(
            self.history_of_all_days,
            key=lambda day: convert_data_from_string_to_number(day.date_of_day),
        )

    def get_history_of_days(self) -> list[HealthDaily]:
        return self.history_of_all_days
