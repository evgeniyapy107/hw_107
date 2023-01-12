# practice dir, Ex.5
my_str = 'Merry Christmas!'
first_word = my_str[:my_str.find(' ')]
second_word = my_str[my_str.find(' ') + 1:]
my_str_new = second_word + first_word
print(my_str_new)
print(my_str_new.replace('1', 'one'))

# home work, Ex.1
str_1 = 'family'
print(str_1[2])     # третий символ (отсчет от 0)
print(str_1[-2])    # предпоследний символ (второй с конца)
print(str_1[0:5])   # первые 5 символов ( от 0 до 5, не включая последний)
print(str_1[:-2])   # от начала до предпоследнего
print(str_1[::2])   # все четные
print(str_1[1::2])  # все нечетные
print(str_1[::-1])  # строка в обратном порядке
print(str_1[::-2])  # строка в обратном порядке через один символ
print(len(str_1))   # длина строки
