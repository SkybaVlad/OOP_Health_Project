class BodyInfo:
    def __init__(self):
        self.sex = None
        self.age = None
        self.weight = None
        self.height = None

    def set_sex(self, sex):
        self.sex = sex

    def set_age(self, age):
        self.age = age

    def set_weight(self, weight):
        self.weight = weight

    def set_height(self, height):
        self.height = height

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height
