class UserBodyInfo:
    def __init__(self, weight: float, height: float):
        self.weight: float = weight
        self.height: float = height
        self.fat_percentage: float = 0.0
        self.body_mass_index: float = 0.0
        self.percentage_of_water_level: float = 0.0
        self.lean_body_mass_index: float = 0

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height

    def get_fat_percentage(self):
        return self.fat_percentage

    def get_body_mass_index(self):
        return self.body_mass_index

    def get_percentage_of_water_level(self):
        return self.percentage_of_water_level

    def get_lean_body_mass_index(self):
        return self.lean_body_mass_index

    def set_weight(self, weight):
        self.weight = weight

    def set_height(self, height):
        self.height = height

    def set_fat_percentage(self, fat_percentage):
        self.fat_percentage = fat_percentage

    def set_body_mass_index(self, body_mass_index):
        self.body_mass_index = body_mass_index

    def set_get_percentage_of_water_level(self, percentage_of_water_level):
        self.percentage_of_water_level = percentage_of_water_level

    def set_get_lean_body_mass_index(self, lean_body_mass_index):
        self.lean_body_mass_index = lean_body_mass_index
