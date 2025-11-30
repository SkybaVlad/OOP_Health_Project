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


class BodyMetricsContainer:
    """This class responsible for storing data about body metrics"""

    def __init__(self):
        self._dictionary = {}

    def add_body_metrics(self, metrics_type: BodyMetricsType, value, date):
        if self.__in_dict(date, metrics_type):
            self._dictionary[(date, metrics_type)].append(value)
        else:
            self._dictionary[(date, metrics_type)] = [value]

    def get_body_metrics(self) -> dict:
        return self._dictionary

    def __in_dict(self, date, metrics_type) -> bool:
        if (date, metrics_type) in self._dictionary.keys():
            return True
        return False


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
        metrics_type = self.filtration_criteria.metrics_type

        dictionary_of_activities = self.body_metrics_container.get_body_metrics()
        list_of_activities = []
        for date, metrics in dictionary_of_activities:
            if metrics_type == metrics:
                list_of_activities.append(
                    (date, dictionary_of_activities[(date, metrics_type)])
                )
        return list_of_activities

    def filter_by_specific_data(self):
        dictionary_of_activities = self.body_metrics_container.get_body_metrics()
        list_of_activities = []
        for data, metrics in dictionary_of_activities:
            if self.filtration_criteria.specific_data == data:
                list_of_activities.append(
                    (metrics, dictionary_of_activities[(data, metrics)])
                )
        return list_of_activities

    def filter_by_greater_value(self):
        dictionary_of_activities = self.body_metrics_container.get_body_metrics()
        list_of_activities = []
        for date, metrics_type in dictionary_of_activities:
            if self.filtration_criteria.metrics_type == metrics_type:
                for weight_value in dictionary_of_activities[(date, metrics_type)]:
                    if weight_value > self.filtration_criteria.greater_value:
                        list_of_activities.append(
                            (date, dictionary_of_activities[(date, metrics_type)])
                        )
        return list_of_activities

    def filter_by_less_value(self):
        dictionary_of_activities = self.body_metrics_container.get_body_metrics()
        list_of_activities = []
        for date, metrics_type in dictionary_of_activities:
            if self.filtration_criteria.metrics_type == metrics_type:
                for weight_value in dictionary_of_activities[(date, metrics_type)]:
                    if weight_value < self.filtration_criteria.lesser_value:
                        list_of_activities.append(
                            (date, dictionary_of_activities[(date, metrics_type)])
                        )
        return list_of_activities


def time_compare(start_time: str, end_time: str):
    pass


container = BodyMetricsContainer()
container.add_body_metrics(BodyMetricsType.body_mass_index_metrics, 100, '30.11.2025')
container.add_body_metrics(BodyMetricsType.weight, 90, '21.10.2025')
container.add_body_metrics(BodyMetricsType.weight, 100, '20.10.2025')
container.add_body_metrics(BodyMetricsType.weight, 91, '21.10.2025')
container.add_body_metrics(BodyMetricsType.weight, 105, '23.10.2025')
container.add_body_metrics(BodyMetricsType.weight, 108, '28.10.2025')
container.add_body_metrics(BodyMetricsType.body_mass_index_metrics, 91, '21.10.2025')
print(container.get_body_metrics())

filtrationCriteriaObject1 = FiltrationCriteria()
filtrationCriteriaObject1.set_greater_value(100)
filtrationCriteriaObject1.set_metrics_type(BodyMetricsType.weight)

filtrationBodyMetricsObject = FiltrationBodyMetrics()
filtrationBodyMetricsObject.set_body_metrics_container(container)
filtrationBodyMetricsObject.set_filtration_criteria(filtrationCriteriaObject1)

print(filtrationBodyMetricsObject.filter_by_greater_value())

filtrationCriteriaObject2 = FiltrationCriteria()
filtrationCriteriaObject2.set_lesser_value(100)
filtrationCriteriaObject2.set_metrics_type(BodyMetricsType.weight)
filtrationBodyMetricsObject.set_filtration_criteria(filtrationCriteriaObject2)

print(filtrationBodyMetricsObject.filter_by_less_value())

filtrationCriteriaObject3 = FiltrationCriteria()
filtrationCriteriaObject3.set_metrics_type(BodyMetricsType.body_mass_index_metrics)
filtrationBodyMetricsObject.set_filtration_criteria(filtrationCriteriaObject3)

print(filtrationBodyMetricsObject.filter_by_type())

filtrationCriteriaObject4 = FiltrationCriteria()
filtrationCriteriaObject4.set_specific_data('21.10.2025')
filtrationBodyMetricsObject.set_filtration_criteria(filtrationCriteriaObject4)
print(filtrationBodyMetricsObject.filter_by_specific_data())
