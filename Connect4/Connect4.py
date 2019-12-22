'''
Created on Dec 20, 2018

@author: Lorena
'''
from Board import Board
from game_manager import Player,comp
import random

class Game:
    def __init__(self,board):
        self.turn=0 #assings players turn
        self.players=[]
        #self.comp=comp('0')
        self.board=board 
        
    def play(self):
        print("Welcome to Connect4 !")
        print("You will play against LolaBot!")
        self.players.append(Player('x'))
        #self.players.append(Player('0'))
        self.players.append(comp('0'))
        
        while True:
            print()
            self.board.print_board()
            print()
            while True:
                try:
                    self.board.add_cell(self.players[self.turn].get_choice(self.board),self.players[self.turn].obj)
                    #self.board.print_board()
                    break
                except Exception as e:
                    print("Invalid")
            
            if self.board.check_winner():
                self.board.clear_board()
                print(f"{self.players[self.turn].name} wins. IEI")
                return 
            if self.board.full_board():
                self.board.clear_board()
                print("Draw. Not IEI")
                return 
            self.turn=(self.turn+1)%2
            
    def play_comp(self):
        print("Welcome to Connect4 !")
        print("Player:")
        self.players.append(Player('x'))
        print("Your opponent will be Lola Bot")
        lolaBot=Player()
            
if __name__=="__main__":
    game=Game(Board(6,7))
    game.play()   
            
                    
    