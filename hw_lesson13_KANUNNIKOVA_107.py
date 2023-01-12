list_ = ['12', 'hello', 'by', '45', '19', 'winter']
num = []
alph = []
for i in list_:
    if i.isalpha():
        i = str(i)
        alph.append(i)
        alph.sort(key=len)
    elif i.isdigit():
        i = int(i)
        num.append(i)
        num.sort()

print(alph)
print(num)
list_sort = alph + num
print(list_sort)

f = open('list.txt', 'w')
for n in str(list_sort):
    f.write(n)
f.close()

