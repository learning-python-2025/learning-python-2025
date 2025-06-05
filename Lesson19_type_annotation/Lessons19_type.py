"""
Аннотации
https://mypy.readthedocs.io/en/stable/getting_started.html
python -m pip install mypy

mypy program.py
"""


def greeting(name):
    return 'Hello ' + name


def greeting(name):
    return 'Hello ' + name


# These calls will fail when the program runs, but mypy does not report an error
# because "greeting" does not have type annotations.
greeting(123)
greeting(b"Alice")


def greeting(name: str) -> str:
    return 'Hello ' + name


def greeting(name):
    return 'Hello ' + name


# These calls will fail when the program runs, but mypy does not report an error
# because "greeting" does not have type annotations.
greeting(123)
greeting(b"Alice")
greeting("Alice")

#


def normalize_id(user_id: int | str) -> str:
    if isinstance(user_id, str):
        return user_id
    return f'user-{user_id:05d}'


normalize_id("user-123")
normalize_id(123)
normalize_id("1")

#


def greet(name: str) -> None:
    print("Hello", name)


greet("John")

greet(45)

#


def greet(name: str) -> str:
    print("Hello", name)
    return name


greet("John")

greet(45)
#


def square(num: int | float) -> float:
    return num*num


sq = square(5)
print(sq)

#
# from typing import TypeVar, reveal_type

IntOrFloat = TypeVar("IntOrFloat", float, int)


def square(num: IntOrFloat) -> IntOrFloat:
    return num*num


sq = square(5)
reveal_type(sq)
sq = square(5.5)
reveal_type(sq)
print(sq)

#
# from functools import wraps
# from typing import TypeVar, reveal_type, Sized, Callable, ParamSpec
IntOrFloat = TypeVar("IntOrFloat", float, int)
ReturnType = TypeVar("ReturnType")
P = ParamSpec("P")


def announced(func: Callable[P, ReturnType]) -> Callable[P, ReturnType]:
    print("creating announced function", func)

    @wraps(func)
    def new_announced(*args: P.args, **kwargs: P.kwargs) -> ReturnType:
        print("run function", func)
        result = func(*args, **kwargs)
        print("done function", func, "res:", result)
        return result
    print("successfully created announced function for",
          func, "announced:", new_announced)
    return new_announced


@announced
def square(num: IntOrFloat) -> IntOrFloat:
    return num*num


@announced
def cube(num: IntOrFloat) -> IntOrFloat:
    return num**3


@announced
def power(num: IntOrFloat, exponent: int) -> IntOrFloat:
    val: IntOrFloat = num**exponent
    return val


@announced
def many_str(line: str, times: int) -> str:
    return line*times


@announced
def get_size(obj: Sized) -> int:
    return len(obj)


s = square(5)
reveal_type(s)
print(s)
c = cube(3.5)
reveal_type(c)
print(c)
p = power(2, 10)
print(p)
reveal_type(p)

line = many_str("foobar", 3)
reveal_type(line)
print(line)
gs = get_size({"a", "b"})
reveal_type(gs)
print(gs)
