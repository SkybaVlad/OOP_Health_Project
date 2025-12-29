import math
from services.validation_user_input.time_validator import (
    time_validator_format_yyyy_mm_dd,
    time_validator_format_hh_mm,
    is_source_time_less_than_target_time,
    is_month_where_max_day_count_is_28,
    is_month_where_max_day_count_is_30,
    is_month_where_max_day_count_is_31,
)


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


def calculate_duration_of_activity(start_time_of_activity, end_time_of_activity) -> int:
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
    res_in_minutes = result[0] * 60 + result[1]
    return res_in_minutes


def plus_one_to_time(time: str) -> str:
    """this function add 1 to time. For example time = 01 -> 02,
    time = 09 -> 10, time = 9999 -> 10000."""

    if len(time) == 2:
        if time == "09":
            return "10"
        if time == "19":
            return "20"
        if time == "29":
            return "30"
        else:
            tmp = ""
            for ch in time:
                tmp += ch  # -> tmp = "n n "
                tmp += " "
            array = tmp.rstrip(" ").split(" ")  # -> array = ["n","n"]
            array_int = []
            for i in array:
                array_int.append(int(i))
            # array_int = [n,n]
            array_int[1] += 1
            # array_int = [n,n+1]
            res = []
            for i in array_int:
                res.append(str(i))
            # res = ["n","n+1"]
            return "".join(res)  # -> "nn+1"
    else:
        tmp = ""
        for ch in time:
            tmp += ch
            tmp += " "
        array = tmp.rstrip(" ").split(" ")
        # array -> ["Y","Y","Y","Y"]
        carry = False
        rev_array = array[::-1]
        for index, elem in enumerate(rev_array):
            rev_array[index] = int(rev_array[index])

        for index, elem in enumerate(rev_array):
            if carry:
                if index == len(array) - 1:
                    rev_array[index] = 10
                    for indx, i in enumerate(rev_array):
                        rev_array[indx] = str(rev_array[indx])
                    return "".join(rev_array[::-1])
                else:
                    rev_array[index] += 1
                    carry = False
            else:
                rev_array[index] += 1
            if rev_array[index] == 10:
                rev_array[index] = 0
                carry = True
            else:
                for indx, i in enumerate(rev_array):
                    rev_array[indx] = str(rev_array[indx])
                return "".join(rev_array[::-1])


def increase_date_by_one_day(date: str) -> str:
    # date -> YYYY-MM-DD
    tmp = date.split("-")  # -> ["YYYY","MM","DD"]

    if is_month_where_max_day_count_is_31(tmp[1]):
        if tmp[2] == "31":
            if tmp[1] == "12":
                tmp[0] = plus_one_to_time(tmp[0])  # year
                tmp[1] = "01"
                tmp[2] = "01"
            else:
                tmp[1] = plus_one_to_time(tmp[1])  # month
                tmp[2] = '01'
        else:
            tmp[2] = plus_one_to_time(tmp[2])  # day
    elif is_month_where_max_day_count_is_30(tmp[1]):
        if tmp[2] == "30":
            if tmp[1] == "12":
                tmp[0] = plus_one_to_time(tmp[0])
                tmp[1] = '01'
                tmp[2] = '01'
            else:
                tmp[1] = plus_one_to_time(tmp[1])
                tmp[2] = '01'
        else:
            tmp[2] = plus_one_to_time(tmp[2])
    elif is_month_where_max_day_count_is_28(tmp[1]):
        if tmp[2] == "28":
            if tmp[1] == "12":
                tmp[0] = plus_one_to_time(tmp[0])
                tmp[1] = '01'
                tmp[2] = '01'
            else:
                tmp[1] = plus_one_to_time(tmp[1])
                tmp[2] = '01'
        else:
            tmp[2] = plus_one_to_time(tmp[2])
    return "-".join(tmp)


def get_list_of_all_dates_between_start_and_end(start_time, end_time) -> list[str]:
    lst = []
    while is_source_time_less_than_target_time(start_time, end_time):
        lst.append(start_time)
        start_time = increase_date_by_one_day(start_time)
    return lst
