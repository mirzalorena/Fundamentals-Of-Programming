from domain import *
from texttable import Texttable
class game():
    def __init__(self,grid):
        self.grid=grid
        
    def placeblinker(self,x,y):
        '''
        this function places a blinker pattern
        input:-x- the vertical starting position of the pattern
            -y- the horizontal starting position of the pattern
        output:none
        '''
        self.grid.data[x][y]=1
        self.grid.data[x+1][y]=1
        self.grid.data[x+2][y]=1
        
    def placeblock(self,x,y):
        '''
        this function places a block pattern
        input:-x- the vertical starting position of the pattern
            -y- the horizontal starting position of the pattern
        output:none
        '''
        self.grid.data[x][y]=1
        self.grid.data[x+1][y]=1
        self.grid.data[x][y+1]=1
        self.grid.data[x+1][y+1]=1
    def placetub(self,x,y):
        '''
        this function places a tub pattern
        input:-x- the vertical starting position of the pattern
            -y- the horizontal starting position of the pattern
        output:none
        '''
        self.grid.data[x][y+1]=1
        self.grid.data[x+1][y]=1
        self.grid.data[x+1][y+2]=1
        self.grid.data[x+2][y+1]=1
    
    def checks(self,i,j):
        '''
        this function numbers how many live cells are in the cell (i,j)
        input:-i- the vertical position
            -j- the horizontal position
        output:
                -s- the number of living cells
        '''
        s=0
        if i-1>=0 and j-1>=0:
            if self.grid.data[i-1][j-1]==1:
                s+=1
        if i-1>=0:
            if self.grid.data[i-1][j]==1:
                s+=1
        if i-1>=0 and j+1<8:
            if self.grid.data[i-1][j+1]==1:
                s+=1
        if j-1>=0:
            if self.grid.data[i][j-1]==1:
                s+=1
        if j+1<8:
            if self.grid.data[i][j+1]==1:
                s+=1
        if i+1<8 and j-1>=0:
            if self.grid.data[i+1][j-1]==1:
                s+=1
        if i+1<8:   
            if self.grid.data[i+1][j]==1:
                s+=1
        if i+1<8 and j+1<8:
            if self.grid.data[i+1][j+1]==1:
                s+=1
        return s
    
    
    def tick(self,n):
        '''
        this function updates the grid corresponding to the rules applied to the game
        input:-n- represents how many times the grid updates before printing
        output:none
        '''
        while n>0:
            n-=1
            livingcells=[]
            deadcells=[]
            for i in range(8):
                for j in range(8):
                    s=self.checks(i,j)
                    if self.grid.data[i][j]==0:
                        if s==3:
                            livingcells.append([i,j])
                    if self.grid.data[i][j]==1:
                        if s==2 or s==3:
                            livingcells.append([i,j])
                        elif s<2:
                            deadcells.append([i,j])
                        elif s>3:
                            deadcells.append([i,j])
            for k in livingcells:
                self.grid.data[k[0]][k[1]]=1
            for k in deadcells:
                self.grid.data[k[0]][k[1]]=0
            
    def saving(self):
        f=open('joculet.txt','w')
        
        for i in range(8):
            lst=[]
            for j in range(8):
                lst.append(self.grid.data[i][j])
            f.write(str(lst))
        f.close()
    def incarca(self):
        f=open('joculet.txt','r')
        lst=[]
        for line in f.readlines():
            lst.append(line)
        print (lst)
        for i in range(8):
            for j in range(8):
                self.grid.data[i][j]=lst[i][j]
        
        
                        
        
    def __str__(self):
        t=Texttable()
        dict={0:'',1:'X'}
        for i in range(8):
            lst=[]
            for j in range(8):
                lst.append(dict[self.grid.data[i][j]])
            t.add_row(lst)
        return t.draw()
        
    