import math
from src.activities.activity_container import ActivityContainer


class Activity:

    def __init__(self):
        self.specific_activity_type_object = None
        self.manager_of_activities = ActivityContainer() # maybe storage objects instead a activity_name

    def count_of_burned_calories(self):
        self.specific_activity_type_object.calculate_count_of_burned_calories()

    def create_specific_activity_type_object(self, activity_name, intensity, start_time, end_time, data_of_activity):
        self.specific_activity_type_object = SpecificActivityType(activity_name, intensity, start_time, end_time)
        self.manager_of_activities.add_activity(self.specific_activity_type_object, data_of_activity)

    def calculate_duration_of_activity(self):
        self.specific_activity_type_object.calculate_duration_of_activity()

    def get_history_of_all_activities(self):
        self.manager_of_activities.get_all_activities()

    def get_activities_in_specific_date(self, data_of_activity):
        self.manager_of_activities.get_activity_in_specific_date(data_of_activity)


class SpecificActivityType:

    def __init__(self, activity_name, intensity_of_activity, start_time_of_activity, end_time_of_activity):
        self.activity_name = activity_name
        self.intensity_of_activity = intensity_of_activity  # 1 to 10
        self.start_time_of_activity = start_time_of_activity
        self.end_time_of_activity = end_time_of_activity

    def calculate_count_of_burned_calories(self):
        return (
            5
            * pow(self.intensity_of_activity, 1.2)
            * math.sqrt(self.calculate_duration_of_activity())
            + 0.3 * self.intensity_of_activity * self.calculate_duration_of_activity()
        )

    def calculate_duration_of_activity(self):
        return abs(self.start_time_of_activity - self.end_time_of_activity)
