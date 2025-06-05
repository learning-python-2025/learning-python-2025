"""
Аннотации
https://mypy.readthedocs.io/en/stable/getting_started.html
python -m pip install mypy

mypy program.py
"""

# Присваивание разных типов данных одной и той же переменной:
from typing import TypeVar, List
from typing import Optional, List, Dict, Tuple
from typing import TypeVar
from typing import Optional
from typing import TypeVar, List, Tuple
from typing import List, Type
from typing import List, Tuple
import asyncio
from typing import Optional, AsyncIterator
from typing import NewType
from typing import Sequence, TypeVar
import random
from typing import List, Dict, Tuple
from typing import List, Dict, Union, Optional, List
import numpy as np
from typing import Any
from typing import Protocol
from typing import List
from typing import List, Dict
from typing import Union
var = 10      # var - это целое число (int)
print(type(var))  # Вывод: <class 'int'>

var = 10.5    # Теперь var - это число с плавающей точкой (float)
print(type(var))  # Вывод: <class 'float'>

var = "Hello"  # Теперь var - это строка (str)
print(type(var))  # Вывод: <class 'str'>

# Использование переменных без явного указания типа:
a = 5
b = "world"
c = [1, 2, 3]

print(type(a))  # Вывод: <class 'int'>
print(type(b))  # Вывод: <class 'str'>
print(type(c))  # Вывод: <class 'list'>

# Функции с динамической типизацией:


def add(x, y):
    return x + y


print(add(5, True))        # Вывод: 15 (сложение целых чисел)
print(add("Hello, ", 5))  # Вывод: Hello, world! (конкатенация строк)

# Изменение типа переменной в процессе выполнения программы:
value = 42
print(type(value))  # Вывод: <class 'int'>

value = "Python"
print(type(value))  # Вывод: <class 'str'>


def greet(name: str) -> str:
    return f"Hello, {name}!"


print(greet("Alice"))  # Вывод: Hello, Alice!

# Использование динамической типизации с функциями высшего порядка:


def apply_function(func, value):
    return func(value)


def square(x):
    return x * x


def to_upper(s):
    return s.upper()


result1 = apply_function(square, 5)
print(result1)  # Вывод: 25

result2 = apply_function(to_upper, "hello")
print(result2)  # Вывод: HELLO

# Использование динамической типизации с классами и объектами:


class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


def make_animal_speak(animal: Animal):
    return animal.speak()


dog = Dog()
cat = Cat()

print(make_animal_speak(dog))  # Вывод: Woof!
print(make_animal_speak(cat))  # Вывод: Meow!

# Использование динамической типизации с декораторами:


def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args}, {kwargs}) -> {result}")
        return result
    return wrapper


@debug
def add(a, b):
    return a + b


@debug
def greet(name):
    return f"Hello, {name}!"


add_result = add(a=3, b=4)  # Вывод: add((3, 4), {}) -> 7
greet_result = greet("Alice")  # Вывод: greet(('Alice',), {}) -> Hello, Alice!

# Использование динамической типизации с обработкой исключений:


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    except TypeError:
        return "Both arguments must be numbers"


print(safe_divide(10, 2))    # Вывод: 5.0
print(safe_divide(10, 0))    # Вывод: Division by zero is not allowed
print(safe_divide(10, "a"))  # Вывод: Both arguments must be numbers

# Использование динамической типизации с аннотациями типов и проверкой типов во время выполнения:


def process_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Processed integer: {value * 2}"
    elif isinstance(value, str):
        return f"Processed string: {value.upper()}"
    else:
        return "Unsupported type"


print(process_value(5))     # Вывод: Processed integer: 10
print(process_value("hello"))  # Вывод: Processed string: HELLO
print(process_value([1, 2, 3]))  # Вывод: Unsupported type


# Модуль typing


def process_items(items: List[int]) -> Dict[str, int]:
    result = {}
    for item in items:
        result[str(item)] = item * 2
    return result


print(process_items([1, 2, 3,]))

# Пример комплексного использования аннотаций и mypy


def greet(names: List[str]) -> None:
    for name in names:
        print(f"Hello, {name}!")


if __name__ == "__main__":
    greet(["Alice", "Bob", "Charlie"])

# Пример утиная типизация в Python


class Duck:
    def quack(self):
        print("Quack!")


class Person():
    def quack(self):
        print("I'm quacking like a duck!")


def make_it_quack(duck_like):
    duck_like.quack()


duck = Duck()
person = Person()

