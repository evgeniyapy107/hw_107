# Ex. 1
# Вычислить сумму кортежа с числами от 0 до 9

a = tuple(range(10))            # создаем кортеж с пом ф-ции tuple и последоват-ти (range(10))
print(a)                        # выводим на печать
print(sum(a))                   # считаем сумму с пом-ю ф-ции sum

# Ex. 2 вычислить кол-во повторяющихся букв

long_word = ('t', 't', 'a', 'i', 'i', 'a', 'i',             # с пом-ю цикла итерируемся по множеству set(long_word)
             'i', 'i', 't', 't', 'a', 'i', 'i', 'i',
             'i', 'i', 't', 'i')
for i in set(long_word):
    print(f'{i} - {long_word.count(i)}')                    # находим кол-во повторений с пом-ю метода count


# Ex. 3

week_temp = (26, 29, 34, 32, 28, 26, 23)                 # вычисляем длину (колл-во элементов) кортежа с пом-ю ф-ции len
sum_temp = sum(week_temp)                                # считаем сумму с пом-ю ф-ции sum
days = len(week_temp)
mean_temp = sum_temp / days
print(int(mean_temp))

