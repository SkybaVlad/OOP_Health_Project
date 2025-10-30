from src.body_metrics.body_metrics import BodyMetrics
from src.activities.activity import Activity
from src.medicine.medicine import Medicine
from src.medicine.patient_status import PatientStatus
from src.medicine.examination import Examination
from src.nutrition_control.nutrition_tracker import Nutrition
from src.water_balance.waterbalance import WaterBalance
from src.sleep_control.sleep_tracker import Sleep
from src.user.user_body_info import UserBodyInfo


class Facade:
    def __init__(self):
        self.user_body_info = UserBodyInfo()
        self.body_metrics = BodyMetrics()
        self.activity = Activity()
        # self.medicine = medicine
        # self.patient_status = PatientStatus()
        # self.examination = Examination()
        # self.nutrition = Nutrition(total_calories)
        # self.water = WaterBalance(total_goal)
        # self.sleep = Sleep(woke_up, went_to_sleep)

    def set_weight(self, weight):
        self.user_body_info.set_weight(weight)

    def get_weight(self):
        return self.user_body_info.get_weight()

    def set_height(self, height):
        self.user_body_info.set_height(height)

    def get_height(self):
        return self.user_body_info.get_height()

    def set_fat_percentage(self, fat_percentage):
        self.user_body_info.set_fat_percentage(fat_percentage)

    def get_fat_percentage(self):
        return self.user_body_info.get_fat_percentage()

    def set_percentage_of_water_level(self, percentage_of_water_level):
        self.user_body_info.set_percentage_of_water_level(percentage_of_water_level)

    def get_percentage_of_water_level(self):
        return self.user_body_info.get_percentage_of_water_level()

    def get_sleep_duration(self):
        return self.sleep.get_sleep_duration()

    def eat(self, calories, meal_name):
        self.nutrition.add_meals(calories, meal_name)

        consumed_calories = self.nutrition.get_consumed_calories()
        total_calories = self.nutrition.get_total_calories()

        if consumed_calories > total_calories:
            status = "Overate"  # add status to patient/user
            weight_to_add = (consumed_calories - total_calories) / 7700
            self.weight.add_weight(weight_to_add)
        else:
            status = "Eaten"  # add status to patient/user

    def get_consumed_calories(self):
        return self.nutrition.get_consumed_calories()

    def get_remaining_calories(self):
        return self.nutrition.get_remaining_calories()

    def do_activity(self, activity_name, intensity_rate, start_time, end_time, date):
        self.activity.create_specific_activity_type_object(
            activity_name, intensity_rate, start_time, end_time, date
        )
        count_of_burned_calories = self.activity.count_of_burned_on_specific_activity()
        # weight_to_remove = burned_calories / 7700  # to get value in kilogram
        # self.body_metrics.remove_weight(weight_to_remove)  # change body_metrics value for user

    def get_activities_in_specific_date(self, date_of_activities) -> list:
        return self.activity.get_activities_in_specific_date(date_of_activities)

    def get_history_of_all_activities(self) -> list:
        return self.activity.get_history_of_all_activities()

    def do_examination(self):
        self.examination.do_examination("Type Of Examination")
        result_of_examination = self.examination.get_result_of_examination()
        if result_of_examination is False:
            self.patient_status.set_is_sick_status(False)
            # detect a disease name and set it into patient_status.set_disease_type(disease_name)
        else:
            self.patient_status.set_is_sick_status(True)
            # detect a disease name and set it into patient_status.set_disease_type(None)

    def drink_water(self, amount_of_water):
        self.water.add_water(amount_of_water)

        consumed = self.water.get_consumed()
        total_goal = self.water.get_total_goal()

        if consumed > total_goal:
            status = "Overhydrated"  # add status to patient/user
        else:
            status = "Drinking"  # add status to patient/user

    def get_consumed_water(self):
        return self.water.get_consumed()

    def get_remaining_water(self):
        return self.water.get_remaining()

    # maybe add load_medicine_recipe()

    # def get_medicine(self):
    #     patient_status_of_health = self.patient_status.get_is_sick_status()
    #     if patient_status_of_health is None:
    #         print("You need to do examination to detect your health status")
    #         return
    #     if patient_status_of_health is False:
    #         self.medicine.calculate_dosage()
    #         self.patient_status.set_is_sick_status(True)
    #         self.patient_status.set_disease_type(None)

    def get_body_mass_index_metrics(self) -> float:
        return self.body_metrics.calculate_body_mass_index_metrics(
            self.user_body_info.get_weight(), self.user_body_info.get_height()
        )

    def get_basal_metabolic_rate_metrics(self) -> float:
        return self.body_metrics.calculate_basal_metabolic_rate_metrics()

    def get_lean_body_mass_metrics(self) -> float:
        return self.body_metrics.calculate_lean_body_mass_metrics(
            self.user_body_info.get_weight(), self.user_body_info.get_fat_percentage()
        )

    def get_fat_mass_metrics(self) -> float:
        return self.body_metrics.calculate_fat_mass_metrics(
            self.user_body_info.get_weight(), self.user_body_info.get_fat_percentage()
        )
