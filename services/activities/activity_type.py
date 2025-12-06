import enum
import math
from services.time_logic import TimeActivityManager


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
        date_of_activity: str,  # YYYY-MM-DD -> 2025-11-20
        start_time_of_activity: str,  # HH:MM -> 17:20
        end_time_of_activity: str,  # HH:MM -> 19:20
    ):
        self._activity_name = activity_name
        self._burned_calories = burned_calories
        self.time_manager = TimeActivityManager(
            date_of_activity, start_time_of_activity, end_time_of_activity
        )

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
