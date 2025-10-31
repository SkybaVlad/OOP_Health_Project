from src.user.user_body_info import UserBodyInfo


class UserBodyGoals:
    def __init__(self):
        self.user_body_info = UserBodyInfo()
        self.total_water_goal = 0
        self.total_calories_goal = 0

    def set_total_water_goal(self) -> float:
        return self.total_water_goal

    def calculate_total_water_goal(self):
        weight = self.user_body_info.get_weight()
        self.total_water_goal = weight*30
        return self.total_water_goal

    def calculate_total_calories_goal(self,weight):
         pass

    def get_total_water_goal(self):
        return self.total_water_goal

    def get_total_calories_goal(self):
        return self.total_calories_goal





