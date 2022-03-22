from snake import Snake
from turtle import Turtle, Screen
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

INITIAL_SNAKE_BODY_LEN = 3

screen = Screen()
screen.title("Snake Gaaaammmmeeee!!!")
screen.tracer(0)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")

snake = Snake(INITIAL_SNAKE_BODY_LEN)

run_game = True

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

while run_game:
    snake.move()
    screen.update()

screen.exitonclick()
