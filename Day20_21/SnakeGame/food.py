from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.turtlesize(stretch_wid=.5, stretch_len=.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        screen = self.getscreen()
        screen_height = screen.window_height()
        screen_width = screen.window_width()
        x_border_left = (screen_width / 2 * -1) + 20
        x_border_right = (screen_width / 2) - 20
        y_border_north = (screen_height / 2) - 20
        y_border_south = (screen_height / 2 * -1) + 20
        rand_x = randint(x_border_left, x_border_right)
        rand_y = randint(y_border_south, y_border_north)
        self.setposition(rand_x, rand_y)
