from texttable import Texttable
class grid():
    def __init__(self):
        self.data=[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8]
        
    def getxsquares(self):
        lst=[]
        for i in range(8):
            for j in range(8):
                if self.data[i][j]==1:
                    lst.append([i,j])
        return lst
    