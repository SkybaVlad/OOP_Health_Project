import enum
from services.body_metrics.body_metrics import BodyMetricsType


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
