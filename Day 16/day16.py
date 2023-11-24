import turtle
from turtle import *
from prettytable import PrettyTable

timmy = turtle.Turtle()

print(timmy)

my_screen = Screen()

print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()


table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
# table.add_row(["Jayanth","Appalla"])

table.align = "l"

print(table.align)

print(table)