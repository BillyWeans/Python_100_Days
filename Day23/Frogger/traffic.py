from turtle import Turtle
import random

COLORS = ["red", "orange", "blue", "gray", "violet", "black", "pink", "purple", "yellow"]
CAR_MOVEMENT = 10

class Traffic(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        screen = self.getscreen()
        self.street_top = screen.window_height() / 2 - 80
        self.street_left = screen.window_height() / 2 * -1 - 40
        self.street_right = screen.window_width() / 2 + 40
        self.street_bottom = screen.window_width() / 2 * -1 + 80

    def add_car(self):
        start_x = self.street_right
        start_y = random.randint(self.street_bottom, self.street_top)
        car = Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_len=2)
        car.penup()
        car.setposition(start_x, start_y)
        self.cars.append(car)

    def move_traffic(self):
        for car in self.cars:
            new_x = car.xcor() - CAR_MOVEMENT # Cars move to the left
            car.setx(new_x)
            if car.xcor() < self.street_left:
                self.cars.remove(car)