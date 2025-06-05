'''
Условная конструкция if

if логическое_выражение:
    инструкции
[elif логическое выражение:
    инструкции]
[else: 
    инструкции]
'''


# language = "english"
# if language == "english1":
#     print("Hello")
# print("End")

# language = "english"
if language == "english1":
    print("Hello")
    print("End")


# language = "russian"
# if language == "english":
#     print("Hello")
# else:
#     print("Bay")
#     print("End")


# language = "russian"
# if language == "english":
#     print("Hello")
#     print("World")
# else:
#     print("Bay")
#     print("World")

# language = "german"
# if language == "english":
#     print("Hello")
#     print("World")
# elif language == "german":
#     print("Hallo")
#     print("Welt")
# else:
#     print("Bay")
#     print("World")

language = "german"
if language == "english":
    print("Hello")
elif language == "german":
    print("Hallo")
elif language == "french":
    print("Salut")
else:
    print("Bay")


# language = "english"
# daytime = "morning"
# if language == "english1":
#     print("English")
#     if daytime == "morning":
#         print("Good morning")
#     else:
#         print("Good evening")

# language = "english"
# daytime = "morning"
# if language == "english1":
#     print("English")
# if daytime == "morning":
#     print("Good morning")
# else:
#      print("Good evening")

language = "english"
daytime = "morning"
if language == "english":
    if daytime == "morning":
        print("Good morning")
    else:
        pass
else:
    if daytime == "morning":
        print("Доброе утро")
    else:
        print("Добрый вечер")

# # Заявление о пропуске
a = 33
b = 200

if b > a:
    pass
