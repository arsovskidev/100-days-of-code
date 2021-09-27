import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()
scoreboard = ScoreBoard()

screen.update()
screen.listen()

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect ball collision with walls.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect ball collistion with paddle.
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Left player get's point.
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.add_l_point()
        l_paddle.reset()
        r_paddle.reset()

    # Right player get's point.
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.add_r_point()
        l_paddle.reset()
        r_paddle.reset()


screen.exitonclick()
