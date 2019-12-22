from domain import *
from controller import *
from texttable import Texttable
class ui():
    def __init__(self,game):
        self.g=game
        
    def verifyblinker(self,x,y):
        '''
        this function verifies if the blinker position is valid
        input:-x- vertical position of the starting point of the pattern
            -y- the horizontal position of the starting point of the pattern
        output:none
        '''
        if x+2>=8:
            raise ValueError
        if self.g.grid.data[x][y]==1:
            raise ValueError
        if self.g.grid.data[x+1][y]==1:
            raise ValueError
        if self.g.grid.data[x+2][y]==1:
            raise ValueError
        
    def verifyblock(self,x,y):
        '''
        this function verifies if the block position is valid
        input:-x- vertical position of the starting point of the pattern
            -y- the horizontal position of the starting point of the pattern
        output:none
        '''
        if x+1>=8 or y+1>=8:
            raise ValueError
        if self.g.grid.data[x][y]==1:
            raise ValueError
        if self.g.grid.data[x+1][y]==1:
            raise ValueError
        if self.g.grid.data[x][y+1]==1:
            raise ValueError
        if self.g.grid.data[x+1][y+1]==1:
            raise ValueError
    def verifytub(self,x,y):
        '''
        this function verifies if the tub position is valid
        input:-x- vertical position of the starting point of the pattern
            -y- the horizontal position of the starting point of the pattern
        output:none
        '''
        if x+2>=8 or y+2>=8:
            raise ValueError
        if self.g.grid.data[x+1][y]==1:
            raise ValueError
        if self.g.grid.data[x][y+1]==1:
            raise ValueError
        if self.g.grid.data[x+1][y+2]==1:
            raise ValueError
        if self.g.grid.data[x+2][y+1]==1:
            raise ValueError
        
    def place(self,cpattern,positions):
        pos=positions.split(',')
        if cpattern=='blinker':
            try:
                self.verifyblinker(int(pos[0]),int(pos[1]))
                self.g.placeblinker(int(pos[0]),int(pos[1]))
            except ValueError:
                print("invalid position")
        elif cpattern=='block':
            try:
                self.verifyblock(int(pos[0]),int(pos[1]))
                self.g.placeblock(int(pos[0]),int(pos[1]))
            except ValueError:
                print('invalid position')
        elif cpattern=='tub':
            try:
                self.verifytub(int(pos[0]),int(pos[1]))
                self.g.placetub(int(pos[0]),int(pos[1]))
            except ValueError:
                print('invalid position')
    def citire(self):
        print(self.g)
        ok=1
        while ok==1:
            command=input().split()
            if command[0]=='place':
                self.place(command[1],command[2])
            if command[0]=='tick':
                if len(command)==1:
                    self.g.tick(1)
                else:
                    self.g.tick(int(command[1]))
            if command[0]=='save' and command[1]=='filename':
                self.g.saving()
            if command[0]=='load' and command[1]=='filename':
                self.g.incarca()
            if command[0]=='exit':
                ok=0
            print(self.g)
    