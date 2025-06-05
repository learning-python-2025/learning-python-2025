'''
class название_класса:
    атрибуты_класса
    методы_класса
'''


class Person:
    pass


tom = Person()      # определение объекта tom
bob = Person()      # определение объекта bob

tom = Person()      # Person() - вызов конструктора, который возвращает объект класса Person

#


class Person:
    # конструктор
    def __init__(self):
        print("Создание объекта Person")


tom = Person()      # Создание объекта Person
#


class Person:

    def __init__(self, name, age):
        self.name = name    # имя человека
        self.age = age        # возраст человека


tom = Person("Tom", 22)

# обращение к атрибутам
# получение значений
print(tom.name)     # Tom
print(tom.age)      # 22
# изменение значения
tom.age = 37
print(tom.age)      # 37

bob = Person("Bob", 43)
print(tom.name)         # Tom
print(bob.name)         # Bob


#
class Person:

    def __init__(self, name, age):
        self.name = name        # имя человека
        self.age = age          # возраст человека


tom = Person("Tom", 22)

tom.company = "Microsoft"
print(tom.company)  # Microsoft

#
tom = Person("Tom", 22)
# ! Ошибка - AttributeError: Person object has no attribute company
print(tom.company)


#  Методы классов объект.метод([параметры метода])

class Person:       # определение класса Person
    def say_hello(self):
        print("Hello")


tom = Person()
tom.say_hello()    # Hello

#


class Person:       # определение класса Person
    def say(self, message):     # метод
        print(message)


tom = Person()
tom.say("Hello METANIT.COM")    # Hello METANIT.COM

# self.атрибут    # обращение к атрибуту
# self.метод      # обращение к методу


class Person:

    def __init__(self, name, age):
        self.name = name        # имя человека
        self.age = age          # возраст человека

    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")


tom = Person("Tom", 22)
tom.display_info()      # Name: Tom  Age: 22

bob = Person("Bob", 43)
bob.display_info()      # Name: Bob  Age: 43

# деструкторы __del__(self)


class Person:

    def __init__(self, name):
        self.name = name
        print("Create Person", self.name)

    def __del__(self):
        print("Delete Person", self.name)


tom = Person("Tom")

#


class Person:

    def __init__(self, name):
        self.name = name
        print("Create Person with name", self.name)

    def __del__(self):
        print("Delete Person with name", self.name)


def create_person():
    tom = Person("Tom")


create_person()
print("End")
