class Nutrition:

    def __init__(self, total_calories):
        self.total_calories = total_calories
        self.consumed_calories = 0
        self.calories_remaining = total_calories
        self.meals = []

    def add_meals(self,calories,meal_name):
        self.consumed_calories += calories
        self.calories_remaining -= calories
        self.meals.append(meal_name)
        return meal_name

    def get_consumed_calories(self):
        return self.consumed_calories

    def get_remaining_calories(self):
        return self.calories_remaining

    def get_total_calories(self):
        return self.total_calories