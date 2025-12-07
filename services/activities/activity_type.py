import enum
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


class ActivityCategory(enum.Enum):
    Cardio = 'Cardio'
    Strength = 'Strength'
    Sport = 'Sport'


class SpecificActivityType:
    """This class describes the activity type. Class has a activity_category attribute that describes in ActivityCategory class,
    activity_name attribute that describes in ActivityType class,
    burned_calories attribute that describes amount of burned calories that user entered,
    date_of_activity attribute describes a date when user do the activity and has the next format YYYY-MM-DD,
    start_time_of_activity attribute describes a time when activity is started and has the next format HH:MM,
    end_time_of_activity attribute describes a time when activity is ended and has the next format HH:MM
    """

    def __init__(
        self,
        activity_category: str,
        activity_name: str,
        burned_calories: float,
        start_time_of_activity: str,
        end_time_of_activity: str,
    ):
        self._activity_category = activity_category
        self._activity_name = activity_name
        self._burned_calories = burned_calories
        self.time_manager = TimeActivityManager(
            start_time_of_activity, end_time_of_activity
        )

    def get_activity_category(self) -> str:
        return self._activity_category

    def get_name_of_specific_activity(self) -> str:
        return self._activity_name

    def get_burned_calories(self) -> float:
        return self._burned_calories

    def calculate_activity_duration_in_minutes(self) -> float:
        return self.time_manager.calculate_activity_duration_in_minutes()

    def get_start_time_of_specific_activity(self) -> str:
        return self.time_manager.start_time_of_activity

    def get_end_time_of_specific_activity(self) -> str:
        return self.time_manager.end_time_of_activity
