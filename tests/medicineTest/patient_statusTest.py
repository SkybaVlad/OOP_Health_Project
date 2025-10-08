import unittest
from src.medicine.patient_status import PatientStatus


class TestMedicine(unittest.TestCase):
    def test_init_method_with_valid_params(self):
        patient_status_obj = PatientStatus(True, 'Covid-19')
        self.assertEqual(patient_status_obj.is_sick, True)
        self.assertEqual(patient_status_obj.disease_type, 'Covid-19')
