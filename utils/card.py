
class Symbol:
    """Class defining a symbol based on colors and icons,"""
  
    def __init__(self,icon):
        """By default, our color and icon is empty"""   
        self.color = ""
        self.icon = icon
    

    def __str__(self):
        return f" {self.icon}"
    


class Card(Symbol):
    def __init__(self,icon,value):
        super(Card,self).__init__(icon)
        self.value = value
        self.set_color()

    def show(self):
        print(f" {self.value} {super().__str__()}")
        

    def __str__(self):
        return f"{self.value} {super().__str__()}"

    def get_color(self):
        return self.color

    def set_color(self):
        if self.icon=="♥":
            self.color = "red"
        elif self.icon=="♦":
            self.color = "red"
        else: self.color = "black"
        
    def get_color(self):
        return self.color

    def get_icon(self):
        return self.icon
    def get_value(self):
        return self.value
    

