# #Создание списка

import itertools
numbers = [1, 2, 3, 4, 5]
people = ["Tom", "Sam", "Bob"]

numbers1 = []
numbers2 = list()

objects = [1, 2.6, "Hello", True]

numbers = [1, 2, 3, 4, 5]
people = ["Tom", "Sam", "Bob"]

print(numbers)  # [1, 2, 3, 4, 5]
print(people)   # ["Tom", "Sam", "Bob"]


numbers1 = [1, 2, 3, 4, 5]
numbers2 = list(numbers1)
print(numbers2)  # [1, 2, 3, 4, 5]

letters = list("Hello")
print(letters)      # ['H', 'e', 'l', 'l', 'o']


numbers = [5] * 6   # 6 раз повторяем 5
print(numbers)      # [5, 5, 5, 5, 5, 5]

people = ["Tom"] * 3    # 3 раза повторяем "Tom"
print(people)           # ["Tom", "Tom", "Tom"]

students = ["Bob", "Sam"] * 2   # 2 раза повторяем "Bob", "Sam"
print(students)                 # ["Bob", "Sam", "Bob", "Sam"]


'''Обращение к элементам списка'''

# people = ["Tom", "Sam", "Bob"]
# получение элементов с начала списка

# print(people[0])   # Tom
# print(people[1])   # Sam
# print(people[2])   # Bob

# получение элементов с конца списка

# print(people[-2])   # Sam
# print(people[-1])   # Bob
# print(people[-3])   # Tom


people = ["Tom", "Sam", "Bob"]

people[1] = "Mike"  # изменение второго элемента
print(people[1])    # Mike
print(people)       # ["Tom", "Mike", "Bob"]

'''Разложение списка'''

people = ["Tom", "Bob", "Sam"]

tom, bob, sam = people

print(tom)      # Tom
print(bob)      # Bob
print(sam)      # Sam
'''
Перебор элементов
'''


people = ["Tom", "Sam", "Bob"]
for person in people:
    print(person)

people = ["Tom", "Sam", "Bob"]
i = 0
while i < len(people):  # len() получаем длину списка
    print(people[i])    # применяем индекс для получения элемента
    i += 1

'''
Сравнение списков
'''

numbers1 = [1, 2, 3, 4, 5]
numbers2 = list([1, 2, 3, 5, 4])
if numbers1 == numbers2:
    print("numbers1 equal to numbers2")
else:
    print("numbers1 is not equal to numbers2")


'''
    Получение части списка
    list[start:end:step]
'''

people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]

slice_people1 = people[:3]   # с 0 по 3
print(slice_people1)   # ["Tom", "Bob", "Alice"]

slice_people2 = people[1:3]   # с 1 по 3
print(slice_people2)   # ["Bob", "Alice"]

slice_people3 = people[1:6:2]   # с 1 по 6 с шагом 2
print(slice_people3)   # ["Bob", "Sam", "Bill"]


people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]

slice_people1 = people[:-1]   # с предпоследнего по нулевой
print(slice_people1)   # ["Tom", "Bob", "Alice", "Sam", "Tim"]

slice_people2 = people[-3:-1]   # с третьего с конца по предпоследний
print(slice_people2)   # [ "Sam", "Tim"]


'''Методы и функции по работе со списками

    append(item): добавляет элемент item в конец списка

    insert(index, item): добавляет элемент item в список по индексу index

    extend(items): добавляет набор элементов items в конец списка

    remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError

    clear(): удаление всех элементов из списка

    index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError

    pop([index]): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.

    count(item): возвращает количество вхождений элемента item в список

    sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию. Но с помощью параметра key мы можем передать функцию сортировки.

    reverse(): расставляет все элементы в списке в обратном порядке

    copy(): копирует список

    встроенные функции для работы со списками:

    len(list): возвращает длину списка

    sorted(list, [key]): возвращает отсортированный список

    min(list): возвращает наименьший элемент списка

    max(list): возвращает наибольший элемент списка
'''
# people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
# print(dir(people))

'''Добавление и удаление элементов
Для добавления элемента применяются методы append(), extend и insert,
а для удаления - методы remove(), pop() и clear().'''

# people = ["Tom", "Bob"]

