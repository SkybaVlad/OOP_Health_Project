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
        self.dictionary = {}

    def add_body_mass_index_metrics(self, value, date):
        if self._in_dict(date, BodyMetricsType.body_mass_index_metrics):
            self.dictionary[(date, BodyMetricsType.body_mass_index_metrics.value)].append(value)
        else:
            self.dictionary[(date, BodyMetricsType.body_mass_index_metrics.value)] = [value]

    def add_basal_metabolic_rate(self, value, date):
        if self._in_dict(date, BodyMetricsType.basal_metabolic_rate.value):
            self.dictionary[(date, BodyMetricsType.basal_metabolic_rate.value)].append(value)
        else:
            self.dictionary[(date, BodyMetricsType.basal_metabolic_rate.value)] = [value]

    def add_lean_body_mass(self, value, date):
        if self._in_dict(date, BodyMetricsType.lean_body_mass):
            self.dictionary[(date, BodyMetricsType.lean_body_mass.value)].append(value)
        else:
            self.dictionary[(date, BodyMetricsType.lean_body_mass.value)] = [value]

    def add_fat_mass(self, value, date):
        if self._in_dict(date, BodyMetricsType.fat_mass.value):
            self.dictionary[(date, BodyMetricsType.fat_mass.value)].append(value)
        else:
            self.dictionary[(date, BodyMetricsType.fat_mass.value)] = [value]

    def add_weight(self, value, date):
        if self._in_dict(date, BodyMetricsType.weight.value):
            self.dictionary[(date, BodyMetricsType.weight.value)].append(value)
        else:
            self.dictionary[(date, BodyMetricsType.weight.value)] = [value]

    def add_height(self, value, date):
        if self._in_dict(date, BodyMetricsType.height.value):
            self.dictionary[(date, BodyMetricsType.height.value)].append(value)
        else:
            self.dictionary[(date, BodyMetricsType.height.value)] = [value]

    def add_fat_percentage(self, value, date):
        if self._in_dict(date, BodyMetricsType.fat_percentage.value):
            self.dictionary[(date, BodyMetricsType.fat_percentage.value)].append(value)
        else:
            self.dictionary[(date, BodyMetricsType.fat_percentage.value)] = [value]

    def add_percentage_of_water_level(self, value, date):
        if self._in_dict(date, BodyMetricsType.percentage_of_water_level.value):
            self.dictionary[(date, BodyMetricsType.percentage_of_water_level.value)].append(value)
        else:
            self.dictionary[(date, BodyMetricsType.percentage_of_water_level.value)] = [value]

    def _in_dict(self, date, metrics_type):
        if (date, metrics_type) in self.dictionary.keys():
            return True
        return False