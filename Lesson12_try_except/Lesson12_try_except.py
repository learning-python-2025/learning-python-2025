'''
Конструкция try...except...finally

try:
    инструкции
except [Тип_исключения]:
    инструкции
except [Тип_исключения]:
    инструкции
    ...
else:
    инструкции
finally:    
    инструкции    
'''


string = "5"
number = int(string)
print(number)

string = "hello"
number = int(string)
print(number)


# ValueError: invalid literal for int() with base 10: 'hello'

string = input("Введите число: ")
number = int(string)
print(number)

try:
    number = int(input("Введите число: "))
    print("Введенное число:", number)
except:
    print("Преобразование прошло неудачно")
print("Завершение программы")


try:
    number = int(input("Введите число: "))
    print("Введенное число:", number)
except:
    print("Преобразование прошло неудачно")
finally:
    print("Блок try завершил выполнение")
print("Завершение программы")

#
try:
    number = 3/0    # генерирует исключение ZeroDivisionError
    print(number)
except:
    print("Деление на ноль")
finally:
    print("Блок try завершил выполнение")
print("Завершение программы")

# except и обработка разных типов исключений

try:
    number = int(input("Введите число: "))
    print("Введенное число:", number)
except ValueError:
    print("Преобразование прошло неудачно")
print("Завершение программы")

'''
https://docs.python.org/3/library/exceptions.html
базовые типы исключений:
    BaseException: базовый тип для всех встроенных исключений

    Exception: базовый тип, который обычно применяется для создания своих типов исключений

    ArithmeticError: базовый тип для исключений, связанных с арифметическими операциями (OverflowError, ZeroDivisionError, FloatingPointError).

    BufferError: тип исключения, которое возникает при невозможности выполнить операцию с буффером

    LookupError: базовый тип для исключений, которое возникают при обращении в коллекциях по некорректному ключу или индексу (например, IndexError, KeyError)
'''

'''
IndexError: исключение возникает, если индекс при обращении к элементу коллекции находится вне допустимого диапазона

KeyError: возникает, если в словаре отсутствует ключ, по которому происходит обращение к элементу словаря.

OverflowError: возникает, если результат арифметической операции не может быть представлен текущим числовым типом (обычно типом float).

RecursionError: возникает, если превышена допустимая глубина рекурсии.

TypeError: возникает, если операция или функция применяется к значению недопустимого типа.

ValueError: возникает, если операция или функция получают объект корректного типа 
с некорректным значением.

ZeroDivisionError: возникает при делении на ноль.

NotImplementedError: тип исключения для указания, что какие-то методы класса не реализованы

ModuleNotFoundError: возникает при при невозможности найти модуль при его импорте директивой import

OSError: тип исключений, которые генерируются при возникновении ошибок системы (например, невозможно найти файл, память диска заполнена и т.д.)
'''
#
try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    print("Результат деления:", number1/number2)
except ValueError:
    print("Преобразование прошло неудачно")
except ZeroDivisionError:
    print("Попытка деления числа на ноль")
except BaseException:
    print("Общее исключение")
print("Завершение программы")

#
try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    print("Результат деления:", number1/number2)
except ZeroDivisionError:
    print("Попытка деления числа на ноль")
print("Завершение программы")

#
try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    print("Результат деления:", number1/number2)
# обработка двух типов исключений - ZeroDivisionError и ValueError
except (ZeroDivisionError, ValueError):
    print("Попытка деления числа на ноль или некорректный ввод")

print("Завершение программы")

# #
try:
    number = int(input("Введите число: "))
    print("Введенное число:", number)
except ValueError as e:
    print("Сведения об исключении", e)
print("Завершение программы")

# # Генерация исключений и оператор raise

try:
    age = int(input("Введите возраст: "))
    if age > 110 or age < 1:
        raise Exception("Некорректный возраст")
    print("Ваш возраст:", age)
except ValueError:
    print("Введены некорректные данные")
except Exception as e:
    print(e)
print("Завершение программы")

# #


class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age   # устанавливаем возраст

    def display_info(self):
        print(f"Имя: {self.__name}  Возраст: {self.__age}")

#


class PersonAgeException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f"Недопустимое значение: {self.age}. " \
            f"Возраст должен быть в диапазоне от {
                self.minage} до {self.maxage}"


class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        minage, maxage = 1, 110
        if minage < age < maxage:   # устанавливаем возраст, если передано корректное значение
            self.__age = age
        else:                       # иначе генерируем исключение
            raise PersonAgeException(age, minage, maxage)

    def display_info(self):
        print(f"Имя: {self.__name}  Возраст: {self.__age}")


try:
    tom = Person("Tom", 37)
    tom.display_info()  # Имя: Tom  Возраст: 37

    bob = Person("Bob", -23)
    bob.display_info()
except PersonAgeException as e:
    print(e)    # Недопустимое значение: -23. Возраст должен быть в диапазоне от 1 до 110
