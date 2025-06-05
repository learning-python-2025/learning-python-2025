# Упражнение 1
# Определите класс Rectangle, который представляет прямоугольник.
# Через конструктор класс принимает ширину и длину и сохраняет
# их в атрибутах width и length соответственно.
# Также этом классе определите метод area, который
#  возвращает площадь прямоугольника, и метод perimeter,
# который возвращает периметра прямоугольника.

# После создания класса определите несколько объектов класса Rectangle
# и продемонстрируйте работу его методов.
class Rectangle:

    def __init__(self, width, length):
        self.width = width        # ширину
        self.length = length     # длина

    def area(self):
        area = self.width * self.length
        print(f"area: {area} ")

    def perimeter(self):
        perimeter = 2*(self.length + self.width)
        print(f"perimeter: {perimeter} ")


Rect_ = Rectangle(5, 5)
Rect_.area()
Rect_.perimeter()
# Упражнение 2
# Создайте класс BankAccount, который представляет банковский счет.
# Определите в этом классе атрибуты account_number и balance,
# которые представляют номер счета и баланс.
# Через параметры конструктора передайте этим атрибутам начальные значения.

# Также в классе определите метод add, который принимает некоторую сумму
# и добавляет ее на баланс счета.
# И определите метод withdraw, который принимает некоторую сумму и снимает ее с баланса.
# При этом с баланса нельзя снять больше, чем имеется. Если на балансе недостаточно средств,
# то пользователю должно выводиться соответствующее сообщение.


class BankAccount:
    def __init__(self, num, summa):
        self.acc_num = num
        self.balance = summa
        print('Acc was create. Balance', summa)

    def add(self, summa):
        self.balance = self.balance + summa
        print('Balance', self.balance)

    def withdraw(self, summa):
        if self.balance >= summa:
            self.balance = self.balance - summa
            print('Balance', self.balance)
        else:
            print('Netu')


acc = BankAccount('123456789', 1000)
acc.add(200)
acc.withdraw(600)
acc.withdraw(700)
print(type(acc))
