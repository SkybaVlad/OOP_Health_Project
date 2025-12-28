import datetime
from datetime import date

"""This module responsible for validation data for time input"""


def is_year_value_in_limits(year: str) -> bool:
    """This function checks if the year value is between current years value - 1 and current years value
    For current_year = 2027 so example check_time_limits_for_years_value(year=2027) -> true and
    example check_time_limits_for_years_value(year=2026) -> true but if year=2025 or 2028 functions should return false
    limits is [curr_year - 1 , curr_year]"""
    current_year_minus_one = str(int(datetime.datetime.now().strftime("%Y")) - 1)
    if year < current_year_minus_one or year > datetime.datetime.now().strftime("%Y"):
        return False
    return True


def is_day_number_in_limits_for_month_where_count_of_days_31(
    month_number: str, number_of_day: str
) -> bool:
    """This function checks if the number of day between 1 and 31 for specific month"""
    if (
        month_number == '01'
        or month_number == '03'
        or month_number == '05'
        or month_number == '07'
        or month_number == '08'
        or month_number == '10'
        or month_number == '12'
    ):
        if number_of_day > '31' or number_of_day < '01':
            return False
    return True


def is_day_number_in_limits_for_month_where_count_of_days_30(
    month_number: str, number_of_day: str
) -> bool:
    if (
        month_number == '04'
        or month_number == '06'
        or month_number == '09'
        or month_number == '11'
    ):
        if number_of_day < '01' or number_of_day > '30':
            return False
    return True


def time_validator_format_yyyy_mm_dd(time: str):
    """Time format must have the following format: YYYY-MM-DD"""
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
    if not is_year_value_in_limits(list_of_values[0]):
        raise ValueError(
            f"Years value should be between {str(int(datetime.datetime.now().strftime("%Y")) - 1)} and {datetime.datetime.now().strftime("%Y")}"
        )

    if list_of_values[1] < '01' or list_of_values[1] > '12':
        raise ValueError('Month number should be between 1 and 12')

    # condition for month with max day count is 31
    if not is_day_number_in_limits_for_month_where_count_of_days_31(
        list_of_values[1], list_of_values[2]
    ):
        raise ValueError("Day must be between 1 and 31")

    # condition for month with max day count is 30
    if not is_day_number_in_limits_for_month_where_count_of_days_30(
        list_of_values[1], list_of_values[2]
    ):
        if list_of_values[2] < '01' or list_of_values[2] > '30':
            raise ValueError("Day must be between 1 and 30")

    # condition for month with max day count is 28
    if list_of_values[1] == '02':
        if list_of_values[2] < '01' or list_of_values[2] > '28':
            raise ValueError("Day must be between 1 and 28")


def time_validator_format_hh_mm(time: str):
    """Time format must have the following format: HH:MM"""
    if type(time) != str:
        raise TypeError('Time must be a string')
    if len(time) != 5:
        raise ValueError('Time must have 5 symbols in the following format: HH:MM')
    i = 0
    while i < len(time):
        if i == 2:
            if time[i] != ':':
                raise ValueError('Between integers must be two dots like HH:MM')
        else:
            if not time[i].isdigit():
                raise ValueError('Years must be integers')
        i += 1

    list_of_values = time.split(':')
    hours = int(list_of_values[0])
    minutes = int(list_of_values[1])

    if hours < 0 or hours > 23:
        raise ValueError('Hours must be between 0 and 23')
    if minutes < 0 or minutes > 59:
        raise ValueError('Minutes must be between 0 and 59')
