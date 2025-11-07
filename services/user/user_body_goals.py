from services.user.user_body_info import UserBodyInfo
from services.user.user_info import User


class UserBodyGoals:
    def __init__(self, user_body_info: UserBodyInfo, user: User):
        self.user_body_info = user_body_info
        self.user = user
        self.total_water_goal = 0
        self.total_calories_goal = 0

    def set_total_water_goal(self, weight):
        self.total_water_goal = self.calculate_total_water_goal(weight)

    def calculate_total_water_goal(self, weight):
        return weight * 30.0

    def calculate_total_calories_goal(self):
        self.body_metrics.calculate_basal_metabolic_rate_metrics = (
            self.body_metrics.calculate_basal_metabolic_rate_metrics(
                self.user_body_info.get_weight(),
                self.user_body_info.get_height(),
                self.user.get_age(),
                self.user.get_sex(),
            )
        )

    def get_total_water_goal(self):
        return self.total_water_goal

    def get_total_calories_goal(self):
        return self.total_calories_goal
