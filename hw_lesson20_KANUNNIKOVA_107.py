
class CardDeck:
    def __init__(self):
        self.start = 0
        self.stop = 52

    @classmethod
    def deck_(cls):
        card_suit = ['Пик', 'Треф', 'Червей', 'Бубен']
        card_name = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
        card_list = []
        for i in card_name:
            for j in card_suit:
                card_list.append(i + ' ' + j)
        card_dict = dict(zip([n for n in range(1, 53)], card_list))
        return card_dict

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        else:
            cards = CardDeck.deck_()
            self.start += 1
            return cards[self.start]

    def __iter__(self):
        return self


deck = CardDeck()
while True:
    print(next(deck))


# ex 2
def infinite(lst, tries):
    lst_iter = iter(lst)
    count = 1
    while count <= tries:

        try:

            iter_ = next(lst_iter)

            print(iter_)

            count += 1

        except StopIteration:

            lst_iter = iter(lst)

    else:

        pass


m = [1, 4, 5, 3, 7, 8]

n = 10

print(infinite(m, n))
