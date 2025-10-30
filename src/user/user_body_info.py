# from src. import UserBodyGoals


class UserBodyInfo:
    def __init__(self):
        self.weight: float = 0.0
        self.height: float = 0.0
        self.fat_percentage: float = 0.0
        self.percentage_of_water_level: float = 0.0
        self.user_body_goals = None

    def get_weight(self) -> float:
        return self.weight

    def get_height(self) -> float:
        return self.height

    def get_fat_percentage(self) -> float:
        return self.fat_percentage

    def get_percentage_of_water_level(self) -> float:
        return self.percentage_of_water_level

    def set_weight(self, weight):
        try:
            self._validate_data_for_setters(weight)
        except ValueError:
            pass
        self.weight = weight

    def set_height(self, height):
        try:
            self._validate_data_for_setters(height)
        except ValueError:
            pass
        self.height = height

    def set_fat_percentage(self, fat_percentage):
        try:
            self._validate_data_for_setters(fat_percentage)
        except ValueError as Error:
            pass
        self.fat_percentage = fat_percentage

    def set_percentage_of_water_level(self, percentage_of_water_level):
        try:
            self._validate_data_for_setters(percentage_of_water_level)
        except ValueError as Error:
            print(Error)
            return
        self.percentage_of_water_level = percentage_of_water_level

    def _validate_data_for_setters(self, data):
        if data < 0 or data is None:
            raise ValueError("data must be an positive number")
