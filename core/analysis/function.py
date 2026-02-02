from core.activity.activity_type import SpecificActivityType
from core.daily_health import HealthDaily
from core.validation_user_input.time_validator import time_in_period


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
