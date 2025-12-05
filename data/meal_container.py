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


class MealSorter:
    def sort_meals(self, meals):
        return sorted(meals, key=lambda m: m.calories, reverse=True)

    def sort_all_meals(self):
        all_meals = []
        for meals in self.dict.values():
            all_meals.extend(meals)
        return self.sort_meals(all_meals)

    def sort_meals_by_day(self, date):
        day_meals = []
        for meal in self.dict[date]:
            day_meals.append(meal)
        return self.sort_meals(day_meals)
