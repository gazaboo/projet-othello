class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.representation = "   |"
        self.owner = None
    
    def set_owner(self, player):
        self.owner = player
        self.representation = f" {self.owner.representation} |"

