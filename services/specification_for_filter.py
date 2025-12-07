from abc import ABC, abstractmethod
from services.health_daily.daily_health import HealthDaily
from services.time_logic import time_in_period

"""In this file describes a pattern called Specification that can be used as condition for 
complex filtration of data."""


class Specification(ABC):
    """This class provide an abstractmethod for children classes"""

    @abstractmethod
    def is_satisfy_by(self, candidate) -> bool:
        pass


class SpecificDaySpecification(Specification):
    """This class provide a condition that find a specific day using a date condition.
    The date attribute has the next format YYYY-MM-DD and string type"""

    def __init__(self, date):
        self.date = date

    def is_satisfy_by(self, day: HealthDaily) -> bool:
        return self.date == day.date_of_day


class PeriodSpecification(Specification):
    """This class provide a condition that ensures that date of day entered
    in specified period of time. Start period of time and end period of time have the next format
    YYYY-MM-DD and string type. In this class used a time in period function from time_logic
    module that doing a comparison and ensures that date of day entered in specified period
    """

    def __init__(self, start_period_time: str, end_period_time: str) -> None:
        self.start_period_time = start_period_time
        self.end_period_time = end_period_time

    def is_satisfy_by(self, day: HealthDaily) -> bool:
        return time_in_period(
            self.start_period_time, self.end_period_time, day.date_of_day
        )


class ActivitySpecification(Specification):
    """This class provide a condition that ensures that HealthDaily object has any activity"""

    def __init__(self, activity_category):
        self.activity_category = activity_category

    def is_satisfy_by(self, day: HealthDaily) -> bool:
        return len(day.list_of_activities_for_day) != 0


class ActivityCategorySpecification(Specification):
    """This class provide a condition that ensures that HealthDaily object has at least one
    activity with specified category"""

    def __init__(self, activity_category):
        self.activity_category = activity_category

    def is_satisfy_by(self, day: HealthDaily) -> bool:
        for activity in day.list_of_activities_for_day:
            if activity.get_activity_category() == self.activity_category:
                return True
        return False


class ActivityNameCategory(Specification):
    """This class provide a condition that ensures that HealthDaily object has at least
    one activity with specified name"""

    def __init__(self, activity_name):
        self.activity_name = activity_name

    def is_satisfy_by(self, day: HealthDaily) -> bool:
        for activity in day.list_of_activities_for_day:
            if activity.get_name_of_specific_activity() == self.activity_name:
                return True
        return False


class GreaterBurnedCaloriesValueSpecification(Specification):
    """This class provide a condition that ensures that HealthDaily object
    has burned_calories value that greater than provided value"""

    def __init__(self, value):
        self.value = value

    def is_satisfy_by(self, day: HealthDaily) -> bool:
        if day.burned_calories_for_day > self.value:
            return True
        return False


class LesserBurnedCaloriesValueSpecification(Specification):
    """This class provide a condition that ensures that HealthDaily object
    has burned_calories value that less than provided value"""

    def __init__(self, value):
        self.value = value

    def is_satisfy_by(self, day: HealthDaily) -> bool:
        if day.burned_calories_for_day < self.value:
            return True
        return False


class GreaterDrunkWaterValueSpecification(Specification):
    """This class provide a condition that ensures that HealthDaily object
    has drunk_water value that greater than provided value"""

    def __init__(self, value):
        self.value = value

    def is_satisfy_by(self, day: HealthDaily) -> bool:
        if day.drunk_water > self.value:
            return True
        return False


class LesserDrunkWaterValueSpecification(Specification):
    """This class provide a condition that ensures that HealthDaily object
    has drunk_water value that lesser than provided value"""

    def __init__(self, value):
        self.value = value

    def is_satisfy_by(self, day: HealthDaily) -> bool:
        if day.drunk_water < self.value:
            return True
        return False


class GreaterSleepDurationSpecification(Specification):
    """This class provide a condition that ensures that HealthDaily object
    has sleep duration value that greater than provided value"""

    def __init__(self, value):
        self.value = value

    def is_satisfy_by(self, day: HealthDaily) -> bool:
        if day.sleep_duration > self.value:
            return True
        return False


class LesserSleepDurationSpecification(Specification):
    """This class provide a condition that ensures that HealthDaily object
    has sleep duration value that lesser than provided value"""

    def __init__(self, value):
        self.value = value

    def is_satisfy_by(self, day: HealthDaily) -> bool:
        if day.sleep_duration < self.value:
            return True
        return False


class ANDSpecification(Specification):
    """This class gets two Specification objects and provide condition that ensures that two object
    satisfy simultaneously. This can be doing by and operator"""

    def __init__(
        self, first_spec_object: Specification, second_spec_object: Specification
    ):
        self.first_spec_object = first_spec_object
        self.second_spec_object = second_spec_object

    def is_satisfy_by(self, day: HealthDaily) -> bool:
        return self.first_spec_object.is_satisfy_by(
            day
        ) and self.second_spec_object.is_satisfy_by(day)


class ORSpecification(Specification):
    """This class gets two Specification objects and provide condition that ensures that two object
    satisfy simultaneously or one of the objects satisfy a specified condition. This can be doing by or operator
    """

    def __init__(
        self, first_spec_object: Specification, second_spec_object: Specification
    ):
        self.first_spec_object = first_spec_object
        self.second_spec_object = second_spec_object

    def is_satisfy_by(self, day: HealthDaily) -> bool:
        return self.first_spec_object.is_satisfy_by(
            day
        ) or self.second_spec_object.is_satisfy_by(day)
