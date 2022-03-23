from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import ScoreBoard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_BORDER_LEFT = SCREEN_WIDTH / 2 * -1
SCREEN_BORDER_RIGHT = SCREEN_WIDTH / 2
SCREEN_BORDER_NORTH = SCREEN_HEIGHT / 2
SCREEN_BORDER_SOUTH = SCREEN_HEIGHT / 2 * -1
SCREEN_PADDING = 19

INITIAL_SNAKE_BODY_LEN = 3

screen = Screen()
screen.title("Snake? Snake?! Snaaaaaakkkkeeeee!!!")
screen.tracer(0)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")

snake = Snake(INITIAL_SNAKE_BODY_LEN)
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

run_game = True
while run_game:
    if snake.head.distance(food) < 19:
        food.refresh()
        snake.add_segment()
        scoreboard.add_point()

    # Hitting Wall
    if snake.head.xcor() > SCREEN_BORDER_RIGHT - SCREEN_PADDING or snake.head.xcor() < SCREEN_BORDER_LEFT + SCREEN_PADDING or snake.head.ycor() > SCREEN_BORDER_NORTH - SCREEN_PADDING or snake.head.ycor() < SCREEN_BORDER_SOUTH + SCREEN_PADDING:
        scoreboard.game_over()
        run_game = False

    # Hitting self
    for snake_segment in snake.body[1:]:
        if snake.head.distance(snake_segment) < 10:
            scoreboard.game_over()
            run_game = False

    snake.move()
    screen.update()
    time.sleep(.1)


screen.exitonclick()
