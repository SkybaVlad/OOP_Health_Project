import enum


class BodyMetricsType(enum.Enum):
    body_mass_index_metrics = 'bmi'
    basal_metabolic_rate = 'bmr'
    lean_body_mass = 'lbm'
    fat_mass = 'fm'
    weight = 'weight'
    height = 'height'
    fat_percentage = 'fp'
    percentage_of_water_level = 'fwl'


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

"""BodyMetricsContainer class provide a basic operation on data like add, get and stored
data in dictionary. The data form storage (date,metrics_type):value"""


class BodyMetricsContainer:
    def __init__(self):
        self._dictionary = {}
        self.filtration = FiltrationBodyMetrics()
        self.filtration_criteria = None

    def add_body_metrics(self, metrics_type: str, value, date):
        if self.__in_dict(date, metrics_type):
            self._dictionary[(date, metrics_type)].append(value)
        else:
            self._dictionary[(date, metrics_type)] = [value]

    def get_body_metrics(self) -> dict:
        return self._dictionary

    def get_specific_body_metrics(self, metrics_type: str) -> dict:
        return self.filtration.filter_by_type(metrics_type)

    def set_criteria(self, filtration_criteria: FiltrationCriteria):
        self.filtration_criteria = filtration_criteria

    def __in_dict(self, date, metrics_type) -> bool:
        if (date, metrics_type) in self._dictionary.keys():
            return True
        return False


class FiltrationBodyMetrics:
    def filter_by_type(
        self,
    ):
        metrics_type = criteria.get_metrics_type()

        dictionary_of_activities = body_metrics_container.get_body_metrics()
        list_of_activities = []
        for date, metrics in dictionary_of_activities:
            if metrics_type == metrics:
                list_of_activities.append(
                    (date, dictionary_of_activities[(date, metrics_type)])
                )
        return list_of_activities

    def filter_by_greater_value(self):
        dictionary_of_activities = body_metrics_container.get_body_metrics()
        list_of_activities = []
        for date, metrics_type in dictionary_of_activities:
            if (
                dictionary_of_activities[(date, criteria.get_metrics_type())]
                > criteria.get_condition_value()
            ):
                list_of_activities.append(
                    (date, dictionary_of_activities[(date, metrics_type)])
                )
        return list_of_activities

    def filter_by_less_value(self):
        dictionary_of_activities = body_metrics_container.get_body_metrics()
        list_of_activities = []
        for date, metrics_type in dictionary_of_activities:
            if (
                dictionary_of_activities[(date, criteria.get_metrics_type())]
                < criteria.get_condition_value()
            ):
                list_of_activities.append(
                    (date, dictionary_of_activities[(date, metrics_type)])
                )
        return list_of_activities
