import random
from turtle import *

#Draw multiple shapes with the functions in Turtle Class.

tim = Turtle()

colors = ["green","red","blue","orange","yellow","black"]

for j in range(6):
    tim.color(random.choice(colors))
    for i in range(j+3):
        tim.right(360/(j+3))
        tim.forward(100)


