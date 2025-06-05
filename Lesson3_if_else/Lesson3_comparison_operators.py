'''
Условные выражения

Операции сравнения
==                      Возвращает True, если оба операнда равны. Иначе возвращает False.

!=                      Возвращает True, если оба операнда НЕ равны. Иначе возвращает False.

> (больше чем)          Возвращает True, если первый операнд больше второго.

< (меньше чем)          Возвращает True, если первый операнд меньше второго.

>= (больше или равно)   Возвращает True, если первый операнд больше или равен второму.

<= (меньше или равно)   Возвращает True, если первый операнд меньше или равен второму.
могут сравнивать различные объекты - строки, числа, логические значения, оба операнда операции должны представлять один и тот же тип
'''
# a = 5
# b = 6
# result = 5 == 6  # сохраняем результат операции в переменную
# print(result)  # False - 5 не равно 6
# print(a != b)  # True
# print(a > b)  # False - 5 меньше 6
# print(a < b)  # True
 
# bool1 = True
# bool2 = False
# print(bool1 == bool2)  # False - bool1 не равно bool2

'''
Логические операции
'''
# # and (логическое умножение)  x and y
# age = 20
# weight = 58
# result = age > 21 and weight == 58
# print(result)  # True

# result = 4 and "w"
# print(result)  # w, так как 4 равно True, поэтому возвращается значение последнего операнда
 
# result = 0 and "w"
# print(result)  # 0, так как 0 эквивалентно False


# # or (логическое сложение) x or y
# age = 22
# isMarried = False
# result = age > 21 or isMarried
# print(result)  # True, так как выражение age > 21 равно True 

# result = 4 or "w"
# print(result)  # 4, так как 4 эквивалентно True, поэтому возвращается значение первого операнда
 
# result = 0 or "w"
# print(result)  # w, так как 0 эквивалентно False, поэтому возвращается значение последнего операнда

# # not (логическое отрицание)
# age = 22
# isMarried = False
# print(not age > 21)  # False
# print(not isMarried)  # True
# print(not 4)  # False
# print(not 0)  # True

# # Оператор in 	
# # значение in набор_значений

message = "hello world!"
hello = "hello"
print(hello in message)  # True - подстрока hello есть в строке "hello world!"
 
gold = "gold"
print(gold in message)  # False - подстроки "gold" нет в строке "hello world!"

message = "hello world!"
hello = "hello"
print(hello not in message)  # False

# # not in 

gold = "gold"
print(gold not in message)  # True

