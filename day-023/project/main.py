import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.update()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

running = True
while running:
    time.sleep(0.1)
    screen.update()

    car_manager.create()
    car_manager.move()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            running = False

    if player.ycor() > 270:
        player.reset()
        car_manager.levelup()
        scoreboard.levelup()

scoreboard.game_over()

screen.exitonclick()
