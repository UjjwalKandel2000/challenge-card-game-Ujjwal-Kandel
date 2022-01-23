import streamlit as st
from utils.player import Deck
from utils.player import Player
from utils.game import Board

deck1 = Deck()

player_name1 = st.text_input(f"name of player 1")
player_name2 = st.text_input(f"name of player 2")
player_name3 = st.text_input(f"name of player 3")
player_name4 = st.text_input(f"name of player 4")

if player_name4:
    p1 = Player(player_name1, deck1)
    p2 = Player(player_name2, deck1)
    p3 = Player(player_name3, deck1)
    p4 = Player(player_name4, deck1)

    group = [p1, p2, p3, p4]

    board = Board(group)
    board.start_game()
