from board import Board
from player import Player
from os import system

class Engine():
    def __init__(self):
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board(self.player1, self.player2)
        self.current_player = self.player1
        self.keep_playing = True
    
    def play(self):
        system('clear')
        self.board.display()
        print(self.get_scores())
        self.board.compute_possible_moves(self.current_player)
        x, y = self.get_correct_move_from_player(self.current_player)
        self.current_player.capture(x, y, self.board)
        self.current_player = self.player1 if self.current_player is self.player2 else self.player2
        
    def get_scores(self):
        score =  f"Score Joueur X : {self.player1.get_score(self.board)}  |  "
        score += f"Score Joueur O : {self.player2.get_score(self.board)}"
        return score
    
    def get_correct_move_from_player(self, player):
        val = input(f"Tour du joueur {player.representation} : ")
        x, y = map(int, val.split(" "))
        while (x, y) not in player.possible_moves:
            print("Movement impossible ! Essaye encore !")
            val = input(f"Tour du joueur {player.representation} : ")
            x, y =  map(int, val.split(" "))
        return x, y
            