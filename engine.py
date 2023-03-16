from board import Board
from player import Player
from os import system
import string

class Engine():
    def __init__(self, size=8):
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board(self.player1, self.player2, size)
        self.current_player = self.player1
        self.keep_playing = True
    
    def next_turn(self):
        self.display_game()
        legal_moves = self.board.compute_possible_moves(self.current_player)
        if len(legal_moves) > 0:
            col, row = self.get_legal_move_from_player(legal_moves, self.current_player)
            self.current_player.capture(col, row, self.board)
        else:
            self.current_player.has_moved = False 
        self.current_player = self.player1 if self.current_player is self.player2 else self.player2            
        return self.is_over()
        
    def get_scores(self):
        score =  f"Score Joueur X : {self.player1.get_score(self.board)}  |  "
        score += f"Score Joueur O : {self.player2.get_score(self.board)}"
        return score
    
    def get_legal_move_from_player(self, legal_moves, player):
        val = input(f"Tour du joueur {player.representation} (col row) : ")
        col, row = val.split(" ")
        col = string.ascii_uppercase.index(col.upper())
        row = int(row)
        while (col, row) not in legal_moves:
            print("Mouvement impossible ! Essaye encore !")
            val = input(f"Tour du joueur {player.representation} : ")
            col, row =  map(int, val.split(" "))
        return col, row
    
    def display_game(self):
        system('clear')
        print(self.board)
        print(self.get_scores())

    def is_over(self): 
        return not self.player1.has_moved and not self.player2.has_moved 