class LimitCallsError(Exception):
    """This exception raised when limit of calling something is exhausted"""

    pass


class DateOfDayIsGreaterThanTodayError(Exception):
    pass


class NotExistingReceiptWithAppropriateMedicationObjectError(Exception):
    pass


class NotExistingDayInListOfDaysWithThisDateError(Exception):
    pass
