from services.activities.activity_type import SpecificActivityType


class ActivityContainer:

    def __init__(self) -> None:
        self.dictionary = {}

    # need check on invalid param

    def add_activity(
        self, specific_activity_object: SpecificActivityType, data_of_activity: str
    ) -> None:
        if data_of_activity in self.dictionary.keys():
            self.dictionary[data_of_activity].append(specific_activity_object)
        else:
            self.dictionary[data_of_activity] = [specific_activity_object]

    def get_all_activities(self) -> dict:
        return self.dictionary
