from turtle import Turtle

FONT = ("Courier", 25, "normal")
HIGHSCORE_FILE = "highscore.txt"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        with open(HIGHSCORE_FILE, mode="r") as hs_file:
            self.high_score = int(hs_file.read())
        self.refresh()

    def refresh(self):
        self.clear()
        screen = self.getscreen()
        screen_top = screen.window_height() / 2
        self.setposition(-200, screen_top - 30)
        self.write(f"Score: {self.score}", align="center", font=FONT)
        self.setposition(160, screen_top - 30)
        self.write(f"High Score: {self.high_score}", align="center", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        with open(HIGHSCORE_FILE, mode="w") as hs_file:
            hs_file.write(f"{self.high_score}")

    def add_point(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.refresh()
