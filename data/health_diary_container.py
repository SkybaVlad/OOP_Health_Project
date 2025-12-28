from services.health_daily.daily_health import HealthDaily
from services.time_logic import (
    convert_data_from_string_to_number_format_yyyy_mm_dd_in_numbers,
)


class HealthDiary:
    """This class is a container for HealthDiary objects"""

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, "initialize"):
            self.history_of_all_days: list[HealthDaily] = []
            self.initialize = True

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
            key=lambda day: convert_data_from_string_to_number_format_yyyy_mm_dd_in_numbers(
                day.date_of_day
            ),
        )

    def get_history_of_days(self) -> list[HealthDaily]:
        return self.history_of_all_days
