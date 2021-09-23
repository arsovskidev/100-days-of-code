import turtle as T
import random

turtle = T.Turtle()

colors = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]


def draw_shapes(num_sides):
    angel = 360 / num_sides
    for _ in range(num_sides):
        angle = 360 / num_sides
        turtle.forward(100)
        turtle.right(angle)


for shape_side_n in range(3, 11):
    turtle.color(random.choice(colors))
    draw_shapes(shape_side_n)

screen = T.Screen()
screen.exitonclick()
