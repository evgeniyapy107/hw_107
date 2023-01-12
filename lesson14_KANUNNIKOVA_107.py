# Ex 1
# функция на определение индекса массы тела

def bmi(weight, height):
    bmi_ = weight / height ** 2
    if bmi_ <= 16:
        return 'выраженный дефицит массы тела'
    elif 16 < bmi_ < 18.5:
        return 'недостаточная масса тела'
    elif 18.5 < bmi_ < 25:
        return 'норма'
    elif 25 < bmi_ < 30:
        return 'избыточная масса тела'
    elif 30 < bmi_ < 35:
        return 'ожирение 1 степени'
    elif 35 < bmi_ < 40:
        return 'ожирение 2 степени'
    elif bmi_ >= 40:
        return 'ожирение 3 степени'


m = int(input('введите ваш вес: '))
h = int(input('введите ваш рост: '))
print(bmi(m, h))

bmi(m, h)


# Ex 2
# функция на определение фигуры по количеству сторон

def figure(x):
    if 3 <= x <= 10:
        return f'{x}-угольник'
    else:
        return 'такой фигуры нет'


a = int(input('введите количество сторон фигуры'))
print(figure(a))
figure(a)


# Ex 3
# функция на определение следующей даты

def month(y):
    if y == 1:
        return 'января'
    elif y == 2:
        return 'февраля'
    elif y == 3:
        return 'марта'
    elif y == 4:
        return 'апреля'
    elif y == 5:
        return 'мая'
    elif y == 6:
        return 'июня'
    elif y == 7:
        return 'июля'
    elif y == 8:
        return 'августа'
    elif y == 9:
        return 'сентября'
    elif y == 10:
        return 'октября'
    elif y == 11:
        return 'ноября'
    elif y == 12:
        return 'декабря'


def date(x, y, z):
    if 1 <= x <= 30 and y in [1, 3, 5, 7, 8, 10, 12]:
        return '(x + 1), month(y), z'
    elif 1 <= x <= 29 and y in [4, 6, 9, 11]:
        return '(x + 1), month(y), z'
    elif x == 31 and y in [1, 3, 5, 7, 8, 10]:
        return '1, month(y + 1), z'
    elif x == 30 and y in [4, 6, 9, 11]:
        return '1, month(y + 1), z'
    elif x == 28 and y == 2 and z % 4 != 0:
        return '1, month(y + 1), z'
    elif x == 28 and y == 2 and z % 4 == 0:
        return '(x + 1), month(y), z'
    elif x == 31 and y == 12:
        return '1, 1, (z + 1)'


day_ = int(input('введите число месяца: '))
month_ = int(input('введите номер месяца: '))
year_ = int(input('введите год: '))

print(date(day_, month_, year_))
date(day_, month_, year_)


# Ex 4
# функция на суммы покупки по количеству товаров

def sum_(count_):
    price1 = 2.95
    price2 = 10.95
    return price1 + (count_ - 1) * price2


k = int(input('введите количество товаров: '))
print(f'{sum_(k)} - сумма к оплате')


# Ex 5
# функция на вычисление результата дроби

def func_(x1, y1):
    m_ = x1 % y1
    n_ = y1 % m_
    x1 = x1 / n_
    y1 = y1 / n_
    return x1 / y1


numer_ = int(input('введите значение числителя: '))
denom_ = int(input('введите значение знаменателя: '))
print(func_(numer_, denom_))
func_(numer_, denom_)


# Ex 6

def fun(list_):
    list_str = []
    a1 = list_[-1:0]
    a2 = list_.sort(reverse=True)
    a3 = list_.sort()
    a4 = list_[2:7]
    print(a1, a2, a3, a4)

    for i in list_:
        if type(i) != int:
            list_str.append(i)
            print(list_str)


l_ = [1, 5, 'fg', 45, 'ree', 'gg', 2, 2, 'ggl', 9, 3]
print(fun(l_))
fun(l_)


# ex 8
def f(list1):
    count1 = 0
    for i in list1:
        if type(i) == list:
            count1 += 1
        return count1


ms = [25, [1, 2, 3], 4, [2, 5], [2, 33]]
print(f(ms))


# ex 9
def anagram(word1, word2):
    word1_list = list(word1)
    word1_list.sort()
    word2_list = list(word2)
    word2_list.sort()
    if word1_list == word2_list:
        return 'слово является анаграммой'


w1 = 'нитка'
w2 = 'ткани'
print(anagram(w1, w2))
anagram(w1, w2)

# p.s все что успела)
