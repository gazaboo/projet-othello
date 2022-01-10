from cell import Cell

class Board():
    
    separator = "\n   +---+---+---+---+---+---+---+---+\n"
    
    def __init__(self, player1, player2):
        self.cells = [Cell(x, y) for y in range(8) for x in range(8)]
        player1.capture(3, 3, self)
        player1.capture(4, 4, self)
        player2.capture(3, 4, self)
        player2.capture(4, 3, self)
    
    def display(self):
        s = "\n     0   1   2   3   4   5   6   7"
        for i, cell in enumerate(self.cells):
            if i % 8 == 0 : 
                s += Board.separator + f"{int(i/8)}  |"
            s += cell.representation
        s += Board.separator
        print(s)

    def get_cell(self, x, y):
        if x in range(0, 8) and y in range(0,8): 
            return self.cells[x + 8*y]
        else: return None
    
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
        for dir in directions.values():
            neighbor_dir = self.get_surrounded_pieces_in_one_direction(x, y, player, dir)
            if neighbor_dir is not None:
                neighbors.extend(neighbor_dir)
        return neighbors
    
    def compute_possible_moves(self, player):
        empty_cells = list(filter(lambda cell: cell.owner is None, self.cells))
        player.possible_moves = {}
        for cell in empty_cells:
            surrounded_pieces = self.get_surrounded_pieces_in_all_directions(cell.x, cell.y, player) 
            if len(surrounded_pieces) > 0:
                player.possible_moves[(cell.x, cell.y)] = surrounded_pieces

