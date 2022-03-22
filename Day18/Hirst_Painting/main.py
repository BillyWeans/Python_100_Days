from turtle import Turtle, Screen
from random import choice
# import colorgram
#
# image_colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
#
# for image_color in image_colors:
#     r = image_color.rgb.r
#     g = image_color.rgb.g
#     b = image_color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


def random_color():
    return choice(color_list)


def draw_circle():
    # timmy.begin_fill()
    # timmy.fillcolor(random_color())
    timmy.dot(20,random_color())
    # timmy.end_fill()

def draw_row():
    for _ in range(10):
        timmy.forward(50)
        draw_circle()


timmy = Turtle()
screen = Screen()
screen.colormode(255)
screen.setup(560, 550)
timmy.speed("fastest")

color_list = [(186, 20, 46), (243, 232, 63), (252, 232, 238), (222, 241, 247), (193, 76, 36), (217, 68, 108), (20, 124, 171), (15, 141, 89), (195, 175, 20), (109, 182, 208), (15, 166, 212), (206, 155, 92), (26, 40, 73), (179, 44, 65), (36, 43, 110), (79, 174, 97), (235, 231, 4), (215, 68, 49), (216, 130, 154), (126, 184, 120), (236, 162, 181), (9, 61, 39), (148, 208, 220), (9, 90, 51), (6, 85, 108), (155, 31, 29), (234, 171, 164), (162, 211, 185)]

screen_width = screen.window_width()
screen_height = screen.window_height()
LEFT_SCREEN = screen_width / 2 * -1
BOTTOM_SCREEN = screen_height / 2 * -1
timmy.penup()
# Start Timmy at the very bottom left
timmy.setposition(LEFT_SCREEN, BOTTOM_SCREEN)
# Move him into a visible space
timmy.left(90)
timmy.forward(50)
timmy.right(90)

# Start drawing the painting
for _ in range(10):
    draw_row()
    timmy.left(90)
    timmy.forward(50)
    timmy.setx(LEFT_SCREEN)
    timmy.right(90)


screen.exitonclick()
