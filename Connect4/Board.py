'''
Created on Dec 20, 2018

@author: Lorena
'''
class Board:
    def __init__(self,width,height):
        self.board=[[" "]*width for i in range(height)]
        self.width=width
        self.height=height 
        
    def clear_board(self):
        """
        clears the board
        """
        self.board=[[" "]*self.width for i in range(0,self.height)]
        
    def full_board(self):
        """
        checks if the board is full (space left on columns)
        output: true - if ful
                false - if not full
        """
        for i in range(0,len(self.board)):
            for j in range(0,len(self.board[i])):
                if self.board[i][j]==' ':
                    return False 
        return True
    
    def print_board(self):
        ''' displays current board
        '''
        print("-" *(2*self.width), end = ' ')
        print()
        
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j],end=' ')
            print()
            
        print("-" *(2*self.width), end = ' ')
        print()
        
        for row in range(len(self.board[i])):
            print(row+1, end= ' ')
            
    def get_empty_cell(self):
        res=[]
        for i in range(self.board):
            for j in range(self.board[i]):
                if self.board[i][j]==0:
                    res.append(i)
        return res
     
    def valid_move(self,col):
        if col<0:
            return False
        if col>=self.width:
            return False
        
        return True 
           
    def add_cell(self,col,obj):
        """
        adds an object to the specified column on board
        """
        for r in range(self.height-1,-1,-1):
            if col<=0:
                raise ValueError("Invalid column")
            if col>self.width:
                raise ValueError("Invalid column")
            if self.board[r][col-1]==" ":
                self.board[r][col-1]=obj 
                break
        else:
            raise ValueError("Column full")   
        
    def check_winner(self):
        #checks horizontally 
        for i in range(0,self.height):
            for j in range(self.width-3):
                if self.board[i][j] != " ":
                    h=[self.board[i][j],self.board[i][j+1],self.board[i][j+2],self.board[i][j+3]]
                    for c in range(0,len(h)):
                        if self.board[i][j]==self.board[i][j+1]==self.board[i][j+2]==self.board[i][j+3]:
                            return True
        
        #checks vertically 
        for i in range(0,self.height-3):
            for j in range(self.width-3):
                if self.board[i][j] != " ":
                    v=[self.board[i][j],self.board[i+1][j],self.board[i+2][j],self.board[i+3][j]]
                    for c in range(0,len(v)):
                        if self.board[i][j]==self.board[i+1][j]==self.board[i+2][j]==self.board[i+3][j]:
                            return True
        
        #checks major diagonal
        for i in range(0,self.height-3):
            for j in range(self.width-3):
                if self.board[i][j] != " ":
                    md=[self.board[i][j],self.board[i+1][j+1],self.board[i+2][j+2],self.board[i+3][j+3]]
                    for c in range(len(md)):
                        if self.board[i][j]==self.board[i+1][j+1]==self.board[i+2][j+2]==self.board[i+3][j+3]:
                            return True
                        
        #checks major diagonal
        for i in range(3,self.height):
            for j in range(self.width-3):
                if self.board[i][j] != " ":
                    md=[self.board[i][j],self.board[i-1][j-1],self.board[i-2][j-2],self.board[i-3][j-3]]
                    for c in range(len(md)):
                        if self.board[i][j]==self.board[i-1][j-1]==self.board[i-2][j-2]==self.board[i-3][j-3]:
                            return True
                        
        return False
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            