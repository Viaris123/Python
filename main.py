from random import shuffle


class Card:

    suits = ["Hearts", "Spades", "Tambourine", "Crosses"]
    nominal = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, s, n):
        self.n = int(n)
        self.s = int(s)

    def __repr__(self):
        msg = self.nominal[self.n] + " of " + self.suits[self.s]
        return msg

    def __lt__(self, other):
        if self.n < other.n:
            return True
        if self.n == other.n:
            if self.s < other.s:
                return True
            else:
                return False

    def __gt__(self, other):
        if self.n > other.n:
            return True
        if self.n == other.n:
            if self.s > other.s:
                return True
        else:
            return False


class Deck:

    deck_list = []

    def __init__(self):
        if len(self.deck_list) != 0:
            self.deck_list.clear()
        for i in range(4):
            for j in range(12):
                self.deck_list.append(Card(i, j))
        shuffle(self.deck_list)

    def get_card(self):
        return self.deck_list.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.card = None
        self.wins = 0


class Game:

    def __init__(self):
        self.name1 = input("Enter first player name: ")
        self.name2 = input("Enter second player name: ")
        self.deck = Deck()
        self.p1 = Player(self.name1)
        self.p2 = Player(self.name2)

    def table(self, player_1_name, player_1_card, player_2_name, player_2_card):
        tbl = "{} put {}, and {} put {}"
        tbl = tbl.format(player_1_name, player_1_card, player_2_name, player_2_card)
        print(tbl)

    def wins(self, winner, loser):
        w = "{} win! {} takes all cards".format(winner, loser)
        print(w)
    def winner(self):
        if self.p1.wins > self.p2.wins:
            print(f"{self.p1.name} win!")
        else:
            print(f"{self.p2.name} win!")

    def play_the_game(self):
        while len(self.deck.deck_list) >= 0:
            print("Let's go!")
            print("Press 'X' to exit, press 'Enter' to continue.")
            res = input()
            if res == 'x':
                break

            self.p1.card = self.deck.get_card()
            self.p2.card = self.deck.get_card()
            self.table(self.p1.name, self.p1.card, self.p2.name, self.p2.card)

            if self.p1.card < self.p2.card:
                self.p2.wins += 1
                self.wins(self.p2.name, self.p1.name)
            else:
                self.p1.wins += 1
                self.wins(self.p1.name, self.p2.name)
        self.winner()
        print("Game over!")



game = Game()
game.play_the_game()
