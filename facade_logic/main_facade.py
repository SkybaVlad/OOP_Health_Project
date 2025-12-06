from facade_logic.facade_analysis import AnalysisFacade
from facade_logic.facade_filtration import FilterFacade
from facade_logic.user_input_facade import UserInputFacade
from facade_logic.facade_dairy_manager import DairyFacade
from services.user.user_info import User


class MainFacade:
    def __init__(self, user: User):
       self.user_input_facade = UserInputFacade(user)
       self.filter_facade = FilterFacade()
       self.analysis_facade = AnalysisFacade()
       self.dairy_facade = DairyFacade()

