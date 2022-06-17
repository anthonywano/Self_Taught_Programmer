class Player:
    def __init__(self, name, cards):
        self.name = name
        self.hand = cards
        self.curr_card = None

    def pick_card(self):
        if len(self.hand) > 0:
            self.curr_card = self.hand[0]
            self.hand.pop(0)

