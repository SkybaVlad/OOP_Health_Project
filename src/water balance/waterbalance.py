class WaterBalance:

    def __init__(self, total_goal):
        self.total_goal = total_goal
        self.consumed = 0
        self.remaining = total_goal
        self.water = []

    def add_water(self, amount_of_water):
        self.consumed += amount_of_water
        self.remaining -= amount_of_water
        self.water.append(f"{amount_of_water} - liters of water")
        print(f"{amount_of_water} - liters of water were just drunk, \nliters left to drink - {self.remaining}")

    def get_consumed(self):
        return self.consumed

    def get_remaining(self):
        return self.remaining