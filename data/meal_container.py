from services.nutrition.meal import Meal


class MealContainer:
    def __init__(self):
        self.dict = {}

    def add_meal(self, meal: Meal, data):
        if data in self.dict:
            self.dict[data].append(meal)
        else:
            self.dict[data] = [meal]

    def get_history(self):
        return self.dict

    def find_by_name(self, name: str):
        result = []
        for day, meals in self.dict.items():
            for meal in meals:
                if meal.meal_name == name:
                    result.append(meal)
        return result

    def sort_by_calories(self, date):
        if date not in self.dict:
            return []
        return sorted(self.dict[date], key=lambda m: m.calories, reverse=True)
