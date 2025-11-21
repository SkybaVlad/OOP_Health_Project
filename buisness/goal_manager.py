from services.user.user_body_goals import UserBodyGoals


class GoalManager:

    def __init__(self):
        self.history = []

    def add_goals(self, new_goal: UserBodyGoals):
        self.history.append(new_goal)

    def get_latest_goal(self):
        if not self.history:
            return None
        return self.history[-1]

    def check_history(self):
        if not self.history:
            return None
        return self.history
