"""
Итераторы
iter()
next()
StopIteration
"""

# https://docs-python.ru/standart-library/modul-typing-python/
from typing import List

list = [1, 2, 3, 4, 5]
for i in list:
    print(i)  # -> 1 2 3 4 5

iterator = iter(list)
print(iterator)
l1 = next(iterator)
print(l1)
l2 = next(iterator)
print(l2)
l3 = next(iterator)
print(l3)
l4 = next(iterator)
print(l4)
l5 = next(iterator)
print(l5)

# Примеры последовательностей
numbers = [1, 2, 3, 4, 5]
letters = ('a', 'b', 'c')
characters = 'habristhebestsiteever'
print(numbers[1])

print(letters[2])

print(characters[11])

print(characters[0:4])

# Итерируемые объекты
unordered_numbers = {1, 2, 3}
print(unordered_numbers[1])  # TypeError: 'set' object is not subscriptable

users = {'males': 23, 'females': 32}
print(users[1])  # TypeError: 'set' object is not subscriptable

for user in users:
    print(user)

# Циклы для последовательностей

list_of_numbers = [1, 2, 3]
index = 0
while index < len(list_of_numbers):
    print(list_of_numbers[index])
    index += 1
# циклы для итерируемых объектов, которые не явл. последовательностями
set_of_numbers = {1, 2, 3}
index = 0
while index < len(set_of_numbers):
    print(set_of_numbers[index])
    index += 1
# TypeError: 'set' object is not subscriptable

set_of_numbers = {1, 2, 3}
for index, number in enumerate(set_of_numbers):
    print(number, index)


#
set_of_numbers = {1, 2, 3}
list_of_numbers = [1, 2, 3]
string_of_numbers = '123'

a = iter(set_of_numbers)  # создается объект итератор set_iterator
print(a)
b = iter(list_of_numbers)  # создается объект итератор list_iterator
print(b)
c = iter(string_of_numbers)  # создается объект итератор str_ascii_iterator
print(c)
print(next(a))
print(next(a))
print(next(a))
print(next(a))  # StopIteration


# Реализация цикла for с помощью функции и цикла while
def for_loop(iterable, loop_body_func):
    iterator = iter(iterable)
    next_element_exist = True
    while next_element_exist:
        try:
            element_from_iterator = next(iterator)
        except StopIteration:
            next_element_exist = False
        else:
            loop_body_func(element_from_iterator)


set_of_numbers = {1, 2, 3}
for_loop(set_of_numbers, print)

# Примеры итераторов
# распаковка
coordinates = [1, 2, 3]
x, y, z = coordinates

numbers = [1, 2, 3, 4, 5]
a, b, *rest = numbers

print(*numbers)

# enumerate
numbers = [1, 2, 3]
enumerate_var = enumerate(numbers)
print(enumerate_var)
print(next(enumerate_var))

# zip
letters = ['a', 'b', 'c']
z = zip(letters, numbers)
print(z)
print(next(z))

# open
f = open('print.txt')
print(next(f))

"""Класс обеспечивает бесконечное последовательное возведение в квадрат заданного числа."""


class InfiniteSquaring:
    def __init__(self, initial_number):
        # Здесь хранится промежуточное значение
        self.number_to_square = initial_number

    def __next__(self):
        # Здесь мы обновляем значение и возвращаем результат
        self.number_to_square = self.number_to_square ** 2
        return self.number_to_square

    def __iter__(self):
        """Этот метод позволяет при передаче объекта функции iter возвращать самого себя, тем самым в точности реализуя протокол итератора."""
        return self


squaring_of_six = InfiniteSquaring(6)
print(next(squaring_of_six))
print(next(squaring_of_six))
print(next(squaring_of_six))
print(next(squaring_of_six))

print(iter(squaring_of_six) is squaring_of_six)
