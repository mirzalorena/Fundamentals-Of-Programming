#TINDER 
from model import *
from control import *

class ui:
    def __init__(self,control,person):
        self.__control=control
        self._person=person
    
    def readFile(self,filename):
        result=[]
        try:
            f=open(filename,"r")
            line=f.readline().strip()
            while len(line)>0:
                line=line.split(" ")
                result.append(person(line[0],int(line[1]),line[2]))
                line=f.readline().strip()
            f.close()
        except IOError as e:
            print("Something went wrong")
            raise e
        return result
    
    def print_people(self):
        #people=[person("ana",18,"dans")]
        for p in self.readFile("data.txt"):
            print(p)
    
    def add_you(self):
        name=str(input("What's your name? "))
        age=str(input("How old are you? "))
        hobby=str(input("Write a hobby!"))
        pers=person(name,age,hobby)
        return pers
    
    def match(self):
        matches=[]
        list_peps=self.readFile("data.txt")
        pers=self.add_you
        f=open("data.txt","r")
        line=f.readline().strip()
        while len(line)>0:
            line=line.split(" ")
            #result.append(person(line[0],int(line[1]),line[2]))
            if line[2]==person.pers.getHobby:
                matches.append(person(line[0],int(line[1]),line[2]))
            line=f.readline().strip()
        f.close() 
        #for p in list_peps:
            
        #return matches
            
    def chooseAdate(self):
        self.print_people()
        choice=int(input("Choose a date!(Parteners name) "))
        return choice 
    
    def gradeDate(self):
        pass
          
    def menu(self):
        print("1.See all people")
        print("2.Add your personal information!")
        print("3.See your matches!") 
        print("4.Choose a date!")  
        print("5.Grade your date!")   
    
    def main(self):
        print("Welcome to Tinder")
        self.menu()
        commands={1:(self.print_people,"See all people"),
                  2:(self.add_you, "Add your personal informations!"),
                  3:(self.match,"See your matches!"),
                  4:(self.chooseAdate,"Choose a date!"),
                  5:(self.gradeDate,"Grade your date!")
                    }
        while True:
            try:
                com=int(input("Please select one command: "))
                if com==0:
                    break
                else:
                    commands[com][0]()
                if com=="exit":
                    break
            except ValueError as ve:
                print("Inavlid command")
        
#if __name__=="main":
ui=ui(control,person)
ui.main()
        
        