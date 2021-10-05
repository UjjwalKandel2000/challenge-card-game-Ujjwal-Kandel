from utils.card import Card
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = [Card]
        self.turn_count = 0
        self.active_cards = 0
        self.history_cards = []

    def draw(self, deck):
        self.history_cards.append(deck.drawCard())
        print(f"{self.name} {self.turn_count} played: {self.history_cards[-1]}")
        return self

    def showHand(self):
        for kaart in self.cards:
            kaart.show()
    def __str__(self):
        return f"name of the player is {self.name}"


p1 = Player("ujjwal")
print(p1)


class Deck:
    def __init__(self):
        self.cards = [Card]
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            # print(f"r: {r}, i:{i}")
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def show(self):
        for c in self.cards:
            c.show(self)

    def drawCard(self):
        return self.cards.pop()
