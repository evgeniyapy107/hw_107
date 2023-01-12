# Ex 1
try:
    a = input('введите значение 1: ')
    b = input('введите значение 2: ')
    result = int(a) / int(b)
except ZeroDivisionError:
    print('попытка деления на ноль, повторите ввод.')
    a = input('введите значение 1: ')
    b = input('введите значение 2: ')
except TypeError:
    print('невозможно выполнить операцию')
finally:
    print('программа завершена')
