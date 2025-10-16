from src.weight.weight import Weight
from src.activities.activity import Activity
from src.medicine.medicine import Medicine
from src.medicine.patient_status import PatientStatus
from src.medicine.examination import Examination
from src.nutrition_control.nutrition_tracker import Nutrition
from src.water_balance.waterbalance import WaterBalance
from src.sleep_control.sleep_tracker import Sleep


class Facade:

    def __init__(
        self,
        user,
        initial_weight,
        medicine,
        patient_status,
        nutrition,
        water,
        sleep,
    ):
        self.weight = Weight(initial_weight)
        self.medicine = medicine
        self.patient_status = PatientStatus()
        self.examination = Examination()
        self.nutrition = nutrition
        self.water = water
        self.sleep = sleep

    def get_weight(self):
        return self.weight.get_weight()

    def get_sleep_duration(self):
        return self.sleep.get_sleep_duration()

    def eat(self, calories, meal_name):
        self.nutrition.add_meals(calories, meal_name)

    def get_consumed_calories(self):
        return self.nutrition.get_consumed_calories()

    def get_remaining_calories(self):
        return self.nutrition.get_remaining_calories()

    def do_activity(self, activity_name, duration):
        activity_object = Activity(activity_name, duration)
        burned_calories = activity_object.count_of_burned_calories()
        weight_to_remove = burned_calories / 7700  # to get value in kilogram
        self.weight.remove_weight(weight_to_remove)  # change weight value for user

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
        return self.water.add_water(amount_of_water)

    def get_consumed_water(self):
        return self.water.get_consumed()

    def get_remaining_water(self):
        return self.water.get_remaining()

    def get_medicine(self):
        patient_status_of_health = self.patient_status.get_is_sick_status()
        if patient_status_of_health is None:
            print("You need to do examination to detect your health status")
            return
        if patient_status_of_health is False:
            self.medicine.calculate_dosage()
            self.patient_status.set_is_sick_status(True)
            self.patient_status.set_disease_type(None)
