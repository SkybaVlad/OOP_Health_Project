from src.body_metrics.type_metrics.weight_metrics import WeightMetrics
from src.body_metrics.type_metrics.fat_metrics import FatMetrics
from src.body_metrics.type_metrics.muscle_metrics import MuscleMetrics


class BodyMetrics:
    def __init__(self):
        self.weight_metrics = WeightMetrics()
        self.fat_metrics = FatMetrics
        self.muscle_metrics = MuscleMetrics()

    def get_weight(self):
        return self.weight_metrics.get_weight()

    def set_weight(self, value_of_weight):
        self.weight_metrics.set_weight(value_of_weight)
