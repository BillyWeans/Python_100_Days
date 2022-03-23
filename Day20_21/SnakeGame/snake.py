from turtle import Turtle
import time

MOVE_DISTANCE = 20

UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:

    def __init__(self, snake_len):
        self.snake_len = snake_len
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for _ in range(self.snake_len):
            self.add_segment()

    def add_segment(self):
        snake_segment = Turtle("square")
        snake_segment.penup()
        snake_segment.color("white")
        if len(self.body) == 0:
            snake_segment_start_pos = 0
        else:
            last_segment = self.body[-1].xcor()
            snake_segment_start_pos = last_segment - 20
        snake_segment.setx(snake_segment_start_pos)
        self.body.append(snake_segment)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].setposition(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
