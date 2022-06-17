class Card:
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    value = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return '{} of {}'.format(Card.value[self.value], Card.suits[self.suit])


# c1 = Card(1, 3)
# print(c1)
