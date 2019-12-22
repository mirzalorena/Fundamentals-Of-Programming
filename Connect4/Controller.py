'''
Created on Dec 29, 2018

@author: Lorena
'''
import copy 
from Board import Board
import random
from random import choice

class controller:
    def __init__(self,board,obj):
        self.__board=board
        self.__obj=obj
        
    def comp_move(self):
        options=self.__board.get_empty_cell()
        if len(options)==0:
            print("Board is full!")
            return
        for option in options:
            b=self.__board.copy()
            b.add_cell(option,'0')
            if b.check_winner()==True:
                #self.__board.add_cell(option,'0')
                return option
        for option in options:
            b.self.board.copy()
            b.add_cell(option,'0')
            if b.check_winner()==True:
                #self.__board.add_cell(option,'0')
                return option
        
        #self.__board.add_cell(choice(options),'0')
        return choice(options)
        
               
    """   
    def get_potential_moves(self,board):
        if board.full_board:
            return [0]*board.width
        
        potential_moves=[0]*board.width
        for first_move in range(board.width):
            aux=copy.deepcopy(board)
            if not aux.valid_move(first_move):
                continue
            aux.add_cell(first_move,'0')
            if aux.check_winner():
                potential_moves[first_move]=1
                break
            else:
                if aux.full_board(aux):
                    potential_moves[first_move]=0
                else:
                    for counter in range(aux.width):
                        aux2=copy.deepcopy(aux)
                        if not aux2.valid_move(counter):
                            continue
                        aux2.add_cell(counter,'0')
                        if aux2.check_winner():
                            potential_moves[first_move]=-1
                            break
                        else:
                            result=self.get_potential_moves(aux2)
                            potential_moves[first_move] += (sum(result)/board.width)/board.width
                    
            return potential_moves
        
    def comp_moves(self):
        potential=self.get_potential_moves(self.__board)
        best=-1
        for i in range(self.__board.width):
            if potential[i]>best and self.__board.valid_move(i):
                best=potential[i]
        bestMoves=[]
        for i in range(len(potential)):
            if potential[i]==best and self.__board.valid_move(i):
                bestMoves.append(i)
        i=random.choice(bestMoves)+1
        self.add_cell(i,'0')
        return i
    """
               
                
                
                
                
                
                
    