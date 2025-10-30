from src.body.body_info import BodyInfo
import math


class BodyMetrics:
    def __init__(self):
        pass

    # def get_body_mass_index_metrics(self):
    #     user_weight = BodyInfo.get_weight()
    #     user_height = BodyInfo.get_height()
    #     return user_weight / math.pow(user_height, 2)

    def get_percentage_of_fat_metrics(self):
        pass

    # def get_lean_body_mass_metrics(self):
    #     if man:
    #         return 0.407 * BodyInfo.get_weight() + 0.267 * BodyInfo.get_height() - 19.2
    #     else:
    #         return 0.252 * BodyInfo.get_weight() + 0.473 * BodyInfo.get_height() - 48.3
