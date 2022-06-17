from Card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []

        for i in range(2, 15):
            for j in range(0, 4):
                self.new_card = Card(i, j)
                self.cards.append(self.new_card)

    def shuffle(self):
        new_order = random.sample(range(0, 52), 52)
        shuffled_deck = []

        for i in range(0, 52):
            shuffled_deck.append(self.cards[new_order[i]])

        self.cards = shuffled_deck

    # def draw_card(self):
    #     return self.cards[0]
