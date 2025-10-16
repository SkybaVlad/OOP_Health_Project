class PatientStatus:
    def __init__(self):
        self.is_sick = None
        self.disease_type = None

    def get_is_sick_status(self):
        return self.is_sick()

    def set_is_sick_status(self, is_sick_status):
        self.is_sick = is_sick_status

    def get_disease_type(self):
        return self.disease_type

    def set_disease_type(self, disease_name):
        self.disease_type = disease_name
