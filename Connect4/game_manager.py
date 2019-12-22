'''
Created on Dec 20, 2018

@author: Lorena
'''
import random 
from Controller import controller


class Player:
    def __init__(self,obj):
        self.obj=obj #x or 0
        self.name=self.get_name()
    
    def get_name(self):
        print("What is your name?")
        name=input("> ")
        return name
    
    def get_choice(self,board):
        print(f"{self.name} which column would you like to place your piece in?")
        choice=int(input("> "))
        return choice 
    
class comp:
    def __init__(self,obj):
        self.obj=obj 
        self.name=self.get_name()
        self.control=controller
    
    def get_name(self):
        name="LolaBot"
        return name
        
    def get_choice(self,board):
        choice=random.randint(1,6)
        #choice=self.control.comp_moves()
        return choice
    