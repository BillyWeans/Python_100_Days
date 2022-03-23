from turtle import Turtle

FONT = ("Courier", 25, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        screen = self.getscreen()
        screen_top = screen.window_height() / 2
        self.setposition(0, screen_top - 30)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def add_point(self):
        self.score += 1
        self.refresh()
