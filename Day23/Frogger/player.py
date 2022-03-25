from turtle import Turtle

PLAYER_MOVEMENT = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        screen = self.getscreen()
        screen_bottom = screen.window_height() / 2 * -1
        self.alive = True
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.startpos = (0,screen_bottom + 40)
        self.setposition(self.startpos)

    def move_up(self):
        if self.alive:
            new_y = self.ycor() + PLAYER_MOVEMENT
            self.sety(new_y)

    def restart(self):
        self.setposition(self.startpos)

    def dead(self):
        self.alive = False
        self.setheading(180)
        self.setheading(270)
        self.setheading(0)
        self.setheading(90)
