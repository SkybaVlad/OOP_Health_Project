import math


def time_in_period(start_time: str, end_time: str, current_time: str):
    """This function compare current time with start time and end time. Return True if current time located
    in period between start and end time and Return False otherwise. The time vars have the next format YYYY-MM-DD
    """
    start_time = start_time.split("-")
    end_time = end_time.split("-")
    current_time = current_time.split("-")

    if current_time[0] < start_time[0] or current_time[0] > end_time[0]:
        return False

    if current_time[1] < start_time[1] or current_time[1] > end_time[1]:
        return False
    else:
        if current_time[1] == start_time[1]:
            if current_time[2] < start_time[2]:
                return False
        elif current_time[1] == end_time[1]:
            if current_time[2] > end_time[2]:
                return False
    return True

    if current_time[2] < start_time[2] or current_time[2] > end_time[2]:
        return False

    return True


def time_validator(date_of_activity: str, start_time: str, end_time: str):
    """Time format must have the following format: YYYY-MM-DD"""
    if date_of_activity is None:
        raise TypeError('Date cannot be None')
    if start_time is None:
        raise TypeError('Start time cannot be None')
    if end_time is None:
        raise TypeError('End time cannot be None')
    if (
        type(date_of_activity) != str
        or type(start_time) != str
        or type(end_time) != str
    ):
        raise TypeError('Time must be a string')
    if len(date_of_activity) != 10:
        raise ValueError('Date of activity must be in follow format YYYY-MM-DD')
    if len(start_time) != 5 or len(end_time) != 5:
        raise ValueError('Time format must have the following format: HH:MM')
    i = 0
    while i < len(date_of_activity):
        if i == 4 or i == 7:
            if date_of_activity[i] != '-':
                raise ValueError('Between integers must be line, YYYY-MM-DD')
        else:
            if not date_of_activity[i].isdigit():
                raise ValueError('Years must be integers')
        i += 1
    i = 0
    while i < len(start_time):
        if i == 2:
            if start_time[i] != ':' or end_time[i] != ':':
                raise ValueError('Between integers must be line, HH:MM')
        else:
            if not start_time[i].isdigit() or not end_time[i].isdigit():
                raise ValueError('Years must be integers')
        i += 1

        # need validate year value month value day value like day < 30 month < 12


class TimeActivityManager:
    def __init__(self, date_of_activity, start_time_of_activity, end_time_of_activity):
        self._date_of_activity = date_of_activity
        self.start_time_of_activity = start_time_of_activity
        self.end_time_of_activity = end_time_of_activity

    def calculate_activity_duration_in_minutes(self):
        """return time duration in minutes
        For example start_time = 17:30, end_time = 19:30
        Return 120 minutes"""

        return self._time_converter_in_minutes_()

    def _time_converter_in_minutes_(self):
        start_time_of_activity = self.start_time_of_activity.split(':')
        end_time_of_activity = self.end_time_of_activity.split(':')
        for i in range(len(start_time_of_activity)):
            start_time_of_activity[i] = int(start_time_of_activity[i])
            end_time_of_activity[i] = int(end_time_of_activity[i])
        if end_time_of_activity[1] < start_time_of_activity[1]:
            end_time_of_activity[1] += 60
            end_time_of_activity[0] -= 1
        if end_time_of_activity[0] < start_time_of_activity[0]:
            end_time_of_activity[0] += 24
        result = [0, 0]
        result[1] = math.fabs(end_time_of_activity[1] - start_time_of_activity[1])
        result[0] = end_time_of_activity[0] - start_time_of_activity[0]
        print(result)
        res_in_minutes = result[0] * 60 + result[1]
        return res_in_minutes
