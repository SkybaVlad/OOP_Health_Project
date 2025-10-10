class Examination:
    def __init__(self, examination_type, date, result):
        self.examination_type = examination_type
        self.date = date
        self.result = result

    def return_result_of_examination(self):
        return self.result

