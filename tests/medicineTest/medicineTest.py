import unittest
from src.medicine.medicine import Medicine


class TestMedicine(unittest.TestCase):
    def test_init_method_with_valid_params(self):
        medicine = Medicine('Paracetamol', 1, 'once_a_day')
        self.assertEqual(medicine.name, 'Paracetamol')
        self.assertEqual(medicine.dosage, 1)
        self.assertEqual(medicine.frequency, 'once_a_day')
