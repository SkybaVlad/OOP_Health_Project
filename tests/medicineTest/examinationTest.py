import unittest
from src.medicine.examination import Examination


class TestExamination(unittest.TestCase):
    def test_examination_init_method(self):
        examination_obj = Examination('Physical', '03/05/2025', True)
        self.assertEqual(examination_obj.examination_type, 'Physical')
        self.assertEqual(examination_obj.date, '03/05/2025')
        self.assertEqual(examination_obj.result, True)


if __name__ == '__main__':
    unittest.main()
