class Example:
    def func1(self, user):

        if isinstance(user, str):
            vow = 0
            cons = 0
            vowels = 'аоуеиыэюя'
            consonants = 'бвгджзйклмнпрстфхцчшщ'
            user_vow = []
            user_cons = []
            for letter in user.lower():
                if letter in vowels:
                    vow += 1
                    user_vow.append(letter)
                elif letter in consonants:
                    cons += 1
                    user_cons.append(letter)
            result = vow * cons
            if result <= self.func2(user):
                print(user_vow)
            else:
                print(user_cons)
        elif isinstance(user, int):

            sum_ = 0
            for num in str(user):
                if int(num) % 2 == 0:
                    sum_ += int(num)
            result2 = sum_ * self.func2(user)
            print(result2)

    def func2(self, user):
        return len(str(user))


obj = Example()
print(obj.func1(45673))

