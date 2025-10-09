class Activity:
    def __init__(self, sport_type, place, start_time, end_time):
        self.sport_type = sport_type
        self.place = place
        self.start_time = start_time
        self.end_time = end_time

    def burn_calories(self):
        pass

    def calculate_duration(self):
        return self.end_time - self.start_time