make_it_quack(duck)   # Quack!
make_it_quack(person)  # I'm quacking like a duck!

# Проверка наличия метода


def make_it_quack(duck_like):
    if hasattr(duck_like, 'quack'):
        duck_like.quack()
    else:
        raise TypeError("Object does not have method 'quack'")


duck = Duck()
person = Person()

make_it_quack(duck)   # Quack!
make_it_quack(person)  # I'm quacking like a duck!

# Subtype relationships Подтипы в Python
# Пример с наследованием:


class Animal:
    pass


class Dog(Animal):
    pass


first_var = Dog()
second_var = Animal()

# Присвоение допустимо, так как Dog является подтипом Animal
second_var = first_var

# Номинальное подтипирование (nominal subtyping)
# Базовый класс (суперкласс)


class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

# Подкласс (подтип), наследующий от Animal


class Dog(Animal):
    def speak(self):
        return "Woof!"

# Подкласс (подтип), наследующий от Animal


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Создаем объекты подклассов
dog = Dog()
cat = Cat()

# Пример использования номинального подтипирования


def make_animal_speak(animal: Animal):
    print(animal.speak())


# Поскольку Dog и Cat являются подтипами Animal,
# мы можем передавать их объекты в функцию make_animal_speak
make_animal_speak(dog)  # Вывод: Woof!
make_animal_speak(cat)  # Вывод: Meow!

# демонстрирует использование аннотаций типов, наследования и создание пользовательского подтип


def add(x: int, y: int) -> int:
    return x + y
# Эта функция принимает два аргумента x и y, которые должны быть целыми числами (тип int).
# Функция возвращает сумму этих двух аргументов, также тип int.


class Count(int):
    def __add__():


Count(1)

# Здесь создается новый класс Count, который наследует от встроенного класса int.
# Это означает, что Count является подтипом int и унаследует все его свойства и методы.
# Класс Count не добавляет никакого нового поведения или атрибутов к базовому классу int, он просто наследует его.
print(add(Count(1), Count(1)))
# Вызов функции add с объектами класса Count


# structural subtyping - основывается на структуре объекта и объявленных методах

# Определение протокола


class Drawable(Protocol):
    def draw(self) -> None:
        ...

# Реализация классов, соответствующих протоколу


class Circle:
    def draw(self) -> None:
        print("Drawing a circle")


class Square:
    def draw(self) -> None:
        print("Drawing a square")

# Функция, принимающая объекты, соответствующие протоколу


def render(shape: Drawable) -> None:
    shape.draw()


# Использование функции с разными типами объектов
circle = Circle()
square = Square()

render(circle)  # Output: Drawing a circle
render(square)  # Output: Drawing a square

# 2 демонстрирует использование протоколов в Python для определения структурного подтипирования
# Импорт модуля Protocol из typing
# Модуль Protocol используется для определения протоколов в Python.
# Протоколы позволяют определить набор методов, которые должны быть реализованы классом, чтобы он соответствовал этому протоколу.


class Sized(Protocol):
    def __len__(self) -> int: ...

# Протокол Sized определяет один метод __len__, который должен возвращать целое число (int).
# Этот протокол говорит о том, что любой класс, который реализует метод __len__, соответствует этому протоколу.


def len(obj: Sized) -> int:
    return obj.__len__()

# Функция len принимает объект obj, который соответствует протоколу Sized.
# Это означает, что объект должен иметь метод __len__, который возвращает целое число.
# Внутри функции вызывается метод __len__ объекта и возвращается его результат.


# 3
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self) -> int:
        return len(self.items)


my_list = MyList([1, 2, 3])
print(len(my_list))  # Output: 3

# Gradual typing

# 1


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def main():
    a = 5
    b = 10
    print("Addition:", add(a, b))
    print("Multiplication:", multiply(a, b))


if __name__ == "__main__":
    main()

# 2


def add(x: int, y: int) -> int:
    return x + y


def multiply(x: int, y: int) -> int:
    return x * y


def main() -> None:
    a: int = 5
    b: int = 10
    print("Addition:", add(a, b))
    print("Multiplication:", multiply(a, b))


if __name__ == "__main__":
    main()

# 3 mypy example.py

# Концепции "is-subtype-of" и "is-consistent-with"
# Подтипы (Subtypes)


class Animal:
    pass


class Dog(Animal):
    pass

# Dog is a subtype of Animal


# Консистентность типов (Consistency)


def func(x: Any) -> int:
    return 42


a: int = 10
b: Any = "hello"

# int is consistent with Any and vice versa

