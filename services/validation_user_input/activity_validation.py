def validate_activity_name(name: str):
    if not isinstance(name, str):
        raise TypeError('Activity name must be a string. ')
    if len(name) < 3:
        raise ValueError('Activity name must contain at least 3 characters')
    if 'a' <= name[0] <= 'z':
        raise ValueError('Surname must start with upper case letter')
    for ch in name:
        if not ch.isalpha():
            raise ValueError('Activity name must contain only letters')
    with open(
        "C:/Users/user/PycharmProjects/OOP_Health_Project/services/activities/activity_names.txt",
        "r",
    ) as file:
        for line in file:
            line = line.rstrip("\n").rstrip(",")
            if line == name:
                return True
    raise ValueError('Activity name not found')


def validate_burned_calories(burned_calories: int):
    if not isinstance(burned_calories, int):
        raise TypeError('Burned calories must be integer')
    if burned_calories < 0:
        raise ValueError('Burned calories must be positive')
    return True


def validate_activity_category(activity_category: str):
    pass


if __name__ == '__main__':
    print(validate_activity_name("Football"))
