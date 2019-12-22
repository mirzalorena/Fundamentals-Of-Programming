'''
Created on Jan 7, 2019

@author: Lorena
'''
class person:
    def __init__(self,name,age,hobby):
        self._age=age
        self._name=name
        self._hobby=hobby
        
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age
    
    def getHobby(self):
        return self._hobby
    
    def setName(self,name):
        self._name=name
    
    def setAge(self,age):
        self._age=age
        
    def setHobby(self,hobby):
        self._hobby=hobby
        
    def __str__(self):
        return self._name + " " + str(self._age)+ " " + self._hobby + ";"
        
class date:
    def __init__(self,id,n1,n2):
        self._id=id
        self._n1=n1
        self._n2=n2
        
    def getID(self):
        return self._id 
    
    def getN1(self):
        return self._n1 
    
    def getN2(self):
        return self._n2
    
    def setID(self,id):
        self._id=id 
    
    def setN1(self,n1):
        self._n1=n1 
        
    def setN2(self,n2):
        self._n2=n2
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    