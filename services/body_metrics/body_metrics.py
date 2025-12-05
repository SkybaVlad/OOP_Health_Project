import math
from abc import ABC, abstractmethod
from enum import Enum


class BodyMetricsType(Enum):
    body_mass_index_metrics = 'bmi'
    basal_metabolic_rate = 'bmr'
    lean_body_mass = 'lbm'
    fat_mass = 'fm'
    weight = 'weight'
    height = 'height'
    fat_percentage = 'fp'
    percentage_of_water_level = 'fwl'


class StrategyBodyMetricsInterface(ABC):
    @abstractmethod
    def calculate(self):
        pass


class Context:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: StrategyBodyMetricsInterface):
        self.strategy = strategy

    def calculate(self):
        self.strategy.calculate()


class StrategyBMICalculator(StrategyBodyMetricsInterface):
    def __init__(self, user_weight, user_height):
        self.user_weight = user_weight
        self.user_height = user_height

    def calculate(self):
        return self.user_weight / math.pow(self.user_height / 100, 2)


class StrategyBMRCalculator(StrategyBodyMetricsInterface):
    def __init__(self, user_weight, user_height, user_age, user_sex):
        self.user_weight = user_weight
        self.user_height = user_height
        self.user_age = user_age
        self.user_sex = user_sex

    def calculate(self):
        if self.user_sex == 'male':
            return (
                10 * self.user_weight + 6.25 * self.user_height - 5 * self.user_age + 5
            )
        else:
            return (
                10 * self.user_weight
                + 6.25 * self.user_height
                - 5 * self.user_age
                - 161
            )


class StrategyLeanBodyMassCalculator(StrategyBodyMetricsInterface):
    def __init__(self, user_weight, user_percentage_of_fat):
        self.user_weight = user_weight
        self.user_percentage_of_fat = user_percentage_of_fat

    def calculate(self):
        return self.user_weight * (1 - self.user_percentage_of_fat / 100)


class StrategyFatMassCalculator(StrategyBodyMetricsInterface):
    def __init__(self, user_weight, user_percentage_of_fat):
        self.user_weight = user_weight
        self.user_percentage_of_fat = user_percentage_of_fat

    def calculate(self):
        lean_body_mass_value = StrategyLeanBodyMassCalculator(
            self.user_weight, self.user_percentage_of_fat
        )
        return self.user_weight - lean_body_mass_value
