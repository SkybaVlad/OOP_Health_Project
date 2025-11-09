from data.body_metrics_container import BodyMetricsContainer


""" This Filtration class provide a different method to filter the data"""


class Filtration:
    def __init__(self, body_metrics_container: BodyMetricsContainer):
        self.body_metrics_container = body_metrics_container

    def get_history_of_specific_metrics_in_all_period(self, metrics_type) -> list:
        list_of_all_metrics = list(
            self.body_metrics_container.get_body_metrics().items()
        )
        list_of_specific_metrics_type = []
        for metrics in list_of_all_metrics:
            pass
        return list_of_all_metrics

    def get_history_of_specific_metrics_in_some_period(
        self, metrics_type, start_period, end_period
    ) -> list:
        pass
