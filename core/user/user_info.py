from core.validation_user_input.user_info_validation import (
    validate_age,
    validate_user_name,
    validate_sex,
    validate_surname,
)


class User:

    def __init__(self, name: str, surname: str, age: int, sex: str):
        try:
            validate_user_name(name)
            validate_surname(surname)
            validate_age(age)
            validate_sex(sex)
        except ValueError as error:
            pass
        except TypeError as error:
            pass
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__sex = sex

    def get_name(self) -> str:
        return self.__name

    def get_surname(self) -> str:
        return self.__surname

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_sex(self) -> str:
        return self.__sex

    def __repr__(self):
        return f"User(name={self.__name}, surname={self.__surname}, age={self.__age}, sex={self.__sex})"
