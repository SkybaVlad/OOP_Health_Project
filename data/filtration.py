from data.body_metrics_container import BodyMetricsContainer
from data.criteria import Criteria


class Filtration:
    def __init__(self, filtration_criteria, body_metrics):
        pass

    def filter_by_type(self):



class FiltrationStrategy(ABC):
    @abstractmethod
    def filter(self, body_metrics_container: BodyMetricsContainer, criteria: Criteria):
        pass


class FiltrationStrategyContext:
    def __init__(self):
        self.filtration_strategy = None

    def set_filtration_strategy(self, filtration_strategy: FiltrationStrategy):
        self.filtration_strategy = filtration_strategy

    def filter(self, body_metrics_container: BodyMetricsContainer):
        self.filtration_strategy.filter(body_metrics_container)


class FiltrationSpecificTypeOfMetrics(FiltrationStrategy):
    def filter(self, body_metrics_container: BodyMetricsContainer, criteria: Criteria):
        pass


class FiltrationAllMetrics(FiltrationStrategy):
    def filter(self, body_metrics_container: BodyMetricsContainer, criteria: Criteria):
        pass


class FiltrationByTypeOfMetricsAllPeriod(FiltrationStrategy):
    def filter(self, body_metrics_container: BodyMetricsContainer, criteria: Criteria):
        """This method doing filter depending on metrics type and return
        list of tuples that have the following structure (date, metrics_value)"""

        metrics_type = criteria.get_metrics_type()

        dictionary_of_activities = body_metrics_container.get_body_metrics()
        list_of_activities = []
        for date, metrics in dictionary_of_activities:
            if metrics_type == metrics:
                list_of_activities.append(
                    (date, dictionary_of_activities[(date, metrics_type)])
                )
        return list_of_activities


class FiltrationByPeriod(FiltrationStrategy):
    def filter(self, body_metrics_container: BodyMetricsContainer, criteria: Criteria):
        pass


class FiltrationByDate(FiltrationStrategy):
    def filter(self, body_metrics_container: BodyMetricsContainer, criteria: Criteria):
        pass


class FiltrationGreaterThan(FiltrationStrategy):
    def filter(self, body_metrics_container: BodyMetricsContainer, criteria: Criteria) -> list:
        """This method doing filter depending on condition value. All data in returned list
        must be over than condition value"""

        dictionary_of_activities = body_metrics_container.get_body_metrics()
        list_of_activities = []
        for date, metrics_type in dictionary_of_activities:
            if dictionary_of_activities[(date, criteria.get_metrics_type())] > criteria.get_condition_value():
                list_of_activities.append(
                    (date, dictionary_of_activities[(date, metrics_type)])
                )
        return list_of_activities


class FiltrationLessThan(FiltrationStrategy):
    def filter(self, body_metrics_container: BodyMetricsContainer, criteria: Criteria) -> list:
        """This method doing filter depending on condition value. All data in returned list
        must be less than condition value"""

        dictionary_of_activities = body_metrics_container.get_body_metrics()
        list_of_activities = []
        for date, metrics_type in dictionary_of_activities:
            if dictionary_of_activities[(date, criteria.get_metrics_type())] < criteria.get_condition_value():
                list_of_activities.append(
                    (date, dictionary_of_activities[(date, metrics_type)])
                )
        return list_of_activities