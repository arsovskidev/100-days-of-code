import turtle as T

turtle = T.Turtle()
turtle.shape("circle")
turtle.color("purple1")

for _ in range(4):
    turtle.forward(200)
    turtle.left(90)

screen = T.Screen()
screen.exitonclick()
