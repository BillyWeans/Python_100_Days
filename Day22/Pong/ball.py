from turtle import Turtle

BASE_BALL_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setposition(0, 0)
        self.ball_speed = BASE_BALL_SPEED
        self.x_dir = 10
        self.y_dir = 10

    def move(self):
        new_x = self.xcor() + self.x_dir
        new_y = self.ycor() + self.y_dir
        self.setposition(new_x, new_y)

    def bounce_vertical(self):
        self.y_dir *= -1
        self.ball_speed *= 0.9

    def bounce_horizontal(self):
        self.x_dir *= -1
        self.ball_speed *= 0.9

    def recenter(self):
        self.ball_speed = BASE_BALL_SPEED
        self.setposition(0, 0)
        self.bounce_horizontal()