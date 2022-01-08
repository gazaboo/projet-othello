class Player():
    def __init__(self, representation):
        self.representation = representation
        
    def capture(self, x, y, board):
        cell = board.get_cell(x, y)
        cell.set_owner(self)
        pieces_to_flip = board.get_neighbors_in_all_directions(x, y, self)
        for piece in pieces_to_flip: 
            piece.set_owner(self)
        
    def get_my_pieces(self, board):
        return list(filter(lambda cell: cell.owner is self, board.cells))
    
    def get_score(self, board):
        return len(self.get_my_pieces(board))