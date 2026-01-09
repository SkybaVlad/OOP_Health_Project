from enum import Enum


class MealType(Enum):
    BREAKFAST = "Breakfast"
    LUNCH = "Lunch"
    DINNER = "Dinner"
    SNACK = "Snack"


class Meal:
    def __init__(self, meal_name: str, calories: int, meal_type: MealType):
        self.meal_name = meal_name
        self.calories = calories
        self.meal_type = meal_type
