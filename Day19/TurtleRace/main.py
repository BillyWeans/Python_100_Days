from turtle import Turtle, Screen
from random import randint
# screen witdth = 500, height = 400

COLORS = ['red', 'orange', 'black', 'green', 'blue', 'purple']
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
RACE_LINE = (SCREEN_WIDTH / 2 * -1) + 20
FINISH_LINE = (SCREEN_WIDTH / 2) - 30

# Setup the race
turtles = {}
turtle_y_pos = -100
for color in COLORS:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle_y_pos += 30
    turtle.setposition(RACE_LINE, turtle_y_pos)
    turtles[color] = turtle

# Get a bet
user_bet = screen.textinput(title="Pick your bet", prompt="Which color turtle do you think is going to win? ").lower()

# Start the race
is_race_over = False
while not is_race_over:
    for color, turtle in turtles.items():
        turtle_movement = randint(0, 10)
        turtle.forward(turtle_movement)
        if turtle.xcor() >= FINISH_LINE:
            is_race_over = True
            winning_color = color

# Announce the winner
if user_bet == winning_color:
    print("You win!!!")
else:
    print("Sorry, you lose :(")

print(f"The {winning_color} turtle won the race!!")

screen.exitonclick()
