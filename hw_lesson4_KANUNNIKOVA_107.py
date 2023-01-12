# practice 4
# Ex. 5
import random

player_one = random.randint(1, 3)
player_two = int(input('Введите 1 (камень), 2 (ножницы) или 3 (бумага): '))
print(player_one, 'против', player_two)
if player_one == player_two:
    print('ничья')
elif player_two - player_one == 1:
    print('вы проиграли')
elif player_one - player_two == 1:
    print('вы выиграли')
elif player_one == 3 and player_two == 1:
    print('вы проиграли')
elif player_one == 1 and player_two == 3:
    print('вы выиграли')
elif player_two > 3 or player_two < 1:
    print('неверное число')

# Ex. 6
x = int(input('введите первое число: '))
y = int(input('введите второе число: '))
xy_val = (x < y)
if xy_val:
    print(x, 'меньше', y)

# Ex. 7
a = int(input('введите длину первой стороны треугольника: '))
b = int(input('введите длину второй стороны треугольника: '))
c = int(input('введите длину третьей стороны треугольника: '))
if (a + b) > c or (a + c) > b or (b + c) > a:
    print('треугольник существует')
else:
    print('треугольник не существует')

# Ex. 8
num_1 = int(input('ведите первое число: '))
num_action = input('введите действие( +, -, *, /): ')
num_2 = int(input('введите второе число: '))
print(num_1, num_action, num_2, '=')
if num_action == '+':
    print(num_1 + num_2)
elif num_action == '-':
    print(num_1 - num_2)
elif num_action == '*':
    print(num_1 * num_2)
elif num_action == '/':
    print(num_1 / num_2)

# Ex. 9
# определим является ли введенное пользователем слово - "Mister"
# через предикат s.capitalize()
string = input('введите слово')
is_mister = (string.capitalize() == 'Mister')
print(is_mister)

# Ex. 10
armor_color = input('введите цвет доспехов (red, yellow, black)')
shield_color = input('введите цвет щита (red, yellow, black)')
is_knight = (armor_color != 'red' and shield_color == 'black')
print(is_knight)

# HW,
# Ex. 1
# лотерея с подбрасыванием монетки
import random

you_var = int(input('введите 1 -орел или 2 - решка: '))
coin_var = random.randint(1, 2)
if coin_var == 1 and coin_var == you_var:
    print('орел, вы выиграли!')
elif coin_var == 2 and coin_var == you_var:
    print('решка, вы выиграли!')
else:
    print('вы проиграли!')

# Ex. 2
# определим знак зодиака по дате рождения
birthday_day = int(input('введите какого числа вы родились(1-31): '))
month_day = int(input('введите месяц вашего рождения от 1 до 12: '))
if (birthday_day >= 22 and month_day == 12) or (birthday_day <= 20 and month_day == 1):
    print('козерог')
elif (birthday_day >= 21 and month_day == 1) or (birthday_day <= 18 and month_day == 2):
    print('водолей')
elif (birthday_day >= 19 and month_day == 2) or (birthday_day <= 20 and month_day == 3):
    print('рыба')
elif (birthday_day >= 21 and month_day == 3) or (birthday_day <= 20 and month_day == 4):
    print('овен')
elif (birthday_day >= 21 and month_day == 4) or (birthday_day <= 21 and month_day == 5):
    print('телец')
elif (birthday_day >= 22 and month_day == 5) or (birthday_day <= 21 and month_day == 6):
    print('близнецы')
elif (birthday_day >= 22 and month_day == 6) or (birthday_day <= 22 and month_day == 7):
    print('рак')
elif (birthday_day >= 23 and month_day == 7) or (birthday_day <= 23 and month_day == 8):
    print('лев')
elif (birthday_day >= 24 and month_day == 8) or (birthday_day <= 23 and month_day == 9):
    print('дева')
elif (birthday_day >= 24 and month_day == 9) or (birthday_day <= 23 and month_day == 10):
    print('весы')
elif (birthday_day >= 24 and month_day == 10) or (birthday_day <= 22 and month_day == 11):
    print('скорпион')
else:
    print('стрелец')

# Ex. 3
# определим скидку по дисконтной карте в зависимости от суммы покупок
amount_of_purchases = int(input('введите сумму покупок: '))
if 500 <= amount_of_purchases <= 1000:
    print('ваша скидка - 5%')
elif 1000 < amount_of_purchases <= 5000:
    print('ваша скидка - 10%')
elif amount_of_purchases > 5000:
    print('ваша скидка - 15%')
else:
    print('у вас нет скидки')
