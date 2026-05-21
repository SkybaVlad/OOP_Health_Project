from pathlib import Path


def validate_activity_name(name: str):
    if not isinstance(name, str):
        raise TypeError("Activity name must be a string.")

    if len(name) < 3:
        raise ValueError("Activity name must contain at least 3 characters")

    if "a" <= name[0] <= "z":
        raise ValueError("Activity name must start with upper case letter")

    for ch in name:
        if not ch.isalpha() and ch != " ":
            raise ValueError("Activity name must contain only letters and spaces")

    activity_names_file = Path(__file__).resolve().parent.parent / "activity" / "activity_names.txt"

    with open(activity_names_file, "r") as file:
        for line in file:
            line = line.rstrip("\n").rstrip(",")
            if line == name:
                return True

    raise ValueError("Activity name not found")


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
