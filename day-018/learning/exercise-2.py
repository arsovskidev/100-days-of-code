import turtle as T

turtle = T.Turtle()
turtle.shape("circle")
turtle.color("purple1")
turtle.speed("slowest")

for _ in range(20):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)

screen = T.Screen()
screen.exitonclick()
