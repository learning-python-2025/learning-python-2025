'''
def имя_функции ([параметры]):
    инструкции
'''
# Тело функции  может быть пустой


from datetime import date


def say_hello():
    pass


def say_hello():
    print("Hello")
#


def say_hello():
    print("Hello")


print("Bye")
#


def say_hello():    # определение функции say_hello
    print("Hello")


say_hello()         # вызов функции say_hello
say_hello()
say_hello()

#


def say_hello(): print("Hello")


say_hello()

#


def say_hello():
    print("Hello")


def say_goodbye():
    print("Good Bye")


say_hello()
say_goodbye()

#


def print_messages():
    # определение локальных функций
    def say_hello(): print("Hello")
    def say_goodbye(): print("Good Bye")
    # вызов локальных функций
    say_hello()
    say_goodbye()


# Вызов функции print_messages
print_messages()

# say_hello() # вне функции print_messages функция say_hello не доступна

#


def main():
    say_hello()
    say_goodbye()


def say_hello():
    print("Hello")


def say_goodbye():
    print("Good Bye")


# Вызов функции main
main()

'''
Параметры функции
'''
#


def say_hello(name):
    print(f"Hello, {name}")


say_hello("Tom")
say_hello("Bob")
say_hello("Alice")

#


def print_person(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")


print_person("Tom", 37)


# Значения по умолчанию
def say_hello(name="Tom"):
    print(f"Hello, {name}")


say_hello()         # здесь параметр name будет иметь значение "Tom"
say_hello("Bob")    # здесь name = "Bob"


#
def print_person(name, age=18):
    print(f"Name: {name}  Age: {age}")


print_person("Bob")
print_person("Tom", 37)

#


def print_person(name="Tom", age=18):
    print(f"Name: {name}  Age: {age}")


print_person()              # Name: Tom  Age: 18
print_person("Bob")         # Name: Bob  Age: 18
print_person("Sam", 37)     # Name: Sam  Age: 37

#


def print_person(name, age):
    print(f"Name: {name}  Age: {age}")


print_person(age=22, name="Tom")

#  только по имени


def print_person(name, *,  age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")


# Name: Bob  Age: 41  company: Microsoft
print_person("Bob", age=41, company="Microsoft")

#


def print_person(*,  name, age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")

# позиционные параметры


def print_person(name, /, age, company="Microsoft"):
    print(f"Name: {name}  Age: {age}  Company: {company}")


# Name: Tom  Age: 24  company: JetBrains
print_person("Tom", company="JetBrains", age=24)
# Name: Bob  Age: 41  company: Microsoft
print_person("Bob", 41)

#


def print_person(name, /,  age=18, *, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")


# Name: Sam  Age: 18  company: Google
print_person("Sam", company="Google")
# Name: Tom  Age: 37  company: JetBrains
print_person("Tom", 37, company="JetBrains")
# Name: Bob  Age: 42  company: Microsoft
print_person("Bob", company="Microsoft", age=42)

# Неопределенное количество параметров


def sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")


sum(1, 2, 3, 4, 5)      # sum = 15
sum(3, 4, 5, 6)         # sum = 18


'''
def имя_функции ([параметры]):
    инструкции
    return возвращаемое_значение
'''


def get_message():
    return "Hello METANIT.COM"


message = get_message()  # получаем результат функции get_message в переменную message
print(message)          # Hello METANIT.COM

# можно напрямую передать результат функции get_message
print(get_message())    # Hello METANIT.COM

#


def double(number):
    return 2 * number


result1 = double(4)     # result1 = 8
result2 = double(5)     # result2 = 10
print(f"result1 = {result1}")   # result1 = 8
print(f"result2 = {result2}")   # result2 = 10

#


def sum(a, b):
    return a + b


result = sum(4, 6)                  # result = 0
print(f"sum(4, 6) = {result}")      # sum(4, 6) = 10
print(f"sum(3, 5) = {sum(3, 5)}")   # sum(3, 5) = 8

#


def get_message():
    return "Hello METANIT.COM"
    print("End of the function")


print(get_message())


#
def print_person(name, age):
    if age > 120 or age < 1:
        print("Invalid age")
        return
    print(f"Name: {name}  Age: {age}")


print_person("Tom", 22)
print_person("Bob", -102)

'''
Функция как тип
'''
def say_hello(): print("Hello")
def say_goodbye(): print("Good Bye")


message = say_hello
message()       # Hello
message = say_goodbye
message()       # Good Bye

#


def sum(a, b): return a + b
def multiply(a, b): return a * b


operation = sum
result = operation(5, 6)
print(result)   # 11

operation = multiply
print(operation(5, 6))      # 30

'''
Функция как параметр функции
'''


def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")


def sum(a, b): return a + b
def multiply(a, b): return a * b


do_operation(5, 4, sum)         # result = 9
do_operation(5, 4, multiply)   # result = 20


#


def get_weekday():
    return date.today().strftime('%A')


def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['create_on_weekday'] = weekday
    return post_copy


initial_post = {
    'id': 243,
    'autor': 'Any_autor',
}

post_with_weekday = create_new_post(initial_post)

print(post_with_weekday)


'''
Функция как результат функции
'''
def sum(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b


def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply


operation = select_operation(1)     # operation = sum
print(operation(10, 6))             # 16

operation = select_operation(2)     # operation = subtract
print(operation(10, 6))             # 4

operation = select_operation(3)     # operation = multiply
print(operation(10, 6))             # 60


def do_operation(a, b, operation):
    result = operation(a, b)
    print(result)


def sum(a, b): return a + b
# def subtract(a, b): return a - b
def multiply(a, b): return a * b


do_operation(5, 4, sum)
do_operation(5, 4, multiply)


'''
Лямбда-выражения
lambda [параметры] : инструкция
'''


def message(): return print("hello")


message()   # hello
# =


def message():
    print("hello")


def square(n): return n * n


print(square(4))    # 16
print(square(5))    # 25
# =
def square2(n): return n * n


#
def sum(a, b): return a + b


print(sum(4, 5))    # 9
print(sum(5, 6))    # 11

#


def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")


do_operation(5, 4, lambda a, b: a + b)  # result = 9
do_operation(5, 4, lambda a, b: a * b)  # result = 20

#

a = 10


def select_operation(choice):
    a = 20
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b


operation = select_operation(1)  # operation = sum
print(operation(10, 6))  # 16

operation = select_operation(2)  # operation = subtract
print(operation(10, 6))  # 4

operation = select_operation(3)  # operation = multiply
print(operation(10, 6))  # 60


'''
Описание функции
'''


def mult_by_factor(value, mult=1):
    """Multiplies number by multiplicator"""
    return value * mult


mult_by_factor(5)

'''
Описание аргументов
'''


def mult_by_factor(value, mult=1):
    """Multiplies number by multiplicator

    Args:
       value (Any) any value \n
       mult (int)
    """
    return value * mult


mult_by_factor(5)
