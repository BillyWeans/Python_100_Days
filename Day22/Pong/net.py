from turtle import Turtle

class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pensize(10)
        screen = self.getscreen()
        screen_bottom = screen.window_height() / 2 * -1
        screen_top = screen.window_height() / 2
        self.penup()
        self.setposition(0, screen_bottom - 50)
        self.setheading(90)
        print(self.ycor())
        for _ in range(int(screen_top)):
            self.pendown()
            self.forward(25)
            self.penup()
            self.penup()
            self.forward(25)