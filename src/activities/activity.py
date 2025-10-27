from src.activities.activity_container import ActivityContainer
from src.activities.activity_type import SpecificActivityType


class Activity:

    def __init__(self):
        self.specific_activity_type_object = None
        self.container_of_activities = ActivityContainer()

    def count_of_burned_on_specific_activity(self):
        self.specific_activity_type_object.calculate_count_of_burned_calories()

    def create_specific_activity_type_object(
        self, activity_name, intensity, start_time, end_time, data_of_activity
    ):
        self.specific_activity_type_object = SpecificActivityType(
            activity_name, intensity, start_time, end_time
        )
        self.container_of_activities.add_activity(
            self.specific_activity_type_object, data_of_activity
        )

    # maybe add get_total_burned_calories()

    # maybe add get_statistics_in_some_period(start_data,end_data)

    def calculate_duration_of_specific_activity(self):
        return (
            self.specific_activity_type_object.calculate_duration_of_specific_activity()
        )

    def get_history_of_all_activities(self):
        self.container_of_activities.get_all_activities()

    def get_activities_in_specific_date(self, data_of_activity):
        return self.container_of_activities.get_activity_in_specific_date(
            data_of_activity
        )
