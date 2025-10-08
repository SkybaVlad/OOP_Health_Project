class PatientStatus:
    def __init__(self, is_sick, disease_type):
        self.is_sick = is_sick
        self.disease_type = disease_type

    def is_sick(self):
        return self.is_sick()