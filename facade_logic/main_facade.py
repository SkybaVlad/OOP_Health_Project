from facade_logic.facade_analysis import AnalysisFacade
from facade_logic.facade_filtration import FilterFacade
from facade_logic.facade_dairy_manager import DairyFacade
from services.user.user_info import User
from services.user.user_body_info import UserBodyInfo


class MainFacade:
    def __init__(self, user: User):
        self.filter_facade = FilterFacade()
        self.analysis_facade = AnalysisFacade()
        self.dairy_facade = DairyFacade()
        self.user_body_info = UserBodyInfo()
        self.user = user

    def add_weight(self, weight_value):
        self.user_body_info.set_weight(weight_value)
        self.dairy_facade.add_weight(weight_value)

    def add_height(self, height_value):
        self.user_body_info.set_height(height_value)
        self.dairy_facade.add_weight(height_value)

    def add_fat_percentage(self, fat_percentage_value):
        self.user_body_info.set_fat_percentage(fat_percentage_value)
        self.dairy_facade.set_fat_percentage(fat_percentage_value)


user = User('Vlad', 'Skyba', 19, 'male')
facade = MainFacade(user)
facade.add_weight(100)
facade.add_height(100)
facade.add_fat_percentage(200)
print(facade.user_body_info.get_weight())
print(facade.user_body_info.get_height())
facade.add_weight(300)
print(facade.user_body_info.get_weight())
print(facade.dairy_facade.health_diary.get_history_of_days())
