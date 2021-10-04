class Symbol:
    """Class defining a symbol based on colors and icons,"""

    def __init__(self, color):
        """By default, our surface is empty"""
        self.color = color
        self.icon = ["♥", "♦", "♣", "♠"]


s = Symbol("red")


class Card(Symbol):
    def __init__(self, color: str):
        Symbol.__init__(self, color)
        self.value = ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']
