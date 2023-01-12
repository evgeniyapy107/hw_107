# Home work
import random

x_num = random.randint(1, 10)                                   # компьютер генерирует числа от 1 до 10
list = ['красный', 'черный']                                    # создаем список необходимых цветов
x_color = random.choice(list)                                   # компьютер генерирует цвет из списка list
i = 0                                                           # вводим переменную i для счета попыток
while i < 5:                                                    # пока количество попыток меньше 5
    user_num = int(input('введите число от 1 до 10: '))         # пользователь вводит число и цвет
    user_color = input('введите цвет - красный или черный: ')
    if user_num == x_num and user_color == x_color:             # если значения пользователя и компьютера равны
        print('Верно, Вы выиграли!')                            # выводим print
        break                                                   # и останавливаем цикл while
    elif user_num != x_num or user_color != x_color:            # иначе - выводим print и переходим к следующей попытке
        print('не верно!')
    i += 1                                                      # счетчик попыток, +1 после каждой итерации цикла
if user_num != x_num or user_color != x_color:
    print('вы проиграли! верный ответ - ', x_num, x_color)      # выводим верный ответ
