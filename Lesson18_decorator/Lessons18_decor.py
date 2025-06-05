# определение функции декоратора
def select(input_func):
    def output_func():      # определяем функцию, которая будет выполняться вместо оригинальной
        # перед выводом оригинальной функции выводим всякую звездочки
        print("*****************")
        input_func()                # вызов оригинальной функции
        # после вывода оригинальной функции выводим всякую звездочки
        print("*****************")
    return output_func     # возвращаем новую функцию


# определение оригинальной функции
@select         # применение декоратора select
def hello():
    print("Hello World!")


# вызов оригинальной функции
hello()


# определение функции декоратора
def check(input_func):
    def output_func(*args):      # через *args получаем значения параметров оригинальной функции
        input_func(*args)                # вызов оригинальной функции
    return output_func     # возвращаем новую функцию

# определение оригинальной функции


@check
def print_person(name, age):
    print(f"Name: {name}  Age: {age}")


# вызов оригинальной функции
print_person("Tom", 38)

# определение функции декоратора


def check(input_func):
    def output_func(*args):
        name = args[0]
        age = args[1]           # получаем значение второго параметра
        if age < 0:
            age = 1     # если возраст отрицательный, изменяем его значение на 1
        input_func(name, age)   # передаем функции значения для параметров
    return output_func

# определение оригинальной функции


@check
def print_person(name, age):
    print(f"Name: {name}  Age: {age}")


# вызов оригинальной функции
print_person(name="Tom", age=38)
print_person("Bob", -5)

# определение функции декоратора


def check(input_func):
    def output_func(*args):
        result = input_func(*args)   # передаем функции значения для параметров
        if result < 0:
            result = 0   # если результат функции меньше нуля, то возвращаем 0
        return result
    return output_func

# определение оригинальной функции


@check
def sum(a, b):
    return a + b


# вызов оригинальной функции
result1 = sum(a=10, b=20)
print(result1)          # 30

# result2 = sum(10, -20)
# print(result2)          # 0

# **********************************************


def _hello():
    print("hello!")


_hello()


def run_announced(func):
    print("run function", func)
    func()
    print("done running function", func)


_hello()
print(_hello)
run_announced(_hello)


def new_hello():
    run_announced(hello)


new_hello()

#


def goodbye():
    print("goodbye!")


def new_goodbye():
    run_announced(goodbye)


new_goodbye()
#


def create_wrapped_announced(func):
    def _run_announced():
        run_announced(func)
    return _run_announced


new_goodbye = create_wrapped_announced(goodbye)  # декоратор

new_goodbye()


goodbye = create_wrapped_announced(goodbye)  # декоратор
goodbye()


@create_wrapped_announced
def say_hi():
    print("hi!")


print(say_hi)

say_hi()

#


def make_announced(func):
    print("creating announced function", func)

    def new_announced():
        print("run function", func)
        func()
        print("done function", func)

    print("successfully created announced function for",
          func, "announced:", new_announced)
    return new_announced


@make_announced
def hello_world():
    print("Hello World!")


print(hello_world)
# hello_world =  make_announced(hello_world)

# print(hello_world)

hello_world.__doc__
print(hello_world.__doc__)
print(hello_world.__name__)

#
# from functools import wraps


def make_announced(func):
    print("creating announced function", func)

    @wraps(func)
    def new_announced():
        print("run function", func)
        func()
        print("done function", func)

    print("successfully created announced function for",
          func, "announced:", new_announced)
    return new_announced


@make_announced
def hello_world():
    """Hello doc string"""
    print("Hello World!")


print(hello_world.__doc__)

print(hello_world)
print(help(hello_world))
print(help(hello_world.__wrapped__))
