from hashlib import new
import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = random.randint(1, 8)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2, 1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(350, random_y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def levelup(self):
        self.car_speed += MOVE_INCREMENT
