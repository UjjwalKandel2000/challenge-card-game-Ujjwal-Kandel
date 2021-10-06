from time import sleep

from utils.card import Card
import random


class Player:
    def __init__(self, name, deck):
        self.deck = deck
        self.name = name
        self.cards = []
        self.turn_count = 0
        self.active_cards = 0
        self.history_cards = []

    def get_history_cards(self):
        return self.history_cards

    def play(self):
        self.turn_count += 1
        self.history_cards.append(self.deck.drawCard())
        print(f" {self.name} {self.turn_count} played : {self.history_cards[-1]} ")

    def showHand(self):
        for kaart in self.history_cards:
            print(kaart.__str__())

    def __str__(self):
        if len(self.history_cards) != 0:
            return f" {self.name} {self.turn_count} played : {self.history_cards[-1]} "
        else:
            return f"{self.name} has not picked a card yet"


class Deck:
    def __init__(self):
        self.cards = []
        self.game_counter = 0

    def fill_deck(self):
        for s in ['♥', '♦', '♣', '♠']:
            for v in range(1, 14):
                self.cards.append(Card(s, str(v)))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            # print(f"r: {r}, i:{i}")
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def show(self):
        for c in self.cards:
            c.show()

    def drawCard(self):
        return self.cards.pop()

    def cards_left(self):
        return len(self.cards)

    def distribute(self, players):
        for player in players:
            self.game_counter += 1
            player.play()
            print(f"counter: {self.game_counter}")
            sleep(0.5)
