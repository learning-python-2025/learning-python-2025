'''
Адреса неизменяемых объектов
'''

from copy import deepcopy
my_number = 10
print(id(my_number))

other_number = 10
print(id(other_number))

print(id(10))

'''
Копирование неизменяемых объектов
'''

first_num = 10
second_num = first_num

print(id(first_num))
print(id(second_num))


second_num = second_num + 5  # создание нового объекта

print(second_num)
print(first_num)

print(id(first_num))
print(id(second_num))

'''
Адреса изменяемых объектов
'''

my_list = [1, 2, 3]
print(id(my_list))

other_list = [1, 2, 3]
print(id(other_list))

print(id([1, 2, 3]))

other_list.append(4)

# print(my_list)
print(id(my_list))
print(id(other_list))


print(id(my_list))

info = {'name': 'Kate',
        'is_instructor': True

        }
print(id(info))

info_copy = info  # копируем ссылку , после копирования изменяемых объектов, изменения отражаются на всех копиях
info['rev_qty'] = 5

print(info['rev_qty'])
print(info_copy['rev_qty'])

info_copy['rev_qty'] = 100
print(info['rev_qty'])
print(info_copy['rev_qty'])


info_1 = {'name': 'Kate',
          'is_instructor': True

          }

info_2 = {'name': 'Kate',
          'is_instructor': True

          }
info_1['rev_qty'] = 5

# print(info_1['rev_qty'])
# print(info_2['rev_qty'])

info_2['rev_qty'] = 100

print(info_1['rev_qty'])
print(info_2['rev_qty'])


'''
Копирование изменяемых объектов
'''
#
info_1 = {'name': 'Kate',
          'is_instructor': True

          }

info_2 = info_1.copy()

info_2['rev_qty'] = 200
print(info_1['rev_qty'])
print(info_2['rev_qty'])

#
info_1 = {'name': 'Kate',
          'is_instructor': True,
          'reviews': []

          }

# копия только первого уровня, вложенные изменяемые объекты сохраняются, копируются только ссылки
info_2 = info_1.copy()
info_2['reviews'].append('Hello!')

print(info_1)

print(info_2)

# Полная копия


info_1 = {'name': 'Kate',
          'is_instructor': True,
          'reviews': []

          }
info_2 = deepcopy(info_1)

info_2['reviews'].append('Hello!')

print(info_1)

print(info_2)

'''
Передача неизменяемых объектов в функцию
'''


def my_fn(a=10, b='123'):
    """
    описание функции my_fn
    """
    a = a + 1  # создается новый объект, внешние переменные не изменятся
    c = a + b
    return c


n1 = 10
n2 = 5

res = my_fn(n1, n2)

print(res)
print(n1)


'''
Передача изменяемых объектов в функцию
'''


def my_fn(person):  # копирование словаря по ссылке, происходит изменение вшего объекта, что не  рекомендуется
    person['age'] += 1
    return person


person_one = {
    'name': 'Kate',
    'age': 25
}

my_fn(person_one)

print(person_one['age'])

# можно создать копию


def my_fn(person):  # копирование словаря по ссылке, происходит изменение вшего объекта, что не  рекомендуется
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy


person_one = {
    'name': 'Kate',
    'age': 25
}

new_person = my_fn(person_one)

print(person_one['age'])
print(new_person['age'])
