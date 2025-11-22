from services.nutrition.meal import Meal, MealType


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

    def find_by_date(self, date):
        if date not in self.dict:
            return []
        return self.dict[date]

    def sort_meals(self, meals):
        return sorted(meals, key=lambda m: m.calories, reverse=True)

    def sort_all_meals(self):
        allmeals = []
        for meals in self.dict.values():
            allmeals.extend(meals)
        return self.sort_meals(allmeals)

    def sort_meals_by_day(self, date):
        daymeals = []
        for meal in self.dict[date]:
            daymeals.append(meal)
        return self.sort_meals(daymeals)
