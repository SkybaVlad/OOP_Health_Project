import math
import datetime


def time_in_period(start_time: str, end_time: str, current_time: str):
    """This function compare current time with start time and end time. Return True if current time located
    in period between start and end time and Return False otherwise. The time vars have the next format YYYY-MM-DD
    """
    time_validator_format_yyyy_mm_dd(start_time)
    time_validator_format_yyyy_mm_dd(end_time)
    time_validator_format_yyyy_mm_dd(current_time)
    start_time = start_time.split("-")  # [YYYY,MM,DD]
    end_time = end_time.split("-")
    current_time = current_time.split("-")

    if current_time[0] == start_time[0] and current_time[0] == end_time[0]:
        if current_time[1] > start_time[1] and current_time[1] < end_time[1]:
            return True
        elif current_time[1] == start_time[1] and current_time[1] < end_time[1]:
            if current_time[2] >= start_time[2]:
                return True
        elif current_time[1] > start_time[1] and current_time[1] == end_time[1]:
            if current_time[2] <= end_time[2]:
                return True
        elif current_time[1] == start_time[1] and current_time[1] == end_time[1]:
            if current_time[2] >= start_time[2] and current_time[2] <= end_time[2]:
                return True
    elif current_time[0] == start_time[0] and current_time[0] < end_time[0]:
        if current_time[1] > start_time[1]:
            return True
        elif current_time[1] == start_time[1]:
            if current_time[2] >= start_time[2]:
                return True
    elif current_time[0] > start_time[0] and current_time[0] == end_time[0]:
        if current_time[1] < end_time[1]:
            return True
        elif current_time[1] == end_time[1]:
            if current_time[2] <= end_time[2]:
                return True
    return False


def convert_data_from_string_to_number_format_yyyy_mm_dd_in_numbers(date: str):
    """This function gets a date with the next format YYYY-MM-DD and return value with the next format YYYYMMDD"""
    return int(date.replace("-", ""))


def time_converter_minutes_in_hours(time_in_minutes: float):
    """This function gets a time value in minutes and converts it to hours and minutes.
    Function return the hours as first value and minutes as second value.
    Example time_converter_minutes_in_hours(150) -> 2 (hours),30(minutes) because 2*60=120, 150-120=30 minutes
    """
    hours = math.floor(time_in_minutes / 60)
    minutes = time_in_minutes - hours * 60
    return hours, minutes


def time_validator_format_yyyy_mm_dd(time: str):
    """Time format must have the following format: YYYY-MM-DD"""
    if time is None:
        raise TypeError('Date cannot be None')
    if type(time) != str:
        raise TypeError('Time must be a string')
    if len(time) != 10:
        raise ValueError(
            'Date of activity must be in follow format YYYY-MM-DD and has a ten symbols'
        )
    i = 0
    while i < len(time):
        if i == 4 or i == 7:
            if time[i] != '-':
                raise ValueError('Between integers must be line, YYYY-MM-DD')
        else:
            if not time[i].isdigit():
                raise ValueError('Years must be integers')
        i += 1

    list_of_values = time.split('-')

    if list_of_values[0] < datetime.datetime.now().strftime("%Y") or list_of_values[
        0
    ] > datetime.datetime.now().strftime("%Y"):
        raise ValueError()
    if list_of_values[1] < '01' or list_of_values[1] > '12':
        raise ValueError('Month value should be between 1 and 12')
    if (
        list_of_values[1] == '01'
        or list_of_values[1] == '03'
        or list_of_values[1] == '05'
        or list_of_values[1] == '07'
        or list_of_values[1] == '08'
        or list_of_values[1] == '10'
        or list_of_values[1] == '12'
    ):
        if list_of_values[2] > '31' or list_of_values[2] < '01':
            raise ValueError()

    if (
        list_of_values[1] == '04'
        or list_of_values[1] == '06'
        or list_of_values[1] == '09'
        or list_of_values[1] == '11'
    ):
        if list_of_values[2] < '01' or list_of_values[2] > '30':
            raise ValueError()

    if list_of_values[1] == '02':
        if list_of_values[2] < '01' or list_of_values[2] > '28':
            raise ValueError()


def time_validator_format_hh_mm(time: str):
    """Time format must have the following format: HH-MM"""
    if time is None:
        raise TypeError('Time cannot be None')
    if type(time) != str:
        raise TypeError('Time must be a string')
    if len(time) != 5:
        raise ValueError('Time must have 5 symbols in the following format: HH-MM')
    i = 0
    while i < len(time):
        if i == 2:
            if time[i] != '-':
                raise ValueError('Between integers must be line, HH-MM')
        else:
            if not time[i].isdigit():
                raise ValueError('Years must be integers')
        i += 1


def calculate_duration_of_activity(start_time_of_activity, end_time_of_activity):
    """return time duration in minutes
    For example start_time = 17:30, end_time = 19:30
    Return 120 minutes
    start_time_of_activity and end_time_of_activity are both strings
    and should have the next format HH:MM"""
    time_validator_format_hh_mm(start_time_of_activity)
    time_validator_format_hh_mm(end_time_of_activity)
    start_time_of_activity = start_time_of_activity.split(':')
    end_time_of_activity = end_time_of_activity.split(':')
    for i in range(len(start_time_of_activity)):
        start_time_of_activity[i] = int(start_time_of_activity[i])
        end_time_of_activity[i] = int(end_time_of_activity[i])
    if end_time_of_activity[1] < start_time_of_activity[1]:
        end_time_of_activity[1] += 60
        end_time_of_activity[0] -= 1
    if end_time_of_activity[0] < start_time_of_activity[0]:
        end_time_of_activity[0] += 24
    result: list[int] = [0, 0]
    result[1] = math.fabs(end_time_of_activity[1] - start_time_of_activity[1])
    result[0] = end_time_of_activity[0] - start_time_of_activity[0]
    print(result)
    res_in_minutes = result[0] * 60 + result[1]
    return res_in_minutes
