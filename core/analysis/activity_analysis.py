from core.activity.activity_type import SpecificActivityType


class ActivityAnalyzer:
    """This class provide the API that under hood analyze different activities
    metrics."""

    def __init__(self):
        self.start_time: str | None = None
        self.end_time: str | None = None
        self.list_of_activities: list[SpecificActivityType] | None = None

    def load_default_values_to_initialize(
        self,
        start_time: str,
        end_time: str,
        list_of_activities: list[SpecificActivityType],
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.list_of_activities = list_of_activities

    def set_period(self, start_time: str, end_time: str):
        self.start_time = start_time
        self.end_time = end_time

    def set_list_of_activities(self, list_of_activities=list[SpecificActivityType]):
        self.list_of_activities = list_of_activities

    def get_total_spend_on_activity(self) -> float:
        total_time = 0.0
        for activity in self.list_of_activities:
            total_time += activity.calculate_activity_duration_in_minutes()
        return total_time

    def get_total_burned_calories_with_activity(self):
        total_burned_calories = 0.0
        for activity in self.list_of_activities:
            total_burned_calories += activity.burned_calories
        return total_burned_calories

    def get_list_of_activities_names_that_exist_in_period(self) -> list[str]:
        lst_of_activities_names = []
        for activity in self.list_of_activities:
            lst_of_activities_names.append(activity.activity_name)
        return lst_of_activities_names

    def get_list_of_activities_categories_that_exist_in_period(self) -> list[str]:
        lst_of_activities_categories = []
        for activity in self.list_of_activities:
            lst_of_activities_categories.append(activity.activity_name)
        return lst_of_activities_categories

    def get_time_spend_on_activities_categories(self):
        dict_of_activities_categories = {}
        for activity in self.list_of_activities:
            if (
                dict_of_activities_categories.get(activity.activity_category, None)
                is None
            ):
                dict_of_activities_categories[activity.activity_category] = (
                    activity.calculate_activity_duration_in_minutes()
                )
            else:
                dict_of_activities_categories[
                    activity.activity_category
                ] += activity.calculate_activity_duration_in_minutes()
        return dict_of_activities_categories

    def get_most_popular_activity_category_and_time_spend_on_this_activity(self):
        pass

    def get_most_popular_activity_name_and_time_spend_on_this_category(self):
        pass
