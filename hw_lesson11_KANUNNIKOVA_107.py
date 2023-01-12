def sum_(num_1, num_2):
    return num_1 + num_2


def minus_(num_1, num_2):
    return num_1 - num_2


def mult_(num_1, num_2):
    return num_1 * num_2


def div_(num_1, num_2):
    if num_2 != 0:
        return num_1 / num_2
    else:
        print('ошибка')


while True:

    n1 = int(input('введите число 1: '))
    operation = input('введите действие (+,-,*,/),для выхода из прогаммы нажмите "0": ')
    n2 = int(input('введите число 2: '))
    if operation == 0:
        break
    elif operation == '+':
        print(sum_(n1, n2))
    elif operation == '-':
        print(minus_(n1, n2))
    elif operation == '*':
        print(mult_(n1, n2))
    elif operation == '/':
        print(div_(n1, n2))
sum_(n1, n2)
minus_(n1, n2)
mult_(n1, n2)
div_(n1, n2)


# Ex. 2


def square_(a):
    p = 4 * a
    s = a ** 2
    d = int((2 * (a ** 2)) ** (1 / 2))
    return (p, s, d)


x = int(input('введите длину стороны квадрата: '))
print(square_(x))

square_(x)
