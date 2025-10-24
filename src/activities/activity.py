import math
from src.activities.activity_container import ActivityContainer


class Activity:

    def __init__(self):
        self.specific_activity_type_object = None
        self.manager_of_activities = ActivityContainer()

    def count_of_burned_calories(self):
        self.specific_activity_type_object.calculate_count_of_burned_calories()

    def set_specific_activity_type_object(self, intensity, start_time, end_time):
        self.specific_activity_type_object = SpecificActivityType(
            intensity, start_time, end_time
        )
        # add new object to container class add_activity()

    def calculate_duration_of_activity(self):
        self.specific_activity_type_object.calculate_duration_of_activity()

    def get_history_of_all_activities(self):
        pass

    def get_activities_in_specific_date(self):
        pass


class SpecificActivityType:

    def __init__(
        self, intensity_of_activity, start_time_of_activity, end_time_of_activity
    ):
        self.intensity_of_activity = intensity_of_activity  # 1 to 10
        self.start_time_of_activity = start_time_of_activity
        self.end_time_of_activity = end_time_of_activity

    def calculate_count_of_burned_calories(
        self,
    ):
        return (
            5
            * pow(self.intensity_of_activity, 1.2)
            * math.sqrt(self.calculate_duration_of_activity())
            + 0.3 * self.intensity_of_activity * self.calculate_duration_of_activity()
        )

    def calculate_duration_of_activity(self):
        return abs(self.start_time_of_activity - self.end_time_of_activity)
