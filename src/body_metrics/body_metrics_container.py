import enum


class BodyMetricsType(enum.Enum):
    body_mass_index_metrics = 'bmi'
    basal_metabolic_rate = 'bmr'
    lean_body_mass = 'lbm'
    fat_mass = 'fm'


class BodyMetricsContainer:
    def __init__(self):
        pass
