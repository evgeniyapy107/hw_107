# Ex. 1
# перемножить все нечетные значения в диапазоне от 1 до 100
pr = 1
for i in range(1, 101, 2):
    pr *= i
print(pr)

# Ex. 2
# Записать в массив все числа в диапазоне от 1 до 500 кратные 5
arr = []
for i in range(1, 501):
    if i % 5 == 0:
        arr.append(i)
print(arr)

# Ex. 3
# Вывести на экран все четные значения в диапазоне от 1 до 497
for i in range(1, 498):
    if i % 2 == 0:
        print(i)

# Ex. 4
# Дан массив чисел. Если число встречается более двух раз, то добавить его в новый массив

my_arr = [1, 2, 4, 4, 7, 15, 4, 15]
new_arr = []
for i in my_arr:
    if my_arr.count(i) > 2:
        new_arr.append(i)
print(new_arr)

# Творческое задание
# не было времени придумывать условие, просто для себя прорешала несколько задач на методы массивов)
# Ex.
arr_x = [1, 2, 3, 7, 14, 22]
for i in arr_x:
    print(arr_x.index(i))

# Ex.
arr_x = [1, 2, 3, 5, 14, 9]
for i in arr_x:
    if i == 5:
        print(arr_x.index(i))

# Ex.
arr_x = [1, 2, 7, 7, 5, 12, 2, 2, 9]
for i in arr_x:
    print(arr_x.count(i))

# Ex.
arr_x = [1, 2, 7, 5, 3, 2, 2, 9]
for i in arr_x:
    if i == 7:
        print(arr_x.count(i))

# Ex.
arr_ = [10, 24, 71, 5, 71]
for i in arr_:
    arr_.remove(71)
    print(arr_)


