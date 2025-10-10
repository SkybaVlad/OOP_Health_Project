from src.weight.weight import Weight
from src.activities.activity import Activity
from src.medicine.medicine import Medicine
from src.medicine.patient_status import PatientStatus
from src.medicine.examination import Examination
from src.nutrition_control.nutrition_tracker import Nutrition
from src.water_balance.waterbalance import WaterBalance
from src.sleep_control.sleep_tracker import Sleep

class Facade:

    def __init__(self, weight, activity, medicine,patient_status,examination,nutrition,water,sleep):
        self.weight = weight
        self.activity = activity
        self.medicine = medicine
        self.patient_status = patient_status
        self.examination = examination
        self.nutrition = nutrition
        self.water = water
        self.sleep = sleep

    def get_weight(self):
        self.weight.get_weight()

    def get_sleep_duration(self):
        self.sleep.get_sleep_duration()

    def eat(self,calories, meal_name):
        self.nutrition.add_meals(calories,meal_name)

    def get_consumed_calories(self):
        return self.nutrition.get_consumed_calories()

    def get_remaining_calories(self):
        return self.nutrition.get_remaining_calories()

    def do_activity(self):
        # do activity
        # burn calories
        # new weight
        pass

    def do_examination(self):
        # do examination
        # get result
        # if result is false
        #   patient_status = false
        # else patient_status = true
        pass

    def drink_water(self, amount_of_water):
        return self.water.add_water(amount_of_water)

    def get_consumed_water(self):
        return self.water.get_consumed()

    def get_remaining_water(self):
        return self.water.get_remaining()

    def get_medicine(self):
        pass
