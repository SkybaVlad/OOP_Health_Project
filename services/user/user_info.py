class User:

    __user_instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__user_instance is None:
            cls.__user_instance = super().__new__(cls)
        return cls.__user_instance

    def __init__(self, name, surname, age, sex):
        if not hasattr(self, 'initialized'):
            self.__name = name
            self.__surname = surname
            self.__age = age
            self.__sex = sex
            self.initialized = True

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

    def __repr__(self):
        return f"User(name={self.__name}, surname={self.__surname}, age={self.__age}, sex={self.__sex})"


user = User("Vlad", "Skyba", 19, "male")
user1 = User("Maks", "Gan", 18, "female")
print(id(user))
print(id(user1))
print(user)
print(user1)
