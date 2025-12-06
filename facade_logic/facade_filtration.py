from data.health_diary import HealthDiary
from data.filtration import (
    ActivityCriteria,
    BodyMetricsCriteria,
    FiltrationActivity,
    FiltrationBodyMetrics,
)


class FilterFacade:
    def __init__(self):
        self.health_dairy: HealthDiary | None = None
        self.filtration_activity: FiltrationActivity | None = None

    def set_health_diary(self, health_diary: HealthDiary):
        self.health_dairy = health_diary

    def filter_days_by_activity_type(
        self, filtration_criteria: ActivityCriteria
    ) -> list:
        self.filtration_activity.set_filtration_criteria(filtration_criteria)
        return self.filtration_activity.filter_by_type()

    def filter_days_by_activity_in_specific_data(
        self, filtration_criteria: ActivityCriteria
    ) -> list:
        self.filtration_activity.set_filtration_criteria(filtration_criteria)
        return self.filtration_activity.filter_by_specific_data()

    def filter_days_by_activity_in_period(
        self, filtration_criteria: ActivityCriteria
    ) -> list:
        self.filtration_activity.set_filtration_criteria(filtration_criteria)
        return self.filtration_activity.filter_by_period()

    def filter_days_by_activity_by_greater_value_on_calories(
        self, filtration_criteria: ActivityCriteria
    ) -> list:
        self.filtration_activity.set_filtration_criteria(filtration_criteria)
        return self.filtration_activity.filter_by_greater_value_of_burned_calories()

    def filter_days_by_activity_by_lesser_value_on_calories(
        self, filtration_criteria: ActivityCriteria
    ) -> list:
        self.filtration_activity.set_filtration_criteria(filtration_criteria)
        return self.filtration_activity.filter_by_less_value_of_burned_calories()

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
