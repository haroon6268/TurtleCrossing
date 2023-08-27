import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        self.backward(MOVE_DISTANCE)
