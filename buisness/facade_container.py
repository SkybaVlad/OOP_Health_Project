from data.activity_container import ActivityContainer
from data.body_metrics_container import BodyMetricsContainer, BodyMetricsType
from data.meal_container import MealContainer
from services.activities.activity_type import SpecificActivityType
from data.filtration import (
    FiltrationActivity,
    ActivityCriteria,
    FiltrationCriteria,
    FiltrationBodyMetrics,
)


class FacadeContainer:
    def __init__(self):
        self.body_metrics_container = BodyMetricsContainer()
        self.activity_container = ActivityContainer()
        self.filtration_activity = FiltrationActivity()
        self.filtration_body_metrics = FiltrationBodyMetrics()

    def add_activity(
        self, activity_object: SpecificActivityType, data_of_activity: str
    ) -> None:
        self.activity_container.add_activity(activity_object, data_of_activity)

    def filter_activity_by_type(self, filtration_criteria: ActivityCriteria) -> list:
        self.filtration_activity.set_filtration_criteria(filtration_criteria)
        return self.filtration_activity.filter_by_type()

    def filter_activity_by_specific_data(
        self, filtration_criteria: ActivityCriteria
    ) -> list:
        self.filtration_activity.set_filtration_criteria(filtration_criteria)
        return self.filtration_activity.filter_by_specific_data()

    def filter_activity_by_period(self, filtration_criteria: ActivityCriteria) -> list:
        self.filtration_activity.set_filtration_criteria(filtration_criteria)
        return self.filtration_activity.filter_by_period()

    def filter_activity_by_greater_value_on_calories(
        self, filtration_criteria: ActivityCriteria
    ) -> list:
        self.filtration_activity.set_filtration_criteria(filtration_criteria)
        pass

    def filter_activity_by_lesser_value_on_calories(
        self, filtration_criteria: ActivityCriteria
    ) -> list:
        pass

    def filter_activity_by_duration(
        self, filtration_criteria: ActivityCriteria
    ) -> list:
        pass

    def add_body_metrics(self, metrics_type, value, data) -> None:
        self.body_metrics_container.add_body_metrics(metrics_type, value, data)
