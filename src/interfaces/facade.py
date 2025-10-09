from src.weight.weight import Weight
from src.activities.activity import Activity
from src.medicine.medicine import Medicine
from src.medicine.patient_status import PatientStatus
from src.medicine.examination import Examination
from src.nutrition_control.nutrition_tracker import Nutrition
from src.water_balance.waterbalance import WaterBalance


class Facade:

    def __init__(
        self,
    ):  # maybe add User class and send user object as arg of init method
        # self.weight = Weight()
        # self.activity = Activity()
        # self.medicine = Medicine()
        # self.patient_status = PatientStatus()
        # self.examination = Examination()
        # self.nutrition = Nutrition()
        # self.water_balance = WaterBalance()
        pass

    def get_weight(self):
        # self.weight.get_weight()
        pass

    def sleep(self):
        pass

    def eat(self):
        pass

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

    def drink_water(self):
        pass

    def get_medicine(self):
        pass
