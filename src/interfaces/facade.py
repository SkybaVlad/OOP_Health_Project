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
        medicine,
        total_calories,
        total_goal,
        woke_up,
        went_to_sleep,
    ):
        self.weight = Weight()
        self.medicine = medicine
        self.patient_status = PatientStatus()
        self.examination = Examination()
        self.nutrition = Nutrition(total_calories)
        self.water = WaterBalance(total_goal)
        self.sleep = Sleep(woke_up, went_to_sleep)

    def get_weight(self):
        weight_value = self.weight.get_weight()
        if weight_value is None:
            return None
        return weight_value

    def set_weight(self, value_of_weight):
        self.weight = self.weight.set_weight(value_of_weight)

    # maybe add load method that allows gets all data about users and initialize all fields in constructor

    def get_sleep_duration(self):
        return self.sleep.get_sleep_duration()

    def eat(self, calories, meal_name):
        self.nutrition.add_meals(calories, meal_name)

        consumed_calories = self.nutrition.consumed_calories
        total_calories = self.nutrition.total_calories

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

    def get_medicine(self):
        patient_status_of_health = self.patient_status.get_is_sick_status()
        if patient_status_of_health is None:
            print("You need to do examination to detect your health status")
            return
        if patient_status_of_health is False:
            self.medicine.calculate_dosage()
            self.patient_status.set_is_sick_status(True)
            self.patient_status.set_disease_type(None)
