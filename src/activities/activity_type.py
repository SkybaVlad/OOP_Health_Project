import math


class SpecificActivityType:

    def __init__(
        self,
        activity_name: str,
        intensity_of_activity: int,
        start_time_of_activity,  # if str need edit method that uses this field for math calculation
        end_time_of_activity,
    ):
        self.activity_name = activity_name
        self.intensity_of_activity = intensity_of_activity  # 1 to 10
        self.start_time_of_activity = start_time_of_activity
        self.end_time_of_activity = end_time_of_activity

    def calculate_count_of_burned_calories(self):
        return (
            5
            * pow(self.intensity_of_activity, 1.2)
            * math.sqrt(self.calculate_duration_of_specific_activity())
            + 0.3
            * self.intensity_of_activity
            * self.calculate_duration_of_specific_activity()
        )

    def calculate_duration_of_specific_activity(self):
        return abs(self.start_time_of_activity - self.end_time_of_activity)

    def get_intensity_of_specific_activity(self):
        return self.intensity_of_activity

    def get_name_of_specific_activity(self):
        return self.activity_name

    def get_start_time_of_specific_activity(self):
        return self.start_time_of_activity

    def get_end_time_of_specific_activity(self):
        return self.end_time_of_activity
