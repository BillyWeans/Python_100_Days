from turtle import Turtle

FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        screen = self.getscreen()
        screen_height = screen.window_height() / 2 - 100
        screen_right = screen.window_width() / 2
        screen_left = screen.window_width() / 2 * -1
        self.setposition(screen_left + 150, screen_height)
        self.write(f"{self.player1_score}", align="center", font=FONT)
        self.setposition(screen_right - 150, screen_height)
        self.write(f"{self.player2_score}", align="center", font=FONT)

    def add_point(self, player):
        if player == "player1":
            self.player1_score += 1
        elif player == "player2":
            self.player2_score += 1
        self.write_score()

