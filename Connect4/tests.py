'''
Created on Dec 20, 2018

@author: Lorena
'''
import unittest
from Board import Board
from Connect4 import Game
from game_manager import Player



class Tests(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def board_tests(self):
        new_board=Board(3,3)
        self.assertEqual(new_board.width,3)
        self.assertEqual(new_board.height, 3)
        self.assertEqual(new_board.full_board(), False)
        self.assertEqual(new_board.check_winner(),False)
        
        #check vertical win cond
        new_board=Board(6,7)
        new_board.add_cell(3, 'x')
        new_board.add_cell(3, 'x')
        new_board.add_cell(3, 'x')
        new_board.add_cell(3, 'x')
        self.assertEqual(new_board.check_winner(), True)
        
        #check orizontal win cond
        new_board=Board(6,7)
        new_board.add_cell(1, 'x')
        new_board.add_cell(2, 'x')
        new_board.add_cell(3, 'x')
        new_board.add_cell(4, 'x')
        new_board.add_cell(5, 'x')
        new_board.add_cell(6, 'x')
        self.assertEqual(new_board.check_winner(), True)
        
        #Check minor diagonal win 
        new_board = Board(7,6)
        new_board.add_cell(1,'x')
        new_board.add_cell(1,'x')
        new_board.add_cell(1,'x')
        new_board.add_cell(1,'x')
        new_board.add_cell(2,'x')
        new_board.add_cell(2,'x')
        new_board.add_cell(2,'o')
        new_board.add_cell(3,'x')
        new_board.add_cell(3,'o')
        new_board.add_cell(4,'o')
        self.assertEqual(new_board.check_winner(), True)
        
        #Check major diagonal win 
        new_board = Board(7,6)
        new_board.add_cell(1,'x')
        new_board.add_cell(2,'o')
        new_board.add_cell(2,'x')
        new_board.add_cell(3,'o')
        new_board.add_cell(3,'o')
        new_board.add_cell(3,'x')
        new_board.add_cell(4,'x')
        new_board.add_cell(4,'o')
        new_board.add_cell(4,'o')
        new_board.add_cell(4,'x')
        self.assertEqual(new_board.check_winner(), True)
        
        #check full board 
        new_board=Board(6,7)
        for i in range(7):
            for j in range(6):
                new_board.add_cell(i+1,'X')
        self.assertEqual(new_board.full_board(), True)
 
 
 
 
if __name__ == '__main__':
    Tests.main()    
            