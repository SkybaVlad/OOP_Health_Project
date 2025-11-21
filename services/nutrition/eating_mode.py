class EatingMode:
    def adjust_calories(self, meal):
        return meal.calories


class Bulking(EatingMode):

    def adjust_calories(self, meal):
        return meal.calories + 200


class Slimming(EatingMode):
    def adjust_calories(self, meal):
        return meal.calories - 200


class Balancing(EatingMode):
    def adjust_calories(self, meal):
        return meal.calories
