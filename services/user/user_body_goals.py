from services.user.user_body_info import UserBodyInfo
from services.user.user_info import User
from services.body_metrics.body_metrics import BodyMetrics


class UserBodyGoals:
    def __init__(
        self, user_body_info: UserBodyInfo, user: User, user_body_metrics: BodyMetrics
    ):
        self.user_body_info = user_body_info
        self.user = user
        self.user_body_metrics = user_body_metrics

        self.total_water_goal = 0
        self.total_calories_goal = 0

    # ==========WATER===========
    def set_total_water_goal(self):
        weight = self.user_body_info.get_weight()
        self.total_water_goal = weight * 30.0

    def get_total_water_goal(self):
        return self.total_water_goal

    # ==========CALORIES===========
    # Set ActivityLevel

    def calculate_total_calories_goal(self):
        bmr = self.body_metrics.calculate_basal_metabolic_rate_metrics = (
            self.body_metrics.calculate_basal_metabolic_rate_metrics(
                self.user_body_info.get_weight(),
                self.user_body_info.get_height(),
                self.user.get_age(),
                self.user.get_sex(),
            )
        )
        # self.total_calories_goal= bmr*activity_level придумати як рівень активності дізнаватися

    def get_total_calories_goal(self):
        return self.total_calories_goal
