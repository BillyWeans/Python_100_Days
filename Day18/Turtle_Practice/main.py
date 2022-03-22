import turtle
from turtle import Turtle, Screen
from random import randint


def draw_square():
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)


def draw_polygon(sides):
    turn_radius = 360 / sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(turn_radius)
        timmy.forward(100)


def change_color_random():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    timmy.pencolor((r, g, b))


timmy = Turtle()
screen = Screen()
screen.colormode(255)

timmy.shape("turtle")
timmy.color("purple")
timmy.speed("fastest")
timmy.pensize(1)

TURN_ANGLE = 5
turns = int(360 / TURN_ANGLE)

for _ in range(turns + 1):
    change_color_random()
    timmy.circle(100)
    timmy.penup()
    #timmy.right(90)
    timmy.left(TURN_ANGLE)
    #timmy.forward(10)
    timmy.pendown()

screen.exitonclick()
