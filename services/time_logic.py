import datetime
import math
from services.validation_user_input.time_validator import (
    time_validator_format_yyyy_mm_dd,
    time_validator_format_hh_mm,
    is_source_time_less_than_target_time,
)
import time


def convert_data_from_string_to_number_format_yyyy_mm_dd_in_numbers(date: str) -> int:
    """This function gets a date with the next format YYYY-MM-DD and return value with the next format YYYYMMDD"""
    time_validator_format_yyyy_mm_dd(date)
    return int(date.replace("-", ""))


def time_converter_minutes_in_hours(time_in_minutes: int):
    """This function gets a time value in minutes and converts it to hours and minutes.
    Function return the hours as first value and minutes as second value.
    Example time_converter_minutes_in_hours(150) -> 2 (hours),30(minutes) because 2*60=120, 150-120=30 minutes
    """
    if type(time_in_minutes) != int:
        raise TypeError("The time input is not a float or int")
    if time_in_minutes < 0:
        raise ValueError("The time can not be negative")
    hours = math.floor(time_in_minutes / 60)
    minutes = time_in_minutes - hours * 60
    return hours, minutes


def calculate_duration_of_activity(
    start_time_of_activity: str, end_time_of_activity: str
) -> int:
    """return time duration in minutes
    For example start_time = 17:30, end_time = 19:30
    Return 120 minutes
    start_time_of_activity and end_time_of_activity are both strings
    and should have the next format HH:MM"""
    raise NotImplementedError()
    time_obj_source = datetime.time.fromisoformat(start_time_of_activity)
    time_obj_target = datetime.time.fromisoformat(end_time_of_activity)

    # start_time_of_activity = start_time_of_activity.split(':')
    # end_time_of_activity = end_time_of_activity.split(':')
    # for i in range(len(start_time_of_activity)):
    #     start_time_of_activity[i] = int(start_time_of_activity[i])
    #     end_time_of_activity[i] = int(end_time_of_activity[i])
    # if end_time_of_activity[1] < start_time_of_activity[1]:
    #     end_time_of_activity[1] += 60
    #     end_time_of_activity[0] -= 1
    # if end_time_of_activity[0] < start_time_of_activity[0]:
    #     end_time_of_activity[0] += 24
    # result: list[int] = [0, 0]
    # result[1] = math.fabs(end_time_of_activity[1] - start_time_of_activity[1])
    # result[0] = end_time_of_activity[0] - start_time_of_activity[0]
    # res_in_minutes = result[0] * 60 + result[1]
    # return res_in_minutes


def increase_date_by_one_day(date: str) -> str:
    # date -> YYYY-MM-DD

    tmp = date.split("-")  # -> ["YYYY","MM","DD"]

    return time.strftime(
        "%Y-%m-%d",
        time.localtime(
            time.mktime((int(tmp[0]), int(tmp[1]), int(tmp[2]), 0, 0, 0, 0, 0, 0))
            + 86400
        ),
    )


def get_list_of_all_dates_between_start_and_end(start_time, end_time) -> list[str]:
    lst = []
    while is_source_time_less_than_target_time(start_time, end_time):
        lst.append(start_time)
        start_time = increase_date_by_one_day(start_time)
    return lst
