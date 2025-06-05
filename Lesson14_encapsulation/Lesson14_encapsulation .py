'''
Инкапсуляция, атрибуты и свойства
'''


class Person:
    def __init__(self, name, age):
        self.name = name    # устанавливаем имя
        self.age = age      # устанавливаем возраст

    def print_person(self):
        print(f"Name: {self.name}\t Age: {self.age}")


tom = Person("Tom", 39)
tom.name = "SpiderMan"       # изменяем атрибут name
tom.age = -129                  # изменяем атрибут age
tom.print_person()              # Имя: Человек-паук     Возраст: -129


class Person:
    def __init__(self, name, age):
        self.__name = name    # устанавливаем имя
        self.__age = age       # устанавливаем возраст

    def print_person(self):
        print(f"Name: {self.__name}\t Age: {self.__age}")


# _ClassName__atribute  self._Person__age
tom = Person("Tom", 39)
tom.__name = "Человек-паук"     # пытаемся изменить атрибут __name
tom._Person__age = -129                # пытаемся изменить атрибут __
tom.print_person()              # Имя: Tom        Возраст: 39

#
print(tom.__age)

#


class Person:
    def __init__(self, name, age):
        self.__name = name    # устанавливаем имя
        self.__age = age       # устанавливаем возраст

    def print_person(self):
        print(f"Name: {self.__name}\tAge: {self.__age}")


tom = Person("Tom", 39)
tom._Person__name = "SpiderMan"     # изменяем атрибут __name
tom.print_person()              # Имя: Человек-паук        Возраст: 39

'''
Методы доступа. Геттеры и сеттеры
'''


class Person:
    def __init__(self, name, age):
        self.__name = name    # устанавливаем имя
        self.__age = age       # устанавливаем возраст

    # сеттер для установки возраста
    def set_age(self, age):
        if 0 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    # геттер для получения возраста
    def get_age(self):
        return self.__age

    # геттер для получения имени
    def get_name(self):
        return self.__name

    def print_person(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


tom = Person("Tom", 39)
tom.print_person()  # Имя: Tom  Возраст: 39
tom.set_age(-3486)  # Недопустимый возраст
tom.set_age(25)
tom.print_person()  # Имя: Tom  Возраст: 25

'''
 Аннотации свойств
'''


class Person:
    def __init__(self, name, age):
        self.__name = name    # устанавливаем имя
        self.__age = age       # устанавливаем возраст

    # свойство-геттер
    @property
    def age(self):
        return self.__age
    # свойство-сеттер

    @age.setter
    def age(self, age):
        if 0 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    @property
    def name(self):
        return self.__name

    def print_person(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


tom = Person("Tom", 39)
tom.print_person()  # Имя: Tom  Возраст: 39
tom.age = -3486     # Недопустимый возраст  (Обращение к сеттеру)
print(tom.age)      # 39 (Обращение к геттеру)
tom.age = 25        # (Обращение к сеттеру)
tom.print_person()  # Имя: Tom  Возраст: 25

'''
Наследование. подкласс и суперкласс

class подкласс (суперкласс):
    методы_подкласса
'''


class Person:

    def __init__(self, name):
        self.__name = name   # имя человека

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name} ")


class Employee(Person):

    def work(self):
        print(f"{self.name} works")


tom = Employee("Tom")
print(tom.name)     # Tom
tom.display_info()  # Name: Tom
tom.work()          # Tom works

# Множественное наследование

#  класс работника


class Employee:
    def work(self):
        print("Employee works")


#  класс студента
class Student:
    def study(self):
        print("Student studies")


# Наследование от классов Employee и Student
class WorkingStudent(Employee, Student):
    pass


# класс работающего студента
tom = WorkingStudent()
tom.work()      # Employee works
tom.study()     # Student studies

#


class Employee:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def work(self):
        print(f"{self.name} works")


class Student:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def study(self):
        print(f"{self.name} studies")


class WorkingStudent(Employee, Student):
    pass


tom = WorkingStudent("Tom")
tom.work()      # Tom works
tom.study()     # Tom studies

#


class Employee:
    def do(self):
        print("Employee works")


class Student:
    def do(self):
        print("Student studies")


# class WorkingStudent(Student,Employee):
class WorkingStudent(Student, Employee):
    pass


tom = WorkingStudent()
tom.do()     # ?

print(WorkingStudent.__mro__)
print(WorkingStudent.mro())

'''
Переопределение функционала базового класса
'''


class Person:

    def __init__(self, name):
        self.__name = name   # имя человека

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name} ")


class Employee(Person):

    def work(self):
        print(f"{self.name} works")

        #


class Person:

    def __init__(self, name):
        self.__name = name   # имя человека

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name}")


class Employee(Person):

    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def display_info(self):
        super().display_info()
        print(f"Company: {self.company}")

    def work(self):
        print(f"{self.name} works")


tom = Employee("Tom", "Microsoft")
tom.display_info()  # Name: Tom
# Company: Microsoft

'''
Проверка типа объекта 	
isinstance(object, type)
'''


class Person:

    def __init__(self, name):
        self.__name = name   # имя человека

    @property
    def name(self):
        return self.__name

    def do_nothing(self):
        print(f"{self.name} does nothing")


#  класс работника
class Employee(Person):

    def work(self):
        print(f"{self.name} works")


#  класс студента
class Student(Person):

    def study(self):
        print(f"{self.name} studies")


def act(person):
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Employee):
        person.work()
    elif isinstance(person, Person):
        person.do_nothing()


