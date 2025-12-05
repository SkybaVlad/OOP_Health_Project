from data.activity_container import ActivityContainer
from data.body_metrics_container import BodyMetricsContainer, BodyMetricsType
from data.meal_container import MealContainer
from services.activities.activity_type import SpecificActivityType
from data.filtration import (
    FiltrationActivity,
    ActivityCriteria,
    BodyMetricsCriteria,
    FiltrationBodyMetrics,
)
from services.nutrition.meal import Meal


class FacadeContainer:
    def __init__(self):
        self.body_metrics_container = BodyMetricsContainer()
        self.activity_container = ActivityContainer()
        self.filtration_activity = FiltrationActivity()
        self.filtration_body_metrics = FiltrationBodyMetrics()
        self.meal_container = MealContainer()

    def add_activity(
        self, activity_object: SpecificActivityType, data_of_activity: str
    ) -> None:
        self.activity_container.add_activity(activity_object, data_of_activity)

    def add_meal(self, meal: Meal, data):
        self.meal_container.add_meal(meal, data)

    def add_body_metrics(self, metrics_type, value, data) -> None:
        self.body_metrics_container.add_body_metrics(metrics_type, value, data)

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
        return self.filtration_activity.filter_by_greater_value_of_burned_calories()

    def filter_activity_by_lesser_value_on_calories(
        self, filtration_criteria: ActivityCriteria
    ) -> list:
        self.filtration_activity.set_filtration_criteria(filtration_criteria)
        return self.filtration_activity.filter_by_less_value_of_burned_calories()

    def filter_activity_by_duration(
        self, filtration_criteria: ActivityCriteria
    ) -> list:
        pass

    def filter_body_metrics_by_type(
        self, body_metrics_criteria: BodyMetricsCriteria
    ) -> list:
        self.filtration_body_metrics.set_filtration_criteria(body_metrics_criteria)
        return self.filtration_body_metrics.filter_by_type()

    def filter_body_metrics_by_specific_data(
        self, body_metrics_criteria: BodyMetricsCriteria
    ) -> list:
        self.filtration_body_metrics.set_filtration_criteria(body_metrics_criteria)
        return self.filtration_body_metrics.filter_by_specific_data()

    def filter_body_metrics_period(
        self, body_metrics_criteria: BodyMetricsCriteria
    ) -> list:
        self.filtration_body_metrics.set_filtration_criteria(body_metrics_criteria)
        return self.filtration_body_metrics.filter_by_period()

    def filter_body_metrics_by_greater_value_of_burned_calories(
        self, body_metrics_criteria: BodyMetricsCriteria
    ) -> list:
        self.filtration_body_metrics.set_filtration_criteria(body_metrics_criteria)
        return self.filtration_body_metrics.filter_by_greater_value()

    def filter_body_metrics_by_lesser_value_on_calories(
        self, body_metrics_criteria: BodyMetricsCriteria
    ) -> list:
        self.filtration_body_metrics.set_filtration_criteria(body_metrics_criteria)
        return self.filtration_body_metrics.filter_by_less_value()
