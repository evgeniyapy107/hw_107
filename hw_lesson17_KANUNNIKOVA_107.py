# Ex 1 Калькулятор
class Calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum_(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def mult(self):
        return self.num1 * self.num2

    def div(self):
        while self.num2 == 0:
            k = int(input('введите значение не равное 0: '))
            return self.num1 / k
        else:
            return self.num1 / self.num2


a = int(input())
b = int(input())
ab_ = Calc(a, b)
c = input('действие (+, -, *, /)?: ')
if c == '+':
    print(ab_.sum_())
elif c == '-':
    print(ab_.minus())
elif c == '*':
    print(ab_.mult())
elif c == '/':
    print(ab_.div())


# Ex 2 реализовать два метода в классе

class Example:
    def func1(self, obj):
        if isinstance(obj, str):
            vowels = 'aeyuio'
            consonants = 'bcdfghjklmnpqrstxvz'
            vow = 0
            cons = 0
            vow_list = []
            cons_list = []
            for letter in obj:
                if letter in vowels:
                    vow += 1
                    vow_list.append(letter)
                elif letter in consonants:
                    cons += 1
                    cons_list.append(letter)
            result = vow * cons
            if result <= len(obj):
                return vow_list
            else:
                return cons_list
        elif isinstance(obj, int):
            sum_ = 0
            for num in str(obj):
                if int(num) % 2 == 0:
                    sum_ += int(num)
                else:
                    pass
            result2 = sum_ * self.func2(obj)
            return result2

    def func2(self, obj):
        return len(str(obj))


k = Example()
m = input('enter string or number: ')
print(k.func1(m))
