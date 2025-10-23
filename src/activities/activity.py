import math


class Activity:
    def __init__(self):
        self.specific_activity_type_object = None
        # maybe add hashmap tp track history activity in specific day but need cover situation where more than
        # 2 activities in one day

    def count_of_burned_calories(self):
        self.specific_activity_type_object.calculate_count_of_burned_calories()

    def set_specific_activity_type_object(self, intensity, start_time, end_time):
        self.specific_activity_type_object = SpecificActivityType(
            intensity, start_time, end_time
        )

    def calculate_duration(self):
        self.specific_activity_type_object.calculate_duration_of_activity()


class SpecificActivityType:

    def __init__(
        self, intensity_of_activity, start_time_of_activity, end_time_of_activity
    ):
        self.intensity_of_activity = intensity_of_activity  # 1 to 10
        self.start_time_of_activity = start_time_of_activity
        self.end_time_of_activity = end_time_of_activity

    def calculate_count_of_burned_calories(
        self,
    ):  # using a unique formula that depend from intensity and time
        return (
            5
            * pow(self.intensity_of_activity, 1.2)
            * math.sqrt(self.calculate_duration_of_activity())
            + 0.3 * self.intensity_of_activity * self.calculate_duration_of_activity()
        )

    def calculate_duration_of_activity(self):
        return abs(
            self.start_time_of_activity - self.end_time_of_activity
        )  # using abs function to cover cases when end_time is next_day and start_time is this day