# Специальный тип Any
# 1 Консистентность типов


def process_data(data: Any) -> None:
    print(data)


data_str: str = "Hello"
data_int: int = 123

process_data(data_str)  # str is consistent with Any
process_data(data_int)  # int is consistent with Any

# 2 Подтипы и консистентность


class Animal:
    pass


class Dog(Animal):
    pass


def show_animal(animal: Animal) -> None:
    print("This is an animal")


dog: Dog = Dog()
show_animal(dog)  # Dog is a subtype of Animal

any_value: Any = "Random String"
show_animal(any_value)  # Any is consistent with Animal


hello: str = "helloWorld"
helloBytes: bytes = b'helloWorld'
nth: int = 2
xth: float = 2.0
abool: bool = True
randomValues: list = ['Foo', 99, 3.1415912]
signalFrequency: dict = {'low': 10, 'high': 700, 'unit': 'Mhertz'}
low_numbers: set = set(['one', 'two', 'three'])
high_numbers: frozenset = frozenset(['97', '98', '99'])

# 1 Функция с несколькими аргументами


def greet(name: str) -> str:
    return f"Hello, {name}!"

# 2 Функция с аргументами по умолчанию


def add(a: int, b: int) -> int:
    return a + b


# 3 Функция с произвольным количеством аргументов


def concatenate(*args: str) -> str:
    return ' '.join(args)

# 4 Функция с именованными аргументами


def display_info(name: str, age: int, city: str = "Unknown") -> str:
    return f"{name}, {age} years old, lives in {city}."

# 5 Функция с аннотацией типа для возвращаемого значения None


def print_message(message: str) -> None:
    print(message)

# 6 Пример функции с использованием кастомного типа


Vector = List[float]


def dot_product(v1: Vector, v2: Vector) -> float:
    return sum(x * y for x, y in zip(v1, v2))

#


def count_vowels(x: str, include_y: bool = False) -> int:
    """Returns the number of vowels contained in `in_string`"""
    vowels = set("aeiouAEIOU")
    if include_y:
        vowels.update("yY")
    return sum(1 for char in x if char in vowels)

# Classes are types Реализация классов и использование их в аннотациях


class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"User(name={self.name}, age={self.age})"


class Admin(User):
    def __init__(self, name: str, age: int, permissions: list[str]) -> None:
        super().__init__(name, age)
        self.permissions = permissions

    def __repr__(self) -> str:
        return f"Admin(name={self.name}, age={self.age}, permissions={self.permissions})"


def create_user(name: str, age: int) -> User:
    return User(name, age)


def create_admin(name: str, age: int, permissions: List[str]) -> Admin:
    return Admin(name, age, permissions)


def print_user_info(user: User) -> None:
    print(f"User Info: {user}")


def print_admin_info(admin: Admin) -> None:
    print(f"Admin Info: {admin}")


if __name__ == "__main__":
    user = create_user("Alice", 30)
    admin = create_admin("Bob", 35, ["read", "write", "execute"])

    print_user_info(user)
    print_admin_info(admin)


def custom_dot_product(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.sum(x * y))


class Dog:
    def __init__(self, name):
        self.name = name

# cls is expected to be the class-object, `Dog`, itself
# This function returns a list of instances of the `Dog` type


def list_famous_dogs(cls: Type[Dog]) -> List[Dog]:
    return [cls(name) for name in ["Lassie", "Shadow", "Air Bud"]]


# Type Aliases  псевдонимы типов
StandardRow = Tuple[str, int,]
SpecialRow = Tuple[int, str]
ItemRow = Union[StandardRow, SpecialRow]
ItemMapping = Dict[str, List[ItemRow]]


def fetch_row_map(id: int) -> Optional[ItemMapping]:
    ...


# Пример кода с использованием Type Aliases
# Определяем псевдонимы типов
StudentName = str
Grade = float
GradesList = List[Grade]
GradeBook = Dict[StudentName, GradesList]

# Функция для вычисления среднего значения оценок студента


def compute_average(grades: GradesList) -> Grade:
    return sum(grades) / len(grades)

# Функция для вычисления статистики по оценкам студентов


def compute_student_stats(grade_book: GradeBook) -> List[Tuple[StudentName, Grade]]:
    stats = []
    for student, grades in grade_book.items():
        average_grade = compute_average(grades)
        stats.append((student, average_grade))
    return stats


# Пример словаря с оценками студентов
grade_book: GradeBook = {
    "Alice": [90.0, 85.0, 92.0],
    "Bob": [78.0, 81.0, 74.0],
    "Charlie": [88.0, 90.0, 85.0]
}

