from utils.player import Deck
from utils.player import Player
from utils.game import Board

dck = Deck()

ujjwal = Player("Ujjwal", dck)
aubin = Player("Aubin", dck)
kasia = Player("kasia", dck)
alber = Player("Alber", dck)

group = [ujjwal, aubin, kasia, alber]

board = Board(group)
board.start_game()