# # добавляем в конец списка
# people.append("Alice")  # ["Tom", "Bob", "Alice"]
# # добавляем на вторую позицию
# people.insert(1, "Bill")  # ["Tom", "Bill", "Bob", "Alice"]
# # добавляем набор элементов ["Mike", "Sam"]
# # ["Tom", "Bill", "Bob", "Alice", "Mike", "Sam"]
# people.extend(["Mike", "Sam"])
# # получаем индекс элемента
# index_of_tom = people.index("Tom")
# # удаляем по этому индексу
# # ["Bill", "Bob", "Alice", "Mike", "Sam"]
# removed_item = people.pop(index_of_tom)
# # удаляем последний элемент
# last_item = people.pop()     # ["Bill", "Bob", "Alice", "Mike"]
# # удаляем элемент "Alice"
# people.remove("Alice")      # ["Bill", "Bob", "Mike"]
# print(people)       # ["Bill", "Bob", "Mike"]
# # удаляем все элементы
# people.clear()
# print(people)       # []

'''Проверка наличия элемента'''

# people = ["Tom", "Bob", "Alice", "Sam"]

# if "Alice" in people:
#     people.remove("Alice")
# print(people)       # ["Tom", "Bob", "Sam"]

'''Удаление с помощью del'''

# people = ["Tom", "Bob", "Alice", "Sam", "Bill", "Kate", "Mike"]

# del people[1]   # удаляем второй элемент
# print(people)   # ["Tom", "Alice", "Sam", "Bill", "Kate", "Mike"]
# del people[:3]   # удаляем  по четвертый элемент не включая
# print(people)   # ["Bill", "Kate", "Mike"]
# del people[1:]   # удаляем  со второго элемента
# print(people)   # ["Bill"]

'''Изменение подсписка'''
# nums = [10, 20, 30, 40, 50]
# nums[1:4] = [11, 22]
# print(nums)     # [10, 11, 22, 50]

'''Подсчет вхождений'''

# people = ["Tom", "Bob", "Alice", "Tom", "Bill", "Tom"]

# people_count = people.count("Tom")
# print(people_count)      # 3

'''Сортировка метод sort()'''

# people = ["Tom", "Bob", "Alice", "Sam", "Bill"]

# people.sort()
# print(people)      # ["Alice", "Bill", "Bob", "Sam", "Tom"]

'''reverse()'''
# people = ["Tom", "Bob", "Alice", "Sam", "Bill"]

# people.sort(reverse = True)
# people.reverse()
# print(people)      # ["Tom", "Sam", "Bob", "Bill", "Alice"]

# people = ["Tom", "bob", "alice", "Sam", "Bill"]

# people.sort()       # стандартная сортировка
# print(people)      # ["Bill", "Sam", "Tom", "alice", "bob"]

# people.sort(key=str.lower)  # сортировка без учета регистра
# print(people)      # ["alice", "Bill", "bob", "Sam", "Tom"]

'''функция sorted()'''

# people = ["Tom", "bob", "alice", "Sam", "Bill"]

# sorted_people = sorted(people, key=str.lower)
# print(sorted_people)      # ["alice", "Bill", "bob", "Sam", "Tom"]

'''Фильтрация списка    функция filter()
    filter(fun, iter)

'''

numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]


def condition(number): return number > 1


result = filter(condition, numbers)

for n in result:
    print(n, end=" ")      # 2 3 4 5

'''через люмбда-выражение'''

# numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# result = filter(lambda n: n > 1, numbers)

# for n in result:
#     print(n, end=" ")      # 2 3 4 5


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [Person("Tom", 38), Person("Kate", 31), Person("Bob", 42),
          Person("Alice", 34),  Person("Sam", 25)]

# # фильтрация элементов, у которых age > 33
view = filter(lambda p: p.age > 33, people)

for person in view:
    print(f"Name: {person.name} Age: {person.age}")

'''Проекция списка
    map(fun, iter)

'''
numbers = [1, 2, 3, 4, 5]


def square(number): return number * number


result = map(square, numbers)

for n in result:
    print(n, end=" ")      # 1 4 9 16 25


# numbers = [1, 2, 3, 4, 5]

# result = map(lambda n: n * n, numbers)

# for n in result:
#     print(n, end=" ")      # 1 4 9 16 25

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# people = [Person("Tom", 38), Person("Kate", 31), Person("Bob", 42),
#           Person("Alice", 34),  Person("Sam", 25)]

# # получаем из Person строку с именем
# view = map(lambda p: p.name, people)

# for person in view:
#     print(person)

'''Минимальное и максимальное значения'''

# numbers = [9, 21, 12, 1, 3, 15, 18]
# print(min(numbers))     # 1
# print(max(numbers))     # 21

'''Копирование списков'''
# shallow copy новый список не создается

# people1 = ["Tom", "Bob", "Alice"]
# people2 = people1
# people2.append("Sam")   # добавляем элемент во второй список
# # people1 и people2 указывают на один и тот же список
# print(people1)   # ["Tom", "Bob", "Alice", "Sam"]
# print(people2)   # ["Tom", "Bob", "Alice", "Sam"]

