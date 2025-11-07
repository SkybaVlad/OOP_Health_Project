from services.activities.activity_type import SpecificActivityType


class ActivityContainer:

    def __init__(self):
        self.dictionary = {}

    # need check on invalid param

    def add_activity(
        self, specific_activity_object: SpecificActivityType, data_of_activity: str
    ):
        if data_of_activity in self.dictionary.keys():
            self.dictionary[data_of_activity].append(specific_activity_object)
        else:
            self.dictionary[data_of_activity] = [specific_activity_object]

    def get_activity_in_specific_date(self, data_of_activity: str) -> list:
        return self.dictionary[data_of_activity]

    def get_all_activities(self) -> list:
        sorted_list_of_activities = sorted(self.dictionary.items())
        return sorted_list_of_activities

    def get_all_dates(self):
        pass


activity_object1 = SpecificActivityType("Football", 400, '17:20', '19:20')
activity_object2 = SpecificActivityType("Running", 500, '16:20', '17:20')
object = ActivityContainer()
object.add_activity(activity_object1, '03.05.2007')
object.add_activity(activity_object2, '01.05.2007')
print(object.get_all_activities())
