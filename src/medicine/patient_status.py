class PatientStatus:
    def __init__(self, is_sick, disease_type):
        self.is_sick = is_sick
        self.disease_type = disease_type

    def get_is_sick_status(self):
        return self.is_sick()

    def set_is_sick_status(self, value):
        self.is_sick = value
