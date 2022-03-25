from turtle import Turtle

FONT = ("Courier", 30, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        screen = self.getscreen()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.screen_top = screen.window_height() / 2 - 40
        self.level = 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.setposition(0, self.screen_top)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
