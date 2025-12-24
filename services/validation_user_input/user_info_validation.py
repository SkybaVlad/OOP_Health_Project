def validate_user_name(name: str) -> bool:
    """This function validates the users names.
    Name of user should be a string type a has the next formal 'Vlad'
    First letter must be the upper case letter. All char must be in English alphabet"""
    if not isinstance(name, str):
        raise TypeError('Name must be a string type')
    if len(name) < 3 or len(name) > 15:
        raise ValueError('Name must be between 3 and 15 characters')
    if name[0] >= 'a' or name[0] <= 'z':
        raise ValueError('Name must start with upper case letter')
    for char in name:
        if not char.isalpha():
            raise ValueError('Name must contain only letters')
    return True


def validate_surname(surname: str):
    if not isinstance(surname, str):
        raise TypeError('Surname must be a string type')
    if len(surname) < 3 or len(surname) > 15:
        raise ValueError('Surname must be between 3 and 15 characters')
    if surname[0] >= 'a' or surname[0] <= 'z':
        raise ValueError('Surname must start with upper case letter')
    for char in surname:
        if not char.isalpha():
            raise ValueError('Surname must contain only letters')
    return True


def validate_age(age: int):
    if not isinstance(age, int):
        raise TypeError('Age must be an integer type')
    if age < 0 or age > 100:
        raise ValueError('Age value must be between 0 and 100')
    return True


def validate_sex(user_sex: str):
    if not isinstance(user_sex, str):
        raise TypeError("User_sex value must be a string type")
    if user_sex != 'Male' or 'Female':
        raise ValueError("User_sex value must be 'Male' or 'Female'")
    return True
