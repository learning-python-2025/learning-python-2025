users = {"Tom", "Bob", "Alice", "Tom"}
print(users)    # {"Alice", "Bob", "Tom"}

people = ["Mike", "Bill", "Ted"]
users = set(people)
print(users)    # {"Mike", "Bill", "Ted"}

users = set()

users = {"Tom", "Bob", "Alice"}
print(len(users))       # 3

users = set()

'''Добавление элементов'''

users.add("Sam")
print(users)

'''Удаление элементов'''

users = {"Tom", "Bob", "Alice"}

user = "Tom"
if user in users:
    users.remove(user)
print(users)    # {"Bob", "Alice"}

users = {"Tom", "Bob", "Alice"}

users.discard("Tim")    # элемент "Tim" отсутствует, и метод ничего не делает
print(users)  # {"Tom", "Bob", "Alice"}

users.discard("Tom")    # элемент "Tom" есть, и метод удаляет элемент
print(users)  # {"Bob", "Alice"}

users.clear()

'''
Перебор множества
'''

users = {"Tom", "Bob", "Alice"}

for user in users:
    print(user)

'''Операции с множествами'''
# Копирование
users = {"Tom", "Bob", "Alice"}
students = users.copy()
print(students)     # {"Tom", "Bob", "Alice"}

# Объединение
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

users3 = users.union(users2)
print(users3)   # {"Bob", "Alice", "Sam", "Kate", "Tom"}


users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

print(users | users2)   # {"Bob", "Alice", "Sam", "Kate", "Tom"}

# Пересечение
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

users3 = users.intersection(users2)
print(users3)   # {"Bob"}

users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

print(users & users2)   # {"Bob"}

# заменяет пересеченными элементами первое множество
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
users.intersection_update(users2)
print(users)   # {"Bob"}

# Разность множеств
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

users3 = users.difference(users2)
print(users3)           # {"Tom", "Alice"}
print(users - users2)   # {"Tom", "Alice"}

# возвращает все элементы обоих множеств за исключением общих
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

users3 = users.symmetric_difference(users2)
print(users3)   # {"Tom", "Alice", "Sam", "Kate"}

users4 = users ^ users2
print(users4)   # {"Tom", "Alice", "Sam", "Kate"}

# Отношения между множествами
# является ли текущее множество подмножеством
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}

print(users.issubset(superusers))   # True
print(superusers.issubset(users))   # False

# текущее множество является надмножеством
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}

print(users.issuperset(superusers))   # False
print(superusers.issuperset(users))   # True

# Тип frozen set является видом множеств, которое не может быть изменено
users = frozenset({"Tom", "Bob", "Alice"})
print(users)
