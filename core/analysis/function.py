import datetime
from core.activity.activity_type import SpecificActivityType
from core.daily_health import HealthDaily
from core.validation_user_input.time_validator import time_in_period


def sort_days(list_of_days):
    pass


def get_list_of_days_in_some_period(
    start_time: str, end_time: str, list_of_days: list[HealthDaily]
) -> list[HealthDaily]:

    lst_of_days = []

    start_time = datetime.date.fromisoformat(start_time)
    end_time = datetime.date.fromisoformat(end_time)

    while True:

        found = False

        if start_time > end_time:
            break

        for day in list_of_days:
            if datetime.date.fromisoformat(day.date_of_day) == start_time:
                lst_of_days.append(day)
                found = True
                break

        if not found:
            lst_of_days.append(HealthDaily(start_time.isoformat()))

        start_time = start_time + datetime.timedelta(days=1)

    return lst_of_days

    # lst_of_days = []
    # for day in list_of_days:
    #     if time_in_period(start_time, end_time, day.date_of_day):
    #         lst_of_days.append(day)


def get_list_of_activities_from_days(
    list_of_days: list[HealthDaily],
) -> list[SpecificActivityType]:
    lst_of_activities = []
    for day in list_of_days:
        for activity in day.list_of_activities_for_day:
            lst_of_activities.append(activity)
    return lst_of_activities
