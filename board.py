import string 
from cell import Cell

class Board():
    
    def __init__(self, player1, player2, size=8):
        self.cells = [Cell(x, y) for y in range(size) for x in range(size)]
        self.size = size
        middle = int(size/2)
        player1.capture(middle - 1, middle - 1, self)
        player1.capture(middle, middle, self)
        player2.capture(middle - 1, middle, self)
        player2.capture(middle, middle - 1, self)
    
    def __str__(self):
        separator = "\n   " + "+---" * self.size + "+\n"
        letters = string.ascii_uppercase[:self.size]
        s = "\n     " + "   ".join(letters)
        for i, cell in enumerate(self.cells):
            if i % self.size == 0 : 
                s += separator + f"{int(i/self.size)}  |"
            s += cell.representation
        s += separator
        return s

    def get_cell(self, x, y):
        in_range = x in range(self.size) and y in range(self.size)
        return self.cells[x + self.size*y] if in_range else None
    
    def get_surrounded_pieces_in_one_direction(self, x, y, player, direction):        
        neighbors = []
        current = self.get_cell(x + direction['x'], y + direction['y'])
        while current is not None and current.owner is not None:
            if current.owner is player:
                return neighbors  
            else:
                neighbors.append(current)
                current = self.get_cell(current.x + direction['x'], current.y + direction['y'])
        return None
         
    def get_surrounded_pieces_in_all_directions(self, x, y, player):
        directions = {
            "RIGHT" : {"x":1 , "y":0 },
            "LEFT"  : {"x":-1, "y":0 },
            "UP"    : {"x":0 , "y":-1},
            "DOWN"  : {"x":0 , "y":1 }
        }
        neighbors = []
        for direction in directions.values():
            neighbor_dir = self.get_surrounded_pieces_in_one_direction(x, y, player, direction)
            if neighbor_dir is not None:
                neighbors.extend(neighbor_dir)
        return neighbors
    
    def compute_possible_moves(self, player):
        empty_cells = filter(lambda cell: cell.owner is None, self.cells)
        possible_moves = {}
        for cell in empty_cells:
            surrounded_pieces = self.get_surrounded_pieces_in_all_directions(cell.x, cell.y, player) 
            if len(surrounded_pieces) > 0:
                possible_moves[(cell.x, cell.y)] = surrounded_pieces
        return possible_moves
