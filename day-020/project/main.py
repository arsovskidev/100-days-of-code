from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.title("Snake")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

running = True

while running:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