# deep copy создается новый объект

# people1 = ["Tom", "Bob", "Alice"]
# people2 = people1.copy()    # копируем элементы из people1 в people2 встроенным методом
# people3 = list(people1)    # копируем элементы из people1 в people3 вызывая конструктор
# people4 = people1[:]    # копируем элементы из people1 в people4 slice нарезкой


# people2.append("Sam")   # добавляем элемент ТОЛЬКО во второй список
# # people1 и people2 указывают на разные списки
# print(people1)   # ["Tom", "Bob", "Alice"]
# print(people2)   # ["Tom", "Bob", "Alice", "Sam"]

'''Соединение списков + (__add__)'''

people1 = ["Tom", "Bob", "Alice"]
people2 = ["Tom", "Sam", "Tim", "Bill"]
people3 = people1 + people2
print(people3)   # ["Tom", "Bob", "Alice", "Tom", "Sam", "Tim", "Bill"]
people4 = people1.__add__(people2)
print(people4)   # ["Tom", "Bob", "Alice", "Tom", "Sam", "Tim", "Bill"]

'''Списки списков'''

people = [
    ["Tom", 29],
    ["Alice", 33],
    ["Bob", 27]
]

print(people[0])         # ["Tom", 29]
print(people[0][0])      # Tom
print(people[0][1])      # 29

# изменение  вложенных списков

people = [
    ["Tom", 29],
    ["Alice", 33],
    ["Bob", 27]
]

# # создание вложенного списка
person = list()
person.append("Bill")
person.append(41)
# добавление вложенного списка
people.append(person)

print(people[-1])         # ["Bill", 41]

# # добавление во вложенный список
# people[-1].append("+79876543210")

# print(people[-1])         # ["Bill", 41, "+79876543210"]

# # удаление последнего элемента из вложенного списка
# people[-1].pop()
# print(people[-1])         # ["Bill", 41]

# # удаление всего последнего вложенного списка
# people.pop(-1)

# # изменение первого элемента
# people[0] = ["Sam", 18]
# print(people)            # [ ["Sam", 18], ["Alice", 33], ["Bob", 27]]

# перебор вложенных списков

people = [
    ["Tom", 29],
    ["Alice", 33],
    ["Bob", 27]
]

for person in people:
    for item in person:
        print(item, end=" | ")

'''Списки и алгоритмы
пример - факториал числа'''


def fact(n):
    return [1, 0][n > 1] or fact(n-1) * n


print(fact(4))

'''
Пошаговое выполнение:

[1,0] [4>1] or fact(4-1) * 4

0 or fact(4-1) * 4

([1,0] [3>1] or fact(3-1)) * 4

(0 or fact(3-1)) * 4

(([1,0] [2>1] or fact(2-1)) * 3) * 4

((0 or fact(2-1)) * 3) * 4

((([1,0] [1>1] or fact(1-1)) * 2) * 3) * 4

(((1 or fact(1-1)) * 2) * 3) * 4

(((1) * 2) * 3) * 4
'''

'''
Функция zip() слияние нескольких списков
'''

a = [10, 20, 30, 40]
b = ['a', 'b', 'c', 'd', 'e']
for i, j in zip(a, b):
    print(i, j)

for i in zip(a, b):
    print(i, type(i))

a = [10, 20, 30, 40]
b = ['a', 'b', 'c', 'd', 'e']
c = [1.1, 1.2]
# for i in itertools.zip_longest(a, b, c):
#     print(i)
for i in itertools.zip_longest(a, b, c, fillvalue=0):
    print(i)

a = [10, 20, 30, 40]
c = [1.1, 1.2, 1.3, 1.4]
ac = zip(a, c)
print(type(ac))

ac = list(ac)
print(type(ac))

print(ac)
# [(10, 1.1), (20, 1.2), (30, 1.3), (40, 1.4)]

values = [1.34, 3.25, 2.99]
coefficient = [3, 2, 2]
for i, j in zip(values, coefficient):
    print(i*j)


a = []
b = []
for i, j in zip(range(10, 20), range(1, 10)):
    a.append(i)
    b.append(j)

fruits = ['apple', 'banana', 'lime']
quantities = {100, 70, 50}
availability = (True, False, False, True)
fruit_qtys_zip = zip(fruits, quantities, availability)  # zip object
print(type(fruit_qtys_zip))
print(fruit_qtys_zip)

print(list(fruit_qtys_zip))

# zip object только 2 списка - ключ и значение, иначе при конвертации получим пустой словарь
fruit_qtys_zip = zip(fruits, quantities)
print(dict(fruit_qtys_zip))
