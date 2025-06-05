'''
Цикл while
while условное_выражение:
   инструкции

'''
# 1
number = 1

while number < 5:
    print(f"number = {number}")
    number += 1
print("End programm")

# 2
number = 1

while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")

# 3
number = 10

while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")

'''
Цикл for
for переменная in набор_значений:
    инструкции

'''
# 1
message = "Hello"

for c in message:
    print(c)

# 2
for n in range(10):
    print(n, end=" ")  # 0 1 2 3 4 5 6 7 8 9

for n in range(4, 10):
    print(n, end=" ")  # 4 5 6 7 8 9

for n in range(0, 10, 2):
    print(n, end=" ")  # 0 2 4 6 8

# 3
message = "Hello"
for c in message:
    print(c)
else:
    print(f"Последний символ: {c}. Цикл завершен")
# инструкция не имеет отступа, поэтому не относится к else
print("Работа программы завершена")

'''
Вложенные циклы

'''
# 1
i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1

# 2
for c1 in "ab":
    for c2 in "ba":
        print(f"{c1}{c2}")

'''
Выход из цикла. break и continue
Блок else НЕ будет выполняться, если цикл остановлен оператором break.
'''
# 1
number = 0
while number < 5:
    number += 1
    if number == 3:    # если number = 3, выходим из цикла
        break
    print(f"number = {number}")

# 2
number = 0
while number < 5:
    number += 1
    if number == 3:    # если number = 3, переходим к новой итерации цикла
        continue
    print(f"number = {number}")

'''
Заявление о пропуске
'''

for x in [0, 1, 2]:
    pass
