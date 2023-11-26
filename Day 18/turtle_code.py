from turtle import *

tim = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)


for i in range(5):
    tim.forward(100)
    if i<=3:
        tim.right(90)

for i in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = Screen()
screen.exitonclick()

