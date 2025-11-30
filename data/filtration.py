from data.body_metrics_container import BodyMetricsContainer
from data.activity_container import ActivityContainer


class FiltrationCriteria:
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
        self.filtration_criteria = None

    def set_body_metrics_container(self, body_metrics_container: BodyMetricsContainer):
        self.body_metrics_container = body_metrics_container

    def set_filtration_criteria(self, filtration_criteria: FiltrationCriteria):
        self.filtration_criteria = filtration_criteria

    def filter_by_type(
        self,
    ):
        dictionary_of_activities = self.body_metrics_container.get_body_metrics()
        list_of_activities = [
            (
                date,
                dictionary_of_activities[(date, self.filtration_criteria.metrics_type)],
            )
            for date, metrics in dictionary_of_activities
            if self.filtration_criteria.metrics_type == metrics
        ]
        return list_of_activities

    def filter_by_specific_data(self):
        dictionary_of_activities = self.body_metrics_container.get_body_metrics()
        list_of_activities = [
            (metrics, dictionary_of_activities[(data, metrics)])
            for data, metrics in dictionary_of_activities
            if self.filtration_criteria.specific_data == data
        ]
        return list_of_activities

    def filter_by_period(self):
        dictionary_of_activities = self.body_metrics_container.get_body_metrics()
        list_of_activities = [
            (metrics, dictionary_of_activities[(data, metrics)])
            for data, metrics in dictionary_of_activities
            if time_compare(
                self.filtration_criteria.start_data,
                self.filtration_criteria.end_data,
                data,
            )
        ]
        return list_of_activities

    def filter_by_greater_value(self):
        dictionary_of_activities = self.body_metrics_container.get_body_metrics()
        list_of_activities = []
        for date, metrics_type in dictionary_of_activities:
            for value in dictionary_of_activities[(date, metrics_type)]:
                if value > self.filtration_criteria.greater_value:
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
                if value < self.filtration_criteria.lesser_value:
                    list_of_activities.append(
                        (
                            date,
                            metrics_type,
                            dictionary_of_activities[(date, metrics_type)],
                        )
                    )
        return list_of_activities


class ActivityCriteria:
    def __init__(self):
        self.activity_type = None
        self.specific_data = None
        self.start_data = None
        self.end_data = None
        self.greater_value = None
        self.lesser_value = None

    def set_metrics_type(self, activity_type):
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

    def set_activity_container(self, activity_container: ActivityContainer):
        self.activity_container = activity_container

    def set_filtration_criteria(self, filtration_criteria: ActivityCriteria):
        self.filtration_activity_criteria = filtration_criteria

    def filter_by_type(
        self,
    ):
        pass

    def filter_by_specific_data(self):
        pass

    def filter_by_period(self):
        pass

    def filter_by_greater_value(self):
        pass

    def filter_by_less_value(self):
        pass


def time_compare(start_time: str, end_time: str, current_time: str):
    pass
