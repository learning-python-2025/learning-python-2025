'''
Создание кортежа
'''

tom = ("Tom", 23)
print(tom)     # ("Tom", 23)

tom = "Tom", 23
print(tom)     # ("Tom", 23)

tom = ("Tom",)

data = ["Tom", 37, "Google"]
tom = tuple(data)
print(tom)      # ("Tom", 37, "Google")


# tom = ("Tom", 37, "Google")
# print(len(tom))     # 3

'''
Обращение к элементам кортежа
'''

# tom = ("Tom", 37, "Google", "software developer")
# print(tom[0])       # Tom
# print(tom[1])       # 37
# print(tom[-1])      # software developer

'''
кортеж - неизменяемый тип (immutable)
'''
# tom[1] = "Tim" # Error

x = ("Tom", 37, "Google", "software developer")
y = list(x)
y[1] = 50
x = tuple(y)

# print(x)

x = ("Tom", 37, "Google", "software developer")
y = list(x)
y.append(50)
x = tuple(y)

# print(x)

thistuple = ("Tom", 37, "Google", "software developer")
y = (50,)
thistuple += y

print(thistuple)


'''
Разложение кортежа
'''

# name, age, company, position = ("Tom", 37, "Google", "software developer")
# print(name)         # Tom
# print(age)          # 37
# print(position)     # software developer
# print(company)     # Google

my_tuple = ("Tom", 37, "Google", "software developer")

(Name, Age, *Who) = my_tuple

print(Name)
print(Age)
print(Who)

my_tuple = ("Tom", 37, "Google", "software developer")

(Name, *Age, Who) = my_tuple

print(Name)
print(Age)
print(Who)

'''
Получение подкортежей
'''
tom = ("Tom", 37, "Google", "software developer")

# получем подкортеж с 1 по 3 элемента (не включая)
print(tom[1:3])     # (37, "Google")

# получем подкортеж с 0 по 3 элемента (не включая)
print(tom[:3])     # ("Tom", 37, "Google")

# получем подкортеж с 1 по послдений элемент
print(type(tom[1:]))     # (37, "Google", "software developer")


'''
Кортеж как параметр и результат функций
'''


def get_user():
    name = "Tom"
    age = 22
    company = "Google"
    return name, age, company


user = get_user()
print(user)     # ("Tom", 37, "Google")
print(type(user))


def print_person(name, age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")


tom = ("Tom", 22)
print_person(*tom, "Microsoft")     # Name: Tom  Age: 22  Company: Microsoft

bob = ("Bob", 41, "Apple")
print_person(*bob)      # Name: Bob  Age: 41  Company: Apple

'''
Перебор кортежей
'''

tom = ("Tom", 22, "Google")
for item in tom:
    print(item)

tom = ("Tom", 22, "Google")

i = 0
while i < len(tom):
    print(tom[i])
    i += 1

'''Проверка наличия значения'''

# user = ("Tom", 22, "Google")
# name = "Tom"
# if name in user:
#     print("Пользователя зовут Tom")
# else:
#     print("Пользователь имеет другое имя")

'''
Методы и функции по работе с кортежами

.index() — используется для вывода индекса элемента.
.count() — используется для подсчета количества элементов в кортеже.
sum() — складывает все элементы кортежа.
min() — показывает элемент кортежа с наименьшим значением.
max() — показывает элемент кортежа с максимальным значением.
len() — показывает количество элементов кортежа.
'''

tom = (11, 22, 33)
print(tom.count(22))

print(tom.index(22))

print(sum(tom))

print(min(tom))

print(max(tom))

print(len(tom))
