from src.body_metrics.body_metrics import BodyMetrics
#from src.user.user import User


class UserBodyGoals:
    def __init__(self):
        #user = User(name, surname, age, sex)
        self.body_metrics = BodyMetrics()
        self.total_water_goal = 0
        self.total_calories_goal = 0

    def set_total_water_goal(self, weight):
        self.total_water_goal = self.calculate_total_water_goal(weight)

    def calculate_total_water_goal(self, weight):
        return weight * 30.0

    def calculate_total_calories_goal(self):
        self.body_metrics.calculate_basal_metabolic_rate_metrics = (
        self.body_metrics.calculate_basal_metabolic_rate_metrics
            (
            self.user_body_info.get_weight(),
            self.user_body_info.get_height(),
            self.user.get_age(),
            self.user.get_sex()
        ))

    def get_total_water_goal(self):
        return self.total_water_goal

    def get_total_calories_goal(self):
        return self.total_calories_goal