tom = Employee("Tom")
bob = Student("Bob")
sam = Person("Sam")

act(tom)    # Tom works
act(bob)    # Bob studies
act(sam)    # Sam does nothing

'''
Атрибуты классов и статические методы
'''


class Person:
    type = "Person"
    description = "Describes a person"


print(Person.type)          # Person
print(Person.description)   # Describes a person

Person.type = "Class Person"
print(Person.type)          # Class Person

#


class Person:
    type = "Person"

    def __init__(self, name):
        self.name = name


tom = Person("Tom")
bob = Person("Bob")
print(tom.type)     # Person
print(bob.type)     # Person

# изменим атрибут класса
Person.type = "Class Person"
print(tom.type)     # Class Person
print(bob.type)     # Class Person


#
class Person:
    default_name = "Undefined"

    def __init__(self, name):
        if name:
            self.name = name
        else:
            self.name = Person.default_name


tom = Person("Tom")
bob = Person("")
print(tom.name)  # Tom
print(bob.name)  # Undefined

#


class Person:
    name = "Undefined"

    def print_name(self):
        print(self.name)


tom = Person()
bob = Person()
tom.print_name()    # Undefined
bob.print_name()    # Undefined

bob.name = "Bob"
bob.print_name()    # Bob
tom.print_name()    # Undefined

tom = Person()
bob = Person()
tom.print_name()    # Undefined
bob.print_name()    # Undefined

Person.name = "Some Person"     # меняем значение атрибута класса
bob.name = "Bob"                # устанавливаем атрибут объекта
bob.print_name()    # Bob
tom.print_name()    # Some Person

'''
Статические методы
@staticmethod
'''


class Person:
    __type = "Person"

    @staticmethod
    def print_type():
        print(Person.__type)


Person.print_type()     # Person - обращение к статическому методу через имя класса

tom = Person()
tom.print_type()     # Person - обращение к статическому методу через имя объекта

#


class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod  # преобразует обычный метод в метод класса, аргумент cls - сам класс
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('.'))
        # про функцию map() читаем здесь -> https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-map/
        # про метод строки split() читаем здесь -> https://www.w3schools.com/python/ref_string_split.asp
        date1 = cls(day, month, year)
        return date1

    def string_to_db(self):
        return f'{self.year}-{self.month}-{self.day}'


date = Date.from_string('30.12.2020')
# date.string_to_db()
print(date.string_to_db())


class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('.'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        # не полный пример проверки валидности
        # и приведен чисто в учебных целях
        if date_as_string.count('.') == 2:
            day, month, year = map(int, date_as_string.split('.'))
            return day <= 31 and month <= 12 and year <= 3999

    def string_to_db(self):
        return f'{self.year}-{self.month}-{self.day}'


    # список строк с датами
dates = [
    '30.12.2020',
    '30-12-2020',
    '01.01.2021',
    '12.31.2020'
]

for string_date in dates:
    # проверяем валидность строки с датой
    if Date.is_date_valid(string_date):
        # если все нормально, то создаем
        # экземпляр из этой строки
        date = Date.from_string(string_date)
        # далее делаем, что-то с экземпляром
        string_to_db = date.string_to_db()
        print(string_to_db)
    else:
        print(f'Неправильная дата или формат строки с датой')

# 2020-12-30
# Неправильная дата или формат строки с датой
# 2020-1-1
# Неправильная дата или формат строки с датой

'''
Класс object. Строковое представление объекта
'''


class Person:
    def __init__(self, name, age):
        self.name = name  # устанавливаем имя
        self.age = age  # устанавливаем возраст

    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")


tom = Person("Tom", 23)
print(tom)


class Person:
    def __init__(self, name, age):
        self.name = name  # устанавливаем имя
        self.age = age  # устанавливаем возраст

    def display_info(self):
        print(self)
        # print(self.__str__())     # или так

    def __str__(self):
        return f"Name: {self.name}  Age: {self.age}"


tom = Person("Tom", 23)
print(tom)      # Name: Tom  Age: 23
tom.display_info()  # Name: Tom  Age: 23

'''
Перегрузка операторов operator 

Сложение a + b __add__(a, b) 1 + 1

Объединение seq1 + seq2 __concat__(seq1, seq2)

'''


class Counter:
    def __init__(self, value):
        self.value = value
    # переопределение оператора сложения

    def __add__(self, other):
        return Counter(self.value + other.value)


counter1 = Counter(5)
counter2 = Counter(15)
counter3 = counter1 + counter2
print(counter3.value)       # 20


#
class Counter:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Counter(self.value + other)


counter1 = Counter(5)
counter3 = counter1 + 6
counter3 = counter1.__add__(6)
a = 6
counter3 = a.__add__+counter1
print(counter3.value)       # 11

#


class Counter:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other


counter1 = Counter(5)
result = counter1 + 7
print(result)       # 12

# bool


class Counter:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return self.value > 0


def test(counter):
    if counter:
        print("Counter = True")
    else:
        print("Counter = False")


counter1 = Counter(3)
test(counter1)              # Counter = True

counter2 = Counter(-3)
test(counter2)              # Counter = False

#


class Counter:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return self.value > 0


counter1 = Counter(3)

while (counter1):
    print("Counter1: ", counter1.value)
    counter1.value -= 1

#


class Counter:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value


counter1 = Counter(1)
counter2 = Counter(2)

if counter1 > counter2:
    print("counter1 больше чем counter2")
elif counter1 < counter2:
    print("counter1 меньше чем counter2")
else:
    print("counter1 и counter2 равны")


#
