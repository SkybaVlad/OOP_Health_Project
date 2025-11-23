from data.body_metrics_container import BodyMetricsContainer
from data.criteria import Criteria
from abc import ABC, abstractmethod


class Filtration:
    def __init__(self, filtration_criteria, body_metrics):
        pass

    def filter_by_type(self):
        pass


class FiltrationStrategy(ABC):
    @abstractmethod
    def filter(self, body_metrics_container: BodyMetricsContainer, criteria: Criteria):
        pass
