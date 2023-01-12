# Home work
# Ex.1
list_ = [15, 48, 'hello', 6, 19, 'world']
for i in list_:
    if type(i) == int and i % 2 == 0:
        sum_ = i % 10 + i // 10
        print(sum_)
    elif type(i) == int and i % 2 != 0:
        list_[list_.index(i)] = 1
        print(list_)
    elif type(i) == str:
        list_2 = ['a', 'o', 'u', 'y', 'e', 'i']
        vowels = 0
        consonants = 0
        for j in i:
            if j in list_2:
                vowels += 1
            else:
                consonants += 1
        print(vowels, consonants)

# Practice
# Ex.4
a = [5, [1, 2], 2, 'r', 4, 'ee']
b = [4, 'we', 'ee', 3, [1, 2]]
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
print(c)

# Ex.5
a = [4, 6, 'py', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]
a.extend(b)
print(a)
a.insert(3, 6)
print(a)
count_ = 0
for i in a:
    if type(i) is str:
        a.remove(i)
print(a)
print(len(a))






