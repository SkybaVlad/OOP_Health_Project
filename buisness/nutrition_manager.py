from services.nutrition.nutrition_tracking import NutritionType


class NutritionManager:
    def __init__(self):
        self.history = []

    def add_nutrition(self, new_meal: NutritionType):
        self.history.append(new_meal)
