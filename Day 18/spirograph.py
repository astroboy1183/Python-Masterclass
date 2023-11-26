import random
import turtle
from turtle import *

tim = Turtle()

tim.speed(0)
turtle.hideturtle()

turtle.colormode(255)


def choose_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

degree_of_turn = 6 ## should be divisible by 360.

for i in range(int(360/degree_of_turn)):
    tim.color(choose_color())
    tim.circle(100)
    tim.left(degree_of_turn)

screen = Screen()
screen.exitonclick()


