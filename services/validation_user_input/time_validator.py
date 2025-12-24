import datetime

"""This module responsible for validation data for time input"""


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
    current_year_minus_one = int(datetime.datetime.now().strftime("%Y"))
    current_year_minus_one = current_year_minus_one - 1
    current_year_minus_one = str(current_year_minus_one)
    if list_of_values[0] < current_year_minus_one or list_of_values[
        0
    ] > datetime.datetime.now().strftime("%Y"):
        raise ValueError(
            "Years value should be between current_year - 1 and current_year"
        )
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
            raise ValueError("Day must be between 1 and 31")

    if (
        list_of_values[1] == '04'
        or list_of_values[1] == '06'
        or list_of_values[1] == '09'
        or list_of_values[1] == '11'
    ):
        if list_of_values[2] < '01' or list_of_values[2] > '30':
            raise ValueError("Day must be between 1 and 30")

    if list_of_values[1] == '02':
        if list_of_values[2] < '01' or list_of_values[2] > '28':
            raise ValueError("Day must be between 1 and 28")


def time_validator_format_hh_mm(time: str):
    """Time format must have the following format: HH:MM"""
    if time is None:
        raise TypeError('Time cannot be None')
    if type(time) != str:
        raise TypeError('Time must be a string')
    if len(time) != 5:
        raise ValueError('Time must have 5 symbols in the following format: HH:MM')
    i = 0
    while i < len(time):
        if i == 2:
            if time[i] != ':':
                raise ValueError('Between integers must be line, HH:MM')
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
