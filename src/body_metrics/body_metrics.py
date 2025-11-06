import math


class BodyMetrics:
    def __init__(self):
        pass

    def calculate_body_mass_index_metrics(self, user_weight, user_height) -> float:
        self.__validate_date(weight=user_weight, height=user_height)
        return user_weight / math.pow(user_height / 100, 2)

    def calculate_basal_metabolic_rate_metrics(
        self, user_weight, user_height, user_age, user_sex
    ) -> float:
        self.__validate_date(weight=user_weight, height=user_height)
        if user_sex == 'male':
            return 10 * user_weight + 6.25 * user_height - 5 * user_age + 5
        else:
            return 10 * user_weight + 6.25 * user_height - 5 * user_age - 161

    def calculate_lean_body_mass_metrics(
        self, user_weight, user_percentage_of_fat
    ) -> float:
        self.__validate_date(weight=user_weight, fat_percantage=user_percentage_of_fat)
        return user_weight * (1 - user_percentage_of_fat / 100)

    def calculate_fat_mass_metrics(self, user_weight, user_percentage_of_fat) -> float:
        self.__validate_date(weight=user_weight, fat_percantage=user_percentage_of_fat)
        lbm_metrics = self.calculate_lean_body_mass_metrics(
            user_weight, user_percentage_of_fat
        )
        return user_weight - lbm_metrics

    def __validate_date(self, **kwargs):
        for key, value in kwargs.items():
            if value == 0:
                raise ValueError(f"The {key} cannot be 0.")