# Вычисление статистики по оценкам студентов
student_stats = compute_student_stats(grade_book)
print("Статистика студентов:", student_stats)


# Type Variables (переменные типов)
Choosable = TypeVar("Choosable", str, float)


def choose(items: Sequence[Choosable]) -> Choosable:
    return random.choice(items)

#


# Определяем переменную типа
T = TypeVar('T')

# Обобщенная функция для нахождения максимального значения в списке


def find_max(items: List[T]) -> T:
    if not items:
        raise ValueError("The list is empty")
    max_item = items[0]
    for item in items[1:]:
        if item > max_item:
            max_item = item
    return max_item


# Пример использования функции с различными типами данных
int_list: List[int] = [1, 2, 3, 4, 5]
str_list: List[str] = ["apple", "banana", "cherry"]

max_int = find_max(int_list)
max_str = find_max(str_list)

print(f"Максимальное значение в списке целых чисел: {max_int}")
print(f"Максимальное значение в списке строк: {max_str}")

# Обобщенная функция для создания кортежа из двух элементов


def make_pair(first: T, second: T) -> Tuple[T, T]:
    return first, second


# Пример использования функции с различными типами данных
int_pair = make_pair(1, 2)
str_pair = make_pair("hello", "world")

print(f"Пара целых чисел: {int_pair}")
print(f"Пара строк: {str_pair}")


# New types

Circle = NewType('Circle', int)


def get_shape(circle_: Circle) -> str:
    ...


# typechecks
get_shape(Circle(42351))
# typecheck error fault; an int is not a Circle
get_shape(999)

#


# Создаем новый тип UserId, который на самом деле является int
UserId = NewType('UserId', int)

# Создаем новый тип Username, который на самом деле является str
Username = NewType('Username', str)

# Функция, которая принимает UserId и возвращает строку


def get_user_name(user_id: UserId) -> Username:
    # В реальном приложении здесь мог бы быть запрос к базе данных
    # Для простоты вернем строку, содержащую user_id
    return Username(f"User_{user_id}")

# Функция, которая принимает Username и выводит приветствие


def greet_user(username: Username) -> None:
    print(f"Hello, {username}!")


# Пример использования новых типов
user_id = UserId(1234)
username = get_user_name(user_id)

greet_user(username)

# Попытка передать неправильный тип вызовет ошибку на этапе проверки типов
# Например, следующая строка будет помечена как ошибка статическими анализаторами типов (например, mypy):
# greet_user(user_id)  # Ошибка: ожидается Username, а передан UserId


# Type checkers

# Static
# mypy https://github.com/python/mypy
# pyre https://github.com/facebook/pyre-check
# pyright https://github.com/microsoft/pyright
# pytype https://github.com/google/pytype

# Dynamic
# pydantic https://github.com/samuelcolvin/pydantic
# beartype https://github.com/beartype/beartype
# pysa https://engineering.fb.com/2020/08/07/security/pysa/
# References


# PEP 483 The Theory of Type Hints: https://www.python.org/dev/peps/pep-0483/
# Tutorial: https://realpython.com/python-type-checking/
# Cheat Sheet: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
# Mypy to Python C Extension Compiler: https://github.com/python/mypy/tree/master/mypyc
# MonkeyType generates static type annotations by collecting runtime types: https://github.com/instagram/MonkeyType

# использование асинхронного итератора в Python для создания обратного отсчет


class arange(AsyncIterator[int]):
    def __init__(self, start: int, stop: int, step: int) -> None:
        self.start = start
        self.stop = stop
        self.step = step
        self.count = start - step

    def __aiter__(self) -> AsyncIterator[int]:
        return self

    async def __anext__(self) -> int:
        self.count += self.step
        if self.count == self.stop:
            raise StopAsyncIteration
        else:
            return self.count


async def countdown_4(tag: str, n: int) -> str:
    async for i in arange(n, 0, -1):
        print('T-minus {} ({})'.format(i, tag))
        await asyncio.sleep(0.1)
    return "Blastoff!"


# использования asyncio для выполнения нескольких асинхронных задач:

# Определяем асинхронную функцию

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)

# Главная асинхронная функция


async def main():
    # Запускаем две задачи параллельно
    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(2, "World"))

    print("Started tasks")

    # Ждем завершения обеих задач
    await task1
    await task2

    print("Finished tasks")

# Запускаем главный цикл событий
asyncio.run(main())
