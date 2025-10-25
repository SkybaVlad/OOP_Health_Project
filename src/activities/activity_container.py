class ActivityContainer:

    def __init__(self):
        self.dictionary = {}

    # need check on invalid param

    # need typehints
    def add_activity(self, specific_activity_object, data_of_activity):
        if data_of_activity in self.dictionary.keys():
            self.dictionary[data_of_activity].append(specific_activity_object)
        else:
            self.dictionary[data_of_activity] = [specific_activity_object]

    def clear_all_activities(self):
        pass

    # need typehints tp return
    def get_activity_in_specific_date(self, data_of_activity):
        return self.dictionary[data_of_activity]

    def get_all_activities(self):
        pass
        # need sort hashtable

    def get_all_dates(self):
        pass
