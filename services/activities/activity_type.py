from services.validation_user_input.activity_validation import (
    validate_activity_name,
    validate_activity_category,
    validate_burned_calories,
)
from services.time_logic import calculate_duration_of_activity
from services.validation_user_input.time_validator import time_validator_format_hh_mm


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
        burned_calories: int,
        start_time_of_activity: str,
        end_time_of_activity: str,
    ):
        try:
            validate_activity_category(activity_category)
            validate_activity_name(activity_name)
            validate_burned_calories(burned_calories)
            time_validator_format_hh_mm(start_time_of_activity)
            time_validator_format_hh_mm(end_time_of_activity)
        except TypeError as e:
            pass
        except ValueError as e:
            pass

        self._activity_category = activity_category
        self._activity_name = activity_name
        self._burned_calories = burned_calories
        self._start_time_of_activity = start_time_of_activity
        self._end_time_of_activity = end_time_of_activity

    def get_activity_category(self) -> str:
        return self._activity_category

    def get_name_of_specific_activity(self) -> str:
        return self._activity_name

    def get_burned_calories(self) -> float:
        return self._burned_calories

    def calculate_activity_duration_in_minutes(self) -> float:
        return calculate_duration_of_activity(
            self._start_time_of_activity, self._end_time_of_activity
        )

    def get_start_time_of_specific_activity(self) -> str:
        return self._start_time_of_activity

    def get_end_time_of_specific_activity(self) -> str:
        return self._end_time_of_activity

    def __str__(self):
        return f"Specific Activity Type: {self._activity_category} - {self._activity_name}, with {self._burned_calories} calories burned and {self.calculate_activity_duration_in_minutes()} minutes duration of activity"

    def __repr__(self):
        return f"SpecificActivityType(activity_category={self._activity_category},activity_name={self._activity_name}, burned_calories={self._burned_calories}, start_time_of_activity={self._start_time_of_activity}, end_time_of_activity={self._end_time_of_activity})"
