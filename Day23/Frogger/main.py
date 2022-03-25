from turtle import Screen
from traffic import Traffic
from player import Player
from scoreboard import Scoreboard
import time

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
FINISH_LINE = SCREEN_HEIGHT / 2 - 40

screen = Screen()
screen.tracer(0)
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.bgcolor("white")

scoreboard = Scoreboard()
traffic = Traffic()
player = Player()

screen.listen()
screen.onkey(key="Up", fun=player.move_up)

game_speed = 0.1
new_car_timer = 0
run_game = True
while run_game:
    new_car_timer += 1
    if new_car_timer % 5 == 0: # A new car every 5 game ticks
        traffic.add_car()

    screen.update()

    # Check for splat!
    for car in traffic.cars:
        if car.distance(player) < 10:
            scoreboard.game_over()
            screen.tracer(1)
            player.dead()
            run_game = False

    if run_game:
        time.sleep(game_speed)
        traffic.move_traffic()

    # Check for win!
    if player.ycor() >= FINISH_LINE:
        game_speed *= .7
        scoreboard.level_up()
        player.restart()


screen.exitonclick()
