from src.user.user_body_goals import UserBodyGoals
from src.user.user_info import User


class UserBodyInfo:
    def __init__(self, user: User):
        self.weight: float = 0.0
        self.height: float = 0.0
        self.fat_percentage: float = 0.0
        self.percentage_of_water_level: float = 0.0
        self.body_mass_index: float = 0.0
        self.basal_metabolic_rate: float = 0.0
        self.lean_body_mass: float = 0.0
        self.fat_mass: float = 0.0
        self.user_body_goals = UserBodyGoals(user)

    def get_weight(self) -> float:
        return self.weight

    def get_height(self) -> float:
        return self.height

    def get_fat_percentage(self) -> float:
        return self.fat_percentage

    def get_percentage_of_water_level(self) -> float:
        return self.percentage_of_water_level

    def get_body_mass_index(self) -> float:
        return self.body_mass_index

    def get_basal_metabolic_rate(self) -> float:
        return self.basal_metabolic_rate

    def get_lean_body_mass(self) -> float:
        return self.lean_body_mass

    def get_fat_mass(self):
        return self.fat_mass

    def set_weight(self, weight):
        self._validate_data_for_setters(weight)
        self.weight = weight

    def set_height(self, height):
        self._validate_data_for_setters(height)
        self.height = height

    def set_fat_percentage(self, fat_percentage):
        self._validate_data_for_setters(fat_percentage)
        self.fat_percentage = fat_percentage

    def set_percentage_of_water_level(self, percentage_of_water_level):
        self._validate_data_for_setters(percentage_of_water_level)
        self.percentage_of_water_level = percentage_of_water_level

    def set_body_mass_index(self, body_mass_index):
        self.body_mass_index = body_mass_index

    def set_basal_metabolic_rate(self, basal_metabolic_rate):
        self.basal_metabolic_rate = basal_metabolic_rate

    def set_lean_body_mass(self, lean_body_mass):
        self.lean_body_mass = lean_body_mass

    def set_fat_mass(self, fat_mass):
        self.fat_mass = fat_mass

    def _validate_data_for_setters(self, data):
        if data < 0 or data is None:
            raise ValueError("data must be an positive number")
