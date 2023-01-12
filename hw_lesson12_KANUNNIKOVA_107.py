# HW
def func(x):
    if type(x) == tuple:
        for i in x:
            if type(i) == str:
                print(f'длина слова {i} - {len(i)}')
    elif type(x) == list:
        letter = 0
        num = 0
        for j in x:
            if type(j) == str:
                letter += 1
            else:
                num += 1
        print(f'колличесвто букв в списке - {letter}, колличесвто чисел в списке - {num}')
    elif type(x) == int:
        odd = 0
        while x > 0:
            if x % 2 == 1:
                odd += 1
            x = x // 10
        print(f'колличесвто нечетных цифр в числе - {odd}')
    elif type(x) == str:
        print(f'{len(x)} букв в строке')


a1 = ('hello', 'winter', 'snow')
a2 = [1, 'g', 'f', 's', 4, 3, 'v', 2, 2]
a3 = 1245
a4 = 'christmas'

func(a4)


# Ex. 2
def rectangle_s(a, b):
    return a * b


def triangle_s(c, h):
    return (1 / 2) * c * h


def circle_s(r):
    return 3.14 * r ** 2


figure = input('выберите фигуру (прямоугольник, треугольник, круг): ')
if figure == 'прямоугольник':
    a_ = int(input('задайте длину стороны 1: '))
    b_ = int(input('задайте длину стороны 2: '))
    print(rectangle_s(a_, b_))
elif figure == 'треугольник':
    c_ = int(input('задайте длину стороны: '))
    h_ = int(input('задайте длину высоты: '))
    print(triangle_s(c_, h_))
elif figure == 'круг':
    r_ = int(input('задайте радиус: '))
    print(circle_s(r_))

# Ex. 3
import random


def list_function(start, end):
    list_ = [random.randint(start, end) for i in range(10)]
    print(list_)


start = int(input('введите начало диапазона: '))
end = int(input('введите конец диапазона: '))

list_function(start, end)


# Ex. 6
def y(x):
    if -5 <= x <= 5:
        return x ** 2
    elif x < -5:
        return 2 * abs(x) - 1
    elif x > 5:
        return 2 * x


for t in range(-10, 11):
    print(y(t))
