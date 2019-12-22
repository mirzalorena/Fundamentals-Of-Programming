from ui.UI import *
from domain.domain import *
from controller.controller import *
from texttable import Texttable


    

def teste():
    matrix=grid()
    joc=game(matrix)
    joc.placeblock(2, 2)
    assert(joc.checks(2, 2)==3)
    assert(joc.checks(0,0)==0)
    joc.tick(3)
    assert(joc.checks(2,2)==3)
    
teste()

def start():
    matrice=grid()
    joc=game(matrice)
    uim=ui(joc)
    uim.citire()

start()
