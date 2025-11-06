import math
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
        activity_name: ActivityType,
        burned_calories,
        # YYYY-MM-DDTHH:MM:SS
        start_time_of_activity,  # if str need edit method that uses this field for math calculation
        end_time_of_activity,
    ):
        self._activity_name = activity_name
        self._burned_calories = burned_calories
        self._start_time_of_activity = start_time_of_activity  #
        self._end_time_of_activity = end_time_of_activity

    def calculate_activity_duration_in_minutes(self):
        return abs(self._start_time_of_activity - self._end_time_of_activity)

    def get_name_of_specific_activity(self):
        return self._activity_name

    def get_burned_calories(self):
        return self._burned_calories

    def get_start_time_of_specific_activity(self):
        return self._start_time_of_activity

    def get_end_time_of_specific_activity(self):
        return self._end_time_of_activity

    def _time_converter_in_minutes_(self):
        start_time_of_activity = self._start_time_of_activity.split()
        end_time_of_activity = self._end_time_of_activity.split()
        pass


