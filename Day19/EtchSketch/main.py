from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def timmy_forward():
    timmy.forward(10)


def timmy_backward():
    timmy.backward(10)


def timmy_counterclock():
    timmy.left(10)


def timmy_clockwise():
    timmy.right(10)


def reset_timmy():
    screen.reset()
    timmy.setposition(0, 0)


screen.listen()
screen.onkey(key='w', fun=timmy_forward)
screen.onkey(key='s', fun=timmy_backward)
screen.onkey(key='a', fun=timmy_counterclock)
screen.onkey(key='d', fun=timmy_clockwise)
screen.onkey(key='c', fun=reset_timmy)

screen.exitonclick()
