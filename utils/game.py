

class Board:
    def __init__(self, players):
        self.players = players
        self.deck = players[0].deck
        self.turn_count = self.deck.game_counter
        self.active_cards = []
        self.history_cards = []

    def start_game(self):
        self.deck.fill_deck()
        self.deck.shuffle()
        while self.deck.cards_left() != 0:
            self.deck.distribute(self.players)
            self.turn_count += 1
            print(f"turn_count: {self.turn_count} cards left: {self.deck.cards_left()}")
