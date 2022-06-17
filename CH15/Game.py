from Player import Player
from Deck import Deck


class Game:
    def __init__(self):
        self.name1 = input("Enter Player 1 Name: ")
        self.name2 = input("Enter Player 2 Name: ")
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player(self.name1, self.deck.cards[:27])
        self.player2 = Player(self.name2, self.deck.cards[27:])

    def play_game(self):
        while not self.check_winner():
            self.player1.pick_card()
            self.player2.pick_card()

            result = self.compare_cards(self.player1.curr_card.value, self.player2.curr_card.value)

            if result == 0:
                self.player1.hand.append(self.player1.curr_card)
                self.player1.hand.append(self.player2.curr_card)
                print("Player1 wins this round.")
            elif result == 1:
                self.player2.hand.append(self.player2.curr_card)
                self.player2.hand.append(self.player1.curr_card)
                print("Player2 wins this round.")
            else:
                self.war()

            self.player1.curr_card = None
            self.player2.curr_card = None
            print("Player1 has {} cards".format(len(self.player1.hand)))
            print("Player2 has {} cards".format(len(self.player2.hand)))
            print()


        print("The winner is {}".format(self.determine_winner()))

    def compare_cards(self, c1, c2):
        print("Player1: {} vs Player2: {}".format(c1, c2))

        if c1 > c2:
            return 0
        elif c1 < c2:
            return 1
        else:
            return 2

    def check_winner(self):
        if len(self.player1.hand) == 0:
            return True
        elif len(self.player2.hand) == 0:
            return True
        else:
            return False

    def determine_winner(self):
        if len(self.player1.hand) == 0:
            return self.player2.name
        else:
            return self.player1.name

    def war(self):

        print("WAR!!!")

        # Make sure players have enough cards to play
        if len(self.player1.hand) < 2:
            self.player1.hand = []

        elif len(self.player2.hand) < 2:
            self.player2.hand = []

        else:
            p1_init_card = self.player1.curr_card
            self.player1.pick_card()
            p1_down = self.player1.curr_card
            self.player1.pick_card()
            p1_war = self.player1.curr_card

            p2_init_card = self.player2.curr_card
            self.player2.pick_card()
            p2_down = self.player2.curr_card
            self.player2.pick_card()
            p2_war = self.player2.curr_card

            result = self.compare_cards(p1_war.value, p2_war.value)

            if result == 0:
                self.player1.hand.append(p1_init_card)
                self.player1.hand.append(p1_down)
                self.player1.hand.append(p1_war)
                self.player1.hand.append(p2_init_card)
                self.player1.hand.append(p2_down)
                self.player1.hand.append(p2_war)
                print("Player1 wins this round.")
            elif result == 1:
                self.player2.hand.append(p1_init_card)
                self.player2.hand.append(p1_down)
                self.player2.hand.append(p1_war)
                self.player2.hand.append(p2_init_card)
                self.player2.hand.append(p2_down)
                self.player2.hand.append(p2_war)
                print("Player2 wins this round.")
            else:
                if p1_war.suit > p2_war.suit:
                    self.player1.hand.append(p1_init_card)
                    self.player1.hand.append(p1_down)
                    self.player1.hand.append(p1_war)
                    self.player1.hand.append(p2_init_card)
                    self.player1.hand.append(p2_down)
                    self.player1.hand.append(p2_war)
                    print("Player1 wins this round.")
                else:
                    self.player2.hand.append(p1_init_card)
                    self.player2.hand.append(p1_down)
                    self.player2.hand.append(p1_war)
                    self.player2.hand.append(p2_init_card)
                    self.player2.hand.append(p2_down)
                    self.player2.hand.append(p2_war)
                    print("Player2 wins this round.")


g = Game()
g.play_game()


