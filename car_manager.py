from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 1
LEVEL_SPEED_INCREASE_RATE = 1.2
Y_BOUNDS = 250
RIGHT_SIDE = 300
EAST = 180
PLAYER_COLLISION_DIST = 17


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed_increment = 0

    def create_car(self):
        color = random.choice(COLORS)
        new_car = Turtle(shape='square')
        new_car.color(color)
        new_car.penup()
        new_car.shapesize(stretch_len=3, stretch_wid=0.7)
        new_car.setheading(EAST)
        y_pos = random.randint(-Y_BOUNDS, Y_BOUNDS)
        new_car.goto(x=RIGHT_SIDE, y=y_pos)
        self.cars.append(new_car)

    def move_all_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT + self.speed_increment)

            # If moving this car leaves the left boundary, remove from list
            if car.xcor() < -RIGHT_SIDE:
                self.cars.remove(car)
                car.hideturtle()

    def clear_all_cars(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()

    def level_up_car_speed(self):
        self.speed_increment += LEVEL_SPEED_INCREASE_RATE

    def reset_car_speed(self):
        self.speed_increment = 0

    def check_car_collision(self, player) -> bool:
        for car in self.cars:
            if car.distance(player) < PLAYER_COLLISION_DIST:
                return True
        return False
