class ActivityContainer:

    def __init__(self):
        self.dictionary = {}

    # need check on invalid param

    def add_activity(self, activity_name, data_of_activity):
        if data_of_activity in self.dictionary.keys():
            self.dictionary[data_of_activity].append(activity_name)
        else:
            self.dictionary[data_of_activity] = [activity_name]

    def remove_activity(self):
        pass

    def remove_all_activities(self):
        pass

    def get_activity_in_specific_date(self, data_of_activity):
        return self.dictionary[data_of_activity]

    def get_all_activities(self):
        pass
        # need sort hashtable
