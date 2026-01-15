class UserBodyDailyGoals:
    """This class contain user-defined values of goals.
    water_goal - how much of litres user want to drink every day

    consumed_calories - how many calories user need to eat every day

    burned_calories - how many calories user need to burn every day

    step_goal - how many steps user need to do every day."""

    def __init__(self):
        self.water_goal = 0
        self.consumed_calories_goal = 0
        self.burned_calories_goal = 0
        self.step_goal = 0

    def set_water_goal(self, user_water_goal: float):
        self.water_goal = user_water_goal

    def get_water_goal(self):
        return self.water_goal

    def set_consumed_calories_goal(self, calories_goal: float):
        self.consumed_calories_goal = calories_goal

    def get_consumed_calories_goal(self):
        return self.consumed_calories_goal

    def set_burned_calories_goal(self, burned_calories_goal: float):
        self.burned_calories_goal = burned_calories_goal

    def get_burned_calories_goal(self):
        return self.burned_calories_goal

    def set_step_goal(self, step_goal: float):
        self.step_goal = step_goal

    def get_step_goal(self) -> float:
        return self.step_goal


class DefaultUserBodyGoals:
    """This class has a constant values that describe
    what's minimum user need complete for healthy life

    count_of_steps = 7000 steps

    consumed_calories = 2000 cal

    burned_calories = 4000 cal

    water = 2 litres

    All this values is a class attribute, so you do not need to create
    objects of this class
    """

    count_of_steps = 7000
    consumed_calories = 2000
    burned_calories = 400
    water = 2
