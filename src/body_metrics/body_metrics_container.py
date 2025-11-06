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

    def get_history_of_specific_matrics(self, metrics_type: str) -> list:
        pass

    def _in_dict(self, date, metrics_type) -> bool:
        if (date, metrics_type) in self._dictionary.keys():
            return True
        return False


