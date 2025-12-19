from abc import ABC, abstractmethod
from services.nutrition.meal import Meal
from enum import Enum


class EatingModeType(Enum):
    BALANCING = "balancing"
    BULKING = "bulking"
    SLIMMING = "slimming"


class EatingMode(ABC):
    @abstractmethod
    def evaluate_meal(self, meal: Meal, daily_calories: int) -> str:
        pass


class BalancingMode(EatingMode):
    def evaluate_meal(self, meal: Meal, daily_calories: int) -> str:
        return "OK"


class BulkingMode(EatingMode):
    def evaluate_meal(self, meal: Meal, daily_calories: int) -> str:
        if meal.calories < 400:
            return "Замало калорій для набору маси"
        return "Добре для набору маси"


class SlimmingMode(EatingMode):
    def evaluate_meal(self, meal: Meal, daily_calories: int) -> str:
        if daily_calories + meal.calories > 1800:
            return "Перевищення денної норми"
        return "OK для схуднення"
