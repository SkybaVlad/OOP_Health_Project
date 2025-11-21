from services.sleep_control.sleep_tracker import Sleep

class SleepManager:
    def __init__(self):
        self.history = []

    def add_sleep(self, sleep: Sleep):
        self.history.append(sleep)

    def get_latest_sleep(self):
        if  not self.history:
            return None
        return self.history[-1]

    def check_history(self):
        return self.history