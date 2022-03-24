from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from net import Net
import time

PLAYER1_START_POS = (-350, 0)
PLAYER2_START_POS = (350, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NORTH_BOUNCE_PADDING = 15
SOUTH_BOUNCE_PADDING = 25
RIGHT_BOUNCE_PADDING = 75
LEFT_BOUNCE_PADDING = 75
WALLS_VISIBLE = True

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong, bro. It's Pong!!!")
screen.bgcolor("black")
screen.tracer(0)

NORTH_WALL = SCREEN_HEIGHT / 2
SOUTH_WALL = SCREEN_HEIGHT / 2 * -1
LEFT_WALL = SCREEN_WIDTH / 2 * -1
RIGHT_WALL = SCREEN_WIDTH / 2

scoreboard = Scoreboard()
net = Net()
player1 = Paddle(PLAYER1_START_POS)
player2 = Paddle(PLAYER2_START_POS)

screen.listen()
# Player 1
screen.onkey(key="w", fun=player1.up)
screen.onkey(key="s", fun=player1.down)
# Player 2
screen.onkey(key="Up", fun=player2.up)
screen.onkey(key="Down", fun=player2.down)

ball = Ball()

run_game = True
while run_game:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with north / south wall
    if ball.ycor() > NORTH_WALL - NORTH_BOUNCE_PADDING or ball.ycor() < SOUTH_WALL + SOUTH_BOUNCE_PADDING:
        ball.bounce_vertical()

    # Detect collision with paddle
    #  we only measure distance to center of paddle, so if we are within 50 pixels AND we are within 20 pixels
    #  of left/right wall, we count it as contact with the paddle
    if (ball.distance(player1) < 50 and ball.xcor() < LEFT_WALL + LEFT_BOUNCE_PADDING) or (ball.distance(player2) < 50 and ball.xcor() > RIGHT_WALL - RIGHT_BOUNCE_PADDING):
        ball.bounce_horizontal()

    # Detect ball out of bounds
    if ball.xcor() < LEFT_WALL - 20:
        ball.recenter()
        scoreboard.add_point("player2")

    if ball.xcor() > RIGHT_WALL + 20:
        ball.recenter()
        scoreboard.add_point("player1")



screen.exitonclick()