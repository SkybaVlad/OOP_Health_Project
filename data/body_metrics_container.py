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


class BodyMetricsContainer:
    def __init__(self):
        self._dictionary = {}

    def add_body_metrics(self, metrics_type: str, value, date):
        if self._in_dict(date, metrics_type):
            self._dictionary[(date, metrics_type)].append(value)
        else:
            self._dictionary[(date, metrics_type)] = [value]

    def get_metrics_in_specific_date(self, metrics_type: str, date) -> list:
        return self._dictionary[(date, metrics_type)]

    def get_history_of_specific_metrics(self, metrics_type_: str) -> list:
        # sorted_list = sorted(self._dictionary.items())
        # list_with_specific_metrics = []
        # for date, metrics_type in sorted_list:
        #     if metrics_type == metrics_type_:
        #         list_with_specific_metrics.append((date, metrics_type))
        # print(list_with_specific_metrics)
        # return list_with_specific_metrics

    def _in_dict(self, date, metrics_type) -> bool:
        if (date, metrics_type) in self._dictionary.keys():
            return True
        return False


obj = BodyMetricsContainer()
obj.add_body_metrics(BodyMetricsType.body_mass_index_metrics.value, 30, '02.05.2007')
obj.add_body_metrics(BodyMetricsType.body_mass_index_metrics.value, 40, '04.05.2007')
obj.add_body_metrics(BodyMetricsType.body_mass_index_metrics.value, 35, '03.05.2007')
obj.add_body_metrics(BodyMetricsType.body_mass_index_metrics.value, 34, '03.05.2007')
obj.add_body_metrics(BodyMetricsType.body_mass_index_metrics.value, 45, '10.05.2007')
obj.add_body_metrics(BodyMetricsType.lean_body_mass.value, 30, '02.05.2007')
obj.add_body_metrics(BodyMetricsType.lean_body_mass.value, 40, '04.05.2007')
obj.add_body_metrics(BodyMetricsType.lean_body_mass.value, 35, '03.05.2007')
obj.add_body_metrics(BodyMetricsType.fat_percentage.value, 34, '05.05.2007')
obj.add_body_metrics(BodyMetricsType.fat_percentage.value, 45, '10.05.2007')

print(
    obj.get_history_of_specific_matrics(BodyMetricsType.body_mass_index_metrics.value)
)
