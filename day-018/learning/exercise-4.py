import turtle as T
import random

T.colormode(255)
turtle = T.Turtle()
turtle.pensize(10)
turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


directions = [0, 90, 180, 270]

for _ in range(200):
    turtle.color(random_color())
    turtle.setheading(random.choice(directions))
    turtle.forward(20)
