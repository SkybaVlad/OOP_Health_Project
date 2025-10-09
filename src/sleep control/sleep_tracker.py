class Sleep:
    def __init__(self, woke_up, went_to_sleep):
       self.woke_up = woke_up
       self.went_to_sleep = went_to_sleep

    def get_sleep_duration(self):
        temp = int(self.went.to.sleep-self.woke_up)
        if temp < 8 :
            print("Ops, you need sleep more")
        else:
            print("My congratulations, you got some sleep and fulled energy:)")
        return temp

