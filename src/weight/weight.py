class Weight:
    def __init__(self, value):
        self.value = value

    def get_weight(self):
        return self.value

    def add_weight(self, weight):
        self.value += weight

    def remove_weight(self, weight):
        self.value -= weight
