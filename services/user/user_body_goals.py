class UserBodyDailyGoals:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            return super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, "initialize"):
            self.water_goal = 0
            self.consumed_calories_goal = 0
            self.burned_calories_goal = 0
            self.initialize = True

    def set_water_goal(self, user_water_goal: float):
        self.water_goal = user_water_goal

    def get_water_goal(self):
        return self.water_goal

    def set_calories_goal(self, calories_goal: float):
        self.consumed_calories_goal = calories_goal

    def get_consumed_calories_goal(self):
        return self.consumed_calories_goal

    def set_burned_calories_goal(self, burned_calories_goal: float):
        self.burned_calories_goal = burned_calories_goal

    def get_burned_calories_goal(self):
        return self.burned_calories_goal
