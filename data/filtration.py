from data.body_metrics_container import BodyMetricsContainer
from data.activity_container import ActivityContainer
from services.time_logic import time_in_period


class BodyMetricsCriteria:
    """This class responsible for any type of body_metrics criteria"""
    def __init__(self):
        self.metrics_type = None
        self.specific_data = None
        self.start_data = None
        self.end_data = None
        self.greater_value = None
        self.lesser_value = None

    def set_metrics_type(self, metrics_type):
        self.metrics_type = metrics_type

    def set_specific_data(self, specific_data):
        self.specific_data = specific_data

    def set_start_data(self, start_data):
        self.start_data = start_data

    def set_end_data(self, end_data):
        self.end_data = end_data

    def set_greater_value(self, greater_value):
        self.greater_value = greater_value

    def set_lesser_value(self, lesser_value):
        self.lesser_value = lesser_value


class FiltrationBodyMetrics:
    """This class responsible for any type of filtration data about body metrics"""

    def __init__(self):
        self.body_metrics_container = None
        self.body_metrics_filtration_criteria = None

    def set_body_metrics_container(self, body_metrics_container: BodyMetricsContainer):
        self.body_metrics_container = body_metrics_container

    def set_filtration_criteria(self, body_metrics_filtration_criteria: BodyMetricsCriteria):
        self.body_metrics_filtration_criteria = body_metrics_filtration_criteria

    def filter_by_type(
        self,
    ):
        dictionary_of_activities = self.body_metrics_container.get_body_metrics()
        list_of_activities = [
            (
                date,
                dictionary_of_activities[(date, self.body_metrics_filtration_criteria.metrics_type)],
            )
            for date, metrics in dictionary_of_activities
            if self.body_metrics_filtration_criteria.metrics_type == metrics
        ]
        return list_of_activities

    def filter_by_specific_data(self):
        dictionary_of_activities = self.body_metrics_container.get_body_metrics()
        list_of_activities = [
            (metrics, dictionary_of_activities[(data, metrics)])
            for data, metrics in dictionary_of_activities
            if self.body_metrics_filtration_criteria.specific_data == data
        ]
        return list_of_activities

    def filter_by_period(self):
        dictionary_of_activities = self.body_metrics_container.get_body_metrics()
        list_of_activities = [
            (metrics, dictionary_of_activities[(data, metrics)])
            for data, metrics in dictionary_of_activities
            if time_in_period(
                self.body_metrics_filtration_criteria.start_data,
                self.body_metrics_filtration_criteria.end_data,
                data,
            )
        ]
        return list_of_activities

    def filter_by_greater_value(self):
        dictionary_of_activities = self.body_metrics_container.get_body_metrics()
        list_of_activities = []
        for date, metrics_type in dictionary_of_activities:
            for value in dictionary_of_activities[(date, metrics_type)]:
                if value > self.body_metrics_filtration_criteria.greater_value:
                    list_of_activities.append(
                        (
                            date,
                            metrics_type,
                            dictionary_of_activities[(date, metrics_type)],
                        )
                    )
        return list_of_activities

    def filter_by_less_value(self):
        dictionary_of_activities = self.body_metrics_container.get_body_metrics()
        list_of_activities = []
        for date, metrics_type in dictionary_of_activities:
            for value in dictionary_of_activities[(date, metrics_type)]:
                if value < self.body_metrics_filtration_criteria.lesser_value:
                    list_of_activities.append(
                        (
                            date,
                            metrics_type,
                            dictionary_of_activities[(date, metrics_type)],
                        )
                    )
        return list_of_activities


class ActivityCriteria:
    """This class responsible for any type of activity criteria"""
    def __init__(self):
        self.activity_type = None
        self.specific_data = None
        self.start_data = None
        self.end_data = None
        self.greater_value = None
        self.lesser_value = None

    def set_activity_type(self, activity_type):
        self.activity_type = activity_type

    def set_specific_data(self, specific_data):
        self.specific_data = specific_data

    def set_start_data(self, start_data):
        self.start_data = start_data

    def set_end_data(self, end_data):
        self.end_data = end_data

    def set_greater_value(self, greater_value):
        self.greater_value = greater_value

    def set_lesser_value(self, lesser_value):
        self.lesser_value = lesser_value


class FiltrationActivity:
    """This class responsible for any type of filtration data about activity"""

    def __init__(self):
        self.activity_container = None
        self.filtration_activity_criteria = None

    def set_activity_container(self, activity_container: ActivityContainer) -> None:
        self.activity_container = activity_container

    def set_filtration_criteria(self, filtration_criteria: ActivityCriteria) -> None:
        self.filtration_activity_criteria = filtration_criteria

    def filter_by_type(
        self,
    ) -> list:
        dictionary_of_activities = self.activity_container.get_all_activities()
        list_of_activities = [(data, dictionary_of_activities[data] for data in dictionary_of_activities if dictionary_of_activities[data].activity_name == self.filtration_activity_criteria.activity_name)]
        return list_of_activities

    def filter_by_specific_data(self) -> list:
        dictionary_of_activities = self.activity_container.get_all_activities()
        list_of_activities = [specific_activity_object for data, specific_activity_object in dictionary_of_activities.items() if data == self.filtration_activity_criteria.specific_data]
        return list_of_activities

    def filter_by_period(self) -> list:
        dictionary_of_activities = self.activity_container.get_all_activities()
        list_of_activities = [specific_activity_object for data, specific_activity_object in dictionary_of_activities.items() if time_in_period(self.filtration_activity_criteria.start_data, self.filtration_activity_criteria.end_data, data)]
        return list_of_activities

    def filter_by_greater_value_of_burned_calories(self) -> list:
        dictionary_of_activities = self.activity_container.get_all_activities()
        list_of_activities = [(data, specific_activity_object) for data, specific_activity_object in dictionary_of_activities.items() if specific_activity_object.burned_calories > self.filtration_activity_criteria.greater_value]
        return list_of_activities

    def filter_by_less_value_of_burned_calories(self) -> list:
        dictionary_of_activities = self.activity_container.get_all_activities()
        list_of_activities = [(data, specific_activity_object) for data, specific_activity_object in dictionary_of_activities.items() if specific_activity_object.burned_calories < self.filtration_activity_criteria.greater_value]
        return list_of_activities

