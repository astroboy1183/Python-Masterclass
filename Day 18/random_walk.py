import random
import turtle
from turtle import *


# from turtle_code import *

turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim = Turtle()

tim.width(14)
tim.speed(0)  # 0 for fastest , 1 for slowest

colors = ["green", "red", "blue", "orange", "yellow", "black"]

directions = [i for i in range(360)]

for i in range(300):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
