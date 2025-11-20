import enum


class ActivityType(enum.Enum):
    Running = 'Running'
    Walking = 'Walking'
    Cycling = 'Cycling'
    Swimming = 'Swimming'
    Yoga = 'Yoga'
    StrengthTraining = 'Strength Training'
    Hiking = 'Hiking'
    Dancing = 'Dancing'
    Football = 'Football'
    Basketball = 'Basketball'
    Tennis = 'Tennis'
    Volleyball = 'Volleyball'
    Skiing = 'Skiing'
    Snowboarding = 'Snowboarding'
    Skating = 'Skating'
    Rowing = 'Rowing'
    Boxing = 'Boxing'
    JumpRope = 'Jump Rope'
    Stretching = 'Stretching'
    Other = 'Other'


class SpecificActivityType:

    def __init__(
        self,
        activity_name: str,
        burned_calories: float,
        # YYYY-MM-DD -> 2025-11-20
        start_time_of_activity: str,
        end_time_of_activity: str,
    ):
        self._activity_name = activity_name
        self._burned_calories = burned_calories
        self.time_manager = TimeManager(start_time_of_activity, end_time_of_activity)

    def get_name_of_specific_activity(self):
        return self._activity_name

    def get_burned_calories(self):
        return self._burned_calories

    def calculate_activity_duration_in_minutes(self):
        return self.time_manager.calculate_activity_duration_in_minutes()

    def get_start_time_of_specific_activity(self):
        return self.time_manager.start_time_of_activity

    def get_end_time_of_specific_activity(self):
        return self.time_manager.end_time_of_activity


class TimeManager:
    def __init__(self, start_time_of_activity, end_time_of_activity):
        self.start_time_of_activity = start_time_of_activity
        self.end_time_of_activity = end_time_of_activity

    def calculate_activity_duration_in_minutes(self):
        year = []
        month = []
        day = []
        i = 0
        if not isinstance(self.start_time_of_activity, str):
            while i < len(self.end_time_of_activity):
                if i < 4:
                    if self.start_time_of_activity[i].isdigit():
                        year.append(self.start_time_of_activity[i])

        return abs(self.start_time_of_activity - self.end_time_of_activity)

    def _time_converter_in_minutes_(self):
        start_time_of_activity = self.start_time_of_activity.split()
        end_time_of_activity = self.end_time_of_activity.split()
        pass


def time_validator(start_time: str, end_time: str):
    """Time format must have the following format: YYYY-MM-DD"""
    if start_time is None:
        raise TypeError('Start time cannot be None')
    if end_time is None:
        raise TypeError('End time cannot be None')
    if type(start_time) != str or type(end_time) != str:
        raise TypeError('Time must be a string')
    if len(start_time) != 10 or len(end_time) != 10:
        raise ValueError('Time format must have the following format: YYYY-MM-DD')
    i = 0
    while i < len(start_time):
        if i == 4 or i == 7:
            if start_time[i] != '-' or end_time[i] != '-':
                raise ValueError('Between integers must be line, YYYY-MM-DD')
        else:
            if not start_time[i].isdigit() or not end_time[i].isdigit():
                raise ValueError('Years must be integers')
        i += 1

        # need validate year value month value day value like day < 30 month < 12
