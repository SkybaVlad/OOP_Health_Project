import enum


class BodyMetricsType(enum.Enum):
    body_mass_index_metrics = 'bmi'
    basal_metabolic_rate = 'bmr'
    lean_body_mass = 'lbm'
    fat_mass = 'fm'


class BodyMetricsContainer:
    def __init__(self):
        self.dictionary = {}

    def add_body_mass_index_metrics(self, value, date):
        self.dictionary[(date, BodyMetricsType.body_mass_index_metrics.value)] = value

    def add_basal_metabolic_rate(self, value, date):
        self.dictionary[(date, BodyMetricsType.basal_metabolic_rate.value)] = value

    def add_lean_body_mass(self, value, date):
        self.dictionary[(date, BodyMetricsType.lean_body_mass.value)] = value

    def add_fat_mass(self, value, date):
        self.dictionary[(date, BodyMetricsType.fat_mass.value)] = value
