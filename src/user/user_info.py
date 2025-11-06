class User:
    def __init__(self, name, surname, age, sex):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__sex = sex

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_sex(self):
        return self.__sex
