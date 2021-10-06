from utils.player import Deck
from utils.player import Player
from utils.game import Board

deck1 = Deck()

p1 = Player("ek", deck1)
p2 = Player("dui", deck1)
p3 = Player("tin", deck1)
p4 = Player("chhar", deck1)

group = [p1, p2, p3, p4]

board = Board(group)
board.start_game()
