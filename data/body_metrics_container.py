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


"""BodyMetricsContainer class provide a basic operation on data like add, get and stored
data in dictionary. The data form storage (date,metrics_type):value"""


class BodyMetricsContainer:
    def __init__(self):
        self._dictionary = {}

    def add_body_metrics(self, metrics_type: str, value, date):
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
