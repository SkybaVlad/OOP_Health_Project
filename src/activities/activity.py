class Activity:
    def __init__(self, activity_name, duration):
        self.activity_name = activity_name
        self.duration = duration

    def do_activity(self):
        pass

    def count_of_burned_calories(self):
        # calculate calories and return it, until return a const value
        return 180

    def calculate_duration(self):
        return self.duration
