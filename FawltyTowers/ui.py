'''
Created on Feb 2, 2019

@author: Lorena
'''
from controller import * 
from model import *

class ui:
    def __init__(self,control,rooms,reserv):
        self.__control=control 
        self._rooms=rooms 
        self._reserv=reserv 
        
    def readFile(self,filename):
        result=[]
        try:
            f=open(filename,"r")
            line=f.readline().strip()
            while len(line)>0:
                line=line.split(" ")
                result.append(room(int(line[0]),line[1]))
                line=f.readline().strip()
            f.close()
        except IOError as e:
            print("Something went wrong")
            raise e 
        return result
    
    def printRooms(self):
        for r in self.readFile("rooms.txt"):
            print(r)
            
    def main(self):
        print("Welcome to Fawlty towers!")
        commands={1:(self.printRooms,"See all rooms")
            }
        while True:
            try: 
                com=int(input("Please select one command: "))
                if com==0:
                    break 
                else:
                    commands[com][0]
                if com=="exit":
                    break
                                    
            except ValueError as ve:
                print("Invalid command")
        
ui=ui(controller,room,reservation)
ui.main()      
        
        
        
        