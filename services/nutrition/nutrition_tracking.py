from services.user.user_body_goals import UserBodyGoals


class Nutrition:

    def __init__(self, user_body_goals: UserBodyGoals):
        self.user_body_goals = user_body_goals
        self.total_calories = user_body_goals.calculate_total_calories_goal()
        self.consumed_calories = 0
        self.calories_remaining = self.total_calories
        self.meals = []

    def add_meal(self, calories:float, meal_name: str):
        self.meals.append(meal_name)
        self.consumed_calories += calories
        self.calories_remaining -= calories
        return meal_name

    def get_consumed_calories(self):
        return self.consumed_calories

    def get_remaining_calories(self):
        return self.calories_remaining

    def get_total_calories(self):
        return self.total_calories

    def check_meals(self):
        for meal in self.meals:
            print(f"Meal: {meal}")
