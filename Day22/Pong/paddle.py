from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(start_pos)

    def up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)
