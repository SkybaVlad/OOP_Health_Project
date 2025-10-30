import math


class BodyMetrics:
    def __init__(self):
        pass

    def calculate_body_mass_index_metrics(self, user_weight, user_height) -> float:
        return user_weight / math.pow(user_height / 100, 2)

    def calculate_basal_metabolic_rate_metrics(
        self, user_weight, user_height, user_age, user_sex
    ) -> float:
        if user_sex == 'male':
            return 10 * user_weight + 6.25 * user_height - 5 * user_age + 5
        else:
            return 10 * user_weight + 6.25 * user_height - 5 * user_age - 161

    def calculate_lean_body_mass_metrics(
        self, user_weight, user_percentage_of_fat
    ) -> float:
        return user_weight * (1 - user_percentage_of_fat / 100)

    def calculate_fat_mass_metrics(self, user_weight, user_percentage_of_fat) -> float:
        lbm_metrics = self.calculate_lean_body_mass_metrics(
            user_weight, user_percentage_of_fat
        )
        return user_weight - lbm_metrics
