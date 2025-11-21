class UserBodyGoals:
    def __init__(self):
        self.water_goal = 0
        self.calories_goal = 0

    # ==========WATER===========
    def set_water_goal(self,user_water_goal: float):
        self.water_goal = user_water_goal

    def get_water_goal(self):
        return self.water_goal

    # ==========CALORIES===========
    def set_calories_goal(self,calories_goal: float):
        self.calories_goal = calories_goal

    def get_calories_goal(self):
        return self.calories_goal
