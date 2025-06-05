# Ключевые слова, нельзя использовать для имени переменных
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield

# PEP 8 – соглашения о кодировании для кода Python
#  https://peps.python.org/pep-0008/

# Какие имена можно давать переменным:
# x, X, xyz, _x_y_z, XYZ, xyz_123, _123, x1Y2z2

# Как нельзя называть переменные:
# 1, 1x, x y z, x&y

# Стили именования переменных:
# lowercase — все буквы строчные;
# lower_case_with_underscores — все буквы строчные, между словами нижние подчёркивания;
# UPPERCASE — все буквы заглавные;
# UPPER_CASE_WITH_UNDERSCORES — все буквы заглавные, между словами нижние подчёркивания;
# amelCase — каждое слово начинается с заглавной буквы;
# mixedCase — каждое слово, кроме первого, начинается с заглавной буквы;
# Camel_Case_With_Underscores — каждое слово начинается с заглавной буквы, между словами нижние подчёркивания (это некрасиво, никогда так не делайте).

# тип переменной определяется в момент присвоения значения и сохраняется, пока не будет переопределен следующими присвоением (динамическая типизация)
# Пример:
# name = "Tom"  # переменной name равна "Tom"
# print(name)   # выводит: Tom

# name = 1  # меняем значение на "Bob"
# print(name)   # выводит: Bob

# Варианты присваивания значений
# Вариант 1:
# x = 1
# y = 1
# z = 1
# print(x)

# Вариант 2:Множественное присваивание значений
# x = y = z = 2
# print(x, y, z)
# если ссылаются на одно значение id ссылки одинаковый:
# print(id(x))
# print(id(y))
# print(id(z))

# x = 3
# print(id(x))
# print(id(y))
# print(id(z))

# Вариант 3:Множественное присваивание разных значений
# x, y, z = 1, 'Game', ['List', 'Go', 'String']
# print(x, y, z)

###########################################################
# Типы данных:
# тип string
# name_first = "Tom"
# print(name_first)

# тип int
# num_int = 123
# print(num_int)

# тип float
# height = 1.68
# pi = 3.14
# weight = 68.
# print(height)   # 1.68
# print(pi)       # 3.14
# print(weight)   # 68.0

# тип Bool
# _bool = True
# print(_bool)   # True

# complexNumber = 1+2j
# print(complexNumber)   # (1+2j)

# Удаление переменных:
# x = 4
# del x
# print(x)


# Области видимости переменных:
# локальная — внутри одной функции
# работаем с локальной переменной в пределах функции
def local_namespace():
    x = 4
    x = x ** 2
    return x


print(local_namespace())

# обращение к локальной переменной не из функции, где она определена - ошибка:


def local_namespace():
    x = 4
    x = x ** 2
    return x


print(x)

# изменение глобальной переменной из функции  - ошибка, функция ее не видит:
x = 4


def local_namespace():
    x = 4
    x = x ** 2
    return x


print(local_namespace())

# чтение значения из глобальной переменной в функции - можно:
x = 4


def local_namespace():
    y = x ** 2
    return y


print(x)
print(local_namespace())

# внутри одной программы может быть сразу несколько переменных с одним и тем же именем. Для этого они должны находиться в разных пространствах имён:
x = 0   # глобальная


def local_namespace():
    x = 4   # локальная
    x = x ** 2
    return x


print(x)
print(local_namespace())

# Глобальные — вне функций, существует в пространстве имён всего py-файла
# К глобальной переменной можно обратиться внутри функции, но нельзя изменять. Чтобы исправить это, существует ключевое слово global:
x = 4


def local_namespace():
    global x
    x = x ** 2
    return x


print(x)
print(local_namespace())

# В функии можно определить глобальную переменную ключевым словом global


def local_namespace():
    global x
    x = 4
    return x


print(local_namespace())
print(x)

# Нелокальные переменные
# используются, когда одна функция вложена в другую, и охватывают пространство имён только этих двух функций. Ключевое слово nonlocal
# def nonlocal_namespace():
#     x = 4
#     def local_namespace():
#         nonlocal x
#         x = x ** 2
#         return x
#     return local_namespace()
# print(nonlocal_namespace())

# в глобальной области видимости к нелокальной переменной обратиться нельзя:
# def nonlocal_namespace():
#     x = 4
#     def local_namespace():
#         nonlocal x
#         x = x ** 2
#         return x
#     return local_namespace()
# print(x)


# Проверка существования переменной
# globals()
# name = 'Виктория'
# if 'name' in globals():
#     print(True)

# name = 'Виктория'
# if 'name' in globals():
#     print(globals().get('name'))

# locals()
# def local_namespace():
#     name = 'Виктория'
#     if 'name' in locals():
#         print(locals().get('name'))
# local_namespace()

# Python поддерживает числа в двоичной, восьмеричной и шестнадцатеричной системах:
# двоичную систему 0b
# a = 0b11
# b = 0b1011
# c = 0b100001
# print(a)    # 3 в десятичной системе
# print(b)    # 11 в десятичной системе
# print(c)    # 33 в десятичной системе
# print(f"number = {a:0b}")
# восьмеричную систему 0o
# a = 0o7
# b = 0o11
# c = 0o17
# print(a)    # 7 в десятичной системе
# print(b)    # 9 в десятичной системе
# print(c)    # 15 в десятичной системе
# print(f"number = {c:0o}")
# шестнадцатеричную систему 0x
# a = 0x0A
# b = 0xFF
# c = 0xA1
# print(a)    # 10 в десятичной системе
# print(b)    # 255 в десятичной системе
# print(c)    # 161 в десятичной системе
# print(f"number = {a:0x}")

# Перенос строки на несколько строк:
# text = ("Laudate omnes gentes laudate "
#         "Magnificat in secula ")
# print(text)

# text = '''Laudate omnes gentes laudate
# Magnificat in secula
# Et anima mea laudate
# Magnificat in secula
# '''
# print(text)

# '''
# Это комментарий
# '''
# Управляющие последовательности в строке
# text = "Message:\n\"Hello World\""
# print(text)

# path = "C:\python\name.txt"
# print(path)

# path = r"C:\python\name.txt"
# print(path)

# Строка может содержать ряд специальных символов - управляющих последовательностей. Некоторые из них:

# \\: позволяет добавить внутрь строки слеш

# \': позволяет добавить внутрь строки одинарную кавычку

# \": позволяет добавить внутрь строки двойную кавычку

# \n: осуществляет переход на новую строку

# \t: добавляет табуляцию (4 отступа)

# Вставка значений в строку
# userName = "Tom"
# userAge = 37
# user = f"name: {userName}  age: {userAge}"
# print(user)   # name: Tom  age: 37

# type() - динамически можно узнать текущий тип переменной
# userId = "abc"  # тип str
# print(userId)

# userId = 234  # тип int
# print(userId)

# userId = "abc"      # тип str
# print(type(userId)) # <class 'str'>

# userId = 234        # тип int
# print(type(userId)) # <class 'int'>
#########################################################################
# Импорт переменных
# from variables2 import name
# print(name)

# доступа к другим переменным из variables2.py в таком случае нет
# from variables2 import name
# print(age)

# импортировать несколько переменных
# from variables2 import name, age
# print(name, age)

# импортировать все объекты
# from variables2 import *
# print(name, age, city)
