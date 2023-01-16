# Ex 1
import string


class Human:
    default_name = 'Piter'
    default_age = 35

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 25000
        self.__house = 'my house'

    def info(self):
        print(self.name)
        print(self.age)
        print(self.__money)
        print(self.__house)

    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_age)

    def earn_money(self, arg):
        self.__money += arg
        print(f'your balance is topped up on {arg}')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def buy_house(self, house, sale):
        pr = house.final_price(sale)
        if self.__money < pr:
            print('insufficient funds')
        else:
            self.__money -= pr


class House:
    def __init__(self, _area, _price):
        self._area = _area
        self._price = _price

    def final_price(self, sale):
        self._price = self._price - (self._price * sale / 100)
        return self._price


class SmallHouse(House):
    default_area = 45

    def __init__(self, _price):
        super().__init__(SmallHouse.default_area, _price)


Human.default_info()
person = Human('Jhon', 39)
person.info()
person.earn_money(1500)
person.info()

new_house = SmallHouse(32000)
person.buy_house(new_house, 17)
person.earn_money(1500)
person.buy_house(new_house, 17)


# Ex 2
class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        amount = 0
        for i in self.letters:
            amount += 1
        print(f'amount letters - {amount}')


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('en', string.ascii_uppercase)

    def is_en_letter(self, letter):
        if letter in self.letters:
            print(f'{letter} is letter by english alphabet!')
        else:
            print(f'english alphabet do not have {letter}!')

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        return 'Hello world'


alp = EngAlphabet()
alp.print()
print(alp.letters_num())
alp.is_en_letter('F')
alp.is_en_letter('Щ')
alp.example()


# Ex 3

class Tomato:
    states = {1: 'green', 2: 'yellow', 3: 'red'}

    def __init__(self, _index):
        self._index = _index
        self._state = 1

    def grow(self):
        if self._state < 3:
            self._state += 1
        print(self._state)

    def is_ripe(self):
        if self._state == 3:
            return True


class TomatoBush:
    def __init__(self, q):
        self.q = q
        self.tomatoes = [Tomato(_index) for _index in range(self.q)]

    def grow_all(self):
        for i in self.tomatoes:
            return i.grow()

    def all_are_ripe(self):
        for i in self.tomatoes:
            if i.is_ripe():
                if self.tomatoes.count(i) == self.q:
                    return True

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('gardener working')
        return self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print('not all tomatoes are ripe yet')

    @staticmethod
    def knowledge_base():
        print('gardening guide')


Gardener.knowledge_base()
vegetable = TomatoBush(9)
gardener = Gardener('Sun', vegetable)
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
