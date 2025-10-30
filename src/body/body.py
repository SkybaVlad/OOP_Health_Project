from src.body.body_info import BodyInfo
from src.body.body_metrics.body_metrics import BodyMetrics


class Body:
    def __init__(self):
        # need thinking about doing body_info field None
        # maybe pass to facade ctr a user_info object or user_body_info, so maybe doing two classes like user_body_info and user_goals and pass it classes object to facade ctr
        self.body_info = BodyInfo()
        self.body_metrics = BodyMetrics()

    def get_weight(self):
        return self.weight_metrics.get_weight()

    def get_body_mass_index(self):
        pass

    def get_percentage_of_fat(self):
        pass

    def get_lean_body_mass(self):
        pass

    def load_user_body_info(self, sex, age, weight, height):
        self.body_info.set_sex(sex)
        self.body_info.set_age(age)
        self.body_info.set_weight(weight)
        self.body_info.set_height(height)
