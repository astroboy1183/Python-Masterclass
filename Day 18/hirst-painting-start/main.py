###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random
import turtle
from turtle import *

import colorgram

#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
# print(len(rgb_colors))




######Hirst Painting Project##############



def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

list_of_colors = []
tim = Turtle()
tim.speed(0.2)
tim.penup()
tim.setpos(-600, 0)
tim.pendown()

turtle.colormode(255)

num_of_dots = 12
num_of_rows=8

def circles():
    for i in range(num_of_dots):
        # tim.color(generate_color())
        tim.begin_fill()
        tim.fillcolor(generate_color())
        tim.circle(6)
        tim.end_fill()
        tim.penup()
        tim.forward(70)
        tim.pendown()


for i in range(num_of_rows):
    circles()
    tim.penup()
    tim.left(90)
    tim.forward(20)
    tim.left(90)
    tim.forward(num_of_dots*70) # go back to the start.
    tim.right(90)
    tim.forward(20)
    tim.right(90)
    tim.pendown()


screen = Screen()
screen.exitonclick()
