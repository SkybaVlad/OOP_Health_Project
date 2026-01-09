class Sleep:
    def __init__(self, woke_up, went_to_sleep):
       self.woke_up = woke_up
       self.went_to_sleep = went_to_sleep

    def get_sleep_duration(self):
        if self.woke_up < self.went_to_sleep:
            temp = 24 - self.went_to_sleep + self.woke_up
        else:
            temp = self.woke_up - self.went_to_sleep
        return temp

