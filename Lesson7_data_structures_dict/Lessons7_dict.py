'''
Создание словаря

dictionary = { ключ1:значение1, ключ2:значение2, ....}
'''

users = {1: "Tom", 2: "Bob", 3: "Bill"}

emails = {"tom@gmail.com": "Tom",
          "bob@gmai.com": "Bob", "sam@gmail.com": "Sam"}

objects = {1: "Tom", "2": True, 3: 100.6}

objects = {}
objects = dict()

'''
Преобразование в  словарь

'''
users_list = [
    ["+111123455", "Tom"],
    ["+384767557", "Bob"],
    ["+958758767", "Alice"]
]
users_dict = dict(users_list)
# {"+111123455": "Tom", "+384767557": "Bob", "+958758767": "Alice"}
print(users_dict)


users_tuple = (
    ("+111123455", "Tom"),
    ("+384767557", "Bob"),
    ("+958758767", "Alice")
)
users_dict = dict(users_tuple)
print(users_dict)

'''
Получение и изменение элементов
'''

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}

# получаем элемент с ключом "+11111111"
print(users["+11111111"])      # Tom

# установка значения элемента с ключом "+33333333"
users["+33333333"] = "Bob Smith"
print(users["+33333333"])   # Bob Smith

users["+4444444"] = "Sam"

user = users["+4444444"]    # KeyError

key = "+4444444"
if key in users:
    user = users[key]
    print(user)
else:
    print("Элемент не найден")

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
# get(key): возвращает из словаря элемент с ключом key. Если элемента с таким ключом нет, то возвращает значение None
user1 = users.get("+55555556")
print(user1)    # Alice

# get(key, default): возвращает из словаря элемент с ключом key.
# Если элемента с таким ключом нет, то возвращает значение по умолчанию default
user2 = users.get("+33333333", "Unknown user")
print(user2)    # Bob
user3 = users.get("+44444444", "Unknown user")
print(user3)    # Unknown user

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
'''
Удаление элементов
'''

del users["+55555555"]
print(users)    # { "+11111111": "Tom", "+33333333": "Bob"}

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}

key = "+55555555"
if key in users:
    del users[key]
    print(f"Элемент с ключом {key} удален")
else:
    print("Элемент не найден")

# pop(key): удаляет элемент по ключу key и возвращает удаленный элемент. Если элемент с данным ключом отсутствует, то генерируется исключение KeyError
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
key = "+55555555"
user = users.pop(key)
print(user)     # Alice

# pop(key, default): удаляет элемент по ключу key и возвращает удаленный элемент. Если элемент с данным ключом отсутствует, то возвращается значение default
user = users.pop("+4444444", "Unknown user")
print(user)     # Unknown user

users.clear()

'''
Копирование и объединение словарей
'''

users = {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}
students = users.copy()
# {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}
print(students)


users = {"+1111111": "Tom", "+3333333": "Bob"}

users2 = {"+2222222": "Sam", "+6666666": "Kate"}
users.update(users2)

# {"+1111111": "Tom", "+3333333": "Bob", "+2222222": "Sam", "+6666666": "Kate"}
print(users)
print(users2)   # {"+2222222": "Sam", "+6666666": "Kate"}

users3 = users.copy()
users3.update(users2)
print(users3)
'''
Перебор словаря
'''

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key in users:
    print(f"Phone: {key}  User: {users[key]} ")

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
# items() возвращает кортеж
for key, value in users.items():
    print(f"Phone: {key}  User: {value} ")

# Перебор ключей
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key in users.keys():
    print(key)

# Перебор значений
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for value in users.values():
    print(value)

'''
Комплексные словари
'''
users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}

old_email = users["Tom"]["email"]
users["Tom"]["email"] = "supertom@gmail.com"
# { phone": "+971478745", "email": "supertom@gmail.com }
print(users["Tom"])

tom_skype = users["Tom"]["skype"]   # KeyError
# Проверить наличие ключа в словаре.
key = "skype"
if key in users["Tom"]:
    print(users["Tom"]["skype"])
else:
    print("skype is not found")

# get()
users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    }
}

tom_skype = users["Tom"].get("skype", "Undefined")
print(tom_skype)    # Undefined
