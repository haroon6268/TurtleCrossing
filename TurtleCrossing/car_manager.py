COLORS = ["green", "black"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
rand_y = 5
from turtle import Turtle,Screen
import random


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.screen = Screen()

    def difficulty(self):
        global rand_y
        level = self.screen.textinput("Difficulty", "Easy, Medium, or Hard").lower()
        if level == "medium":
            rand_y = 3
        if level == "hard":
            rand_y = 2






    def create_car(self):
        random_chance = random.randint(1,rand_y)
        if random_chance == 2:
            new_car = Turtle()
            new_car.penup()
            new_car.goto(300, random.randint(-200, 300))
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            self.all_cars.append(new_car)

    def movement(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)



