'''
Created on Feb 2, 2019

@author: Lorena
'''
class room:
    def __init__(self,nr,type):
        self._nr=nr 
        self._type=type
        
    def get_nr(self):
        return self._nr 
    
    def get_type(self):
        return self._type
    
class reservation:
    pass