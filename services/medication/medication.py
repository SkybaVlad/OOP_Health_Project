

class Medication:
    def __init__(self, medication_name, medication_dosage):
        self.medication_name = None
        self.medication_dosage = None

    def get_medication_name(self):
        return self.medication_name

    def get_medication_dosage(self):
        return self.medication_dosage


class MedicationReminder:
    def __init__(self):
        self.dictionary = {}

    def add_to_journal_of_medication(self, medication_object: Medication, time_to_take_medication):
        if time_to_take_medication in self.dictionary.keys():
            self.dictionary[time_to_take_medication].append(medication_object)
        else:
            self.dictionary[medication_object.medication_name] = [time_to_take_medication]

    def delete_from_journal_of_medication(self, medication_object: Medication):
        pass