class Criteria:
    def __init__(self):
        self.metric_type = None
        self.specific_date = None
        self.start_period = None
        self.end_period = None
        self.max_value = None
        self.min_value = None

    def set_metrics_type(self, metrics_type):
        self.metric_type = metrics_type

    def set_specific_date(self, specific_date):
        self.specific_date = specific_date

    def set_start_period(self, start_period):
        self.start_period = start_period

    def set_end_period(self, end_period):
        self.end_period = end_period

    def set_max_value(self, max_value):
        self.max_value = max_value

    def set_min_value(self, min_value):
        self.min_value = min_value

    def get_condition_value(self):
        return self.max_value

    def get_specific_date(self):
        return self.specific_date

    def get_start_period(self):
        return self.start_period

    def get_end_period(self):
        return self.end_period

    def get_metrics_type(self):
        return self.metric_type
