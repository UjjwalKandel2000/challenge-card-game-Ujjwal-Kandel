class Symbol:
    """Class defining a symbol based on colors and icons,"""

    def __init__(self,icon):
        """By default, our surface is empty"""
        self.color = ["red", "black"]
        self.icon = icon

    def __str__(self):
        return f" {self.icon}"


class Card(Symbol):
    def __init__(self,icon,value):
        super(Card,self).__init__(icon)
        self.value = value

    def show(self):
        print(f"{super().__str__()}, {self.value}")

    def __str__(self):
        return f"{super().__str__()}, {self.value}"


card = Card("d",1)
print(card)
