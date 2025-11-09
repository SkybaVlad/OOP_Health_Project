class UserBodyInfo:
    def __init__(self):
        self.__weight: float = 0.0
        self.__height: float = 0.0
        self.__fat_percentage: float = 0.0
        self.__percentage_of_water_level: float = 0.0
        self.__body_mass_index: float = 0.0
        self.__basal_metabolic_rate: float = 0.0
        self.__lean_body_mass: float = 0.0
        self.__fat_mass: float = 0.0

    def get_weight(self) -> float:
        return self.__weight

    def get_height(self) -> float:
        return self.__height

    def get_fat_percentage(self) -> float:
        return self.__fat_percentage

    def get_percentage_of_water_level(self) -> float:
        return self.__percentage_of_water_level

    def get_body_mass_index(self) -> float:
        return self.__body_mass_index

    def get_basal_metabolic_rate(self) -> float:
        return self.__basal_metabolic_rate

    def get_lean_body_mass(self) -> float:
        return self.__lean_body_mass

    def get_fat_mass(self):
        return self.__fat_mass

    def set_weight(self, weight):
        self.__validate_data_for_setters(weight)
        self.__weight = weight

    def set_height(self, height):
        self.__validate_data_for_setters(height)
        self.__height = height

    def set_fat_percentage(self, fat_percentage):
        self.__validate_data_for_setters(fat_percentage)
        self.__fat_percentage = fat_percentage

    def set_percentage_of_water_level(self, percentage_of_water_level):
        self.__validate_data_for_setters(percentage_of_water_level)
        self.__percentage_of_water_level = percentage_of_water_level

    def set_body_mass_index(self, body_mass_index):
        self.__body_mass_index = body_mass_index

    def set_basal_metabolic_rate(self, basal_metabolic_rate):
        self.__basal_metabolic_rate = basal_metabolic_rate

    def set_lean_body_mass(self, lean_body_mass):
        self.__lean_body_mass = lean_body_mass

    def set_fat_mass(self, fat_mass):
        self.__fat_mass = fat_mass

    def __validate_data_for_setters(self, data):
        if data is None or data < 0:
            raise ValueError("data must be an positive number or not None")
