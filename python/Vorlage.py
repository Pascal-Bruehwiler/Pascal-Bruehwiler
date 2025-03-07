#DIESEN TEIL IGNORIEREN
#Imports
from gturtle import *
import math
from random import *

#HIER GEHT DAS PROGRAMM LOS
#Schildkröte erstellen
t = makeTurtle()

#zu Punkt 0,0 springen
setPos(0,0)
t.fd(100) #forward

t.rt(90) #rotate right
t.bk(50) #backward
t.lt(45) #rotate left

setPos(0,100)
t.goto(50,150)