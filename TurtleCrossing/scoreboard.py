FONT = ("Courier", 24, "normal")
from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(0,0)
    def welcome(self):
        self.write("Welcome to Turtle Crossing",align="center",font=FONT)
    def instructions(self):
        self.write("Click 'W' to move forward.\nTry to get to the other side!", align="center", font=FONT)

    def loser(self):
        self.write("A car hit you! You lost!", align="center", font=FONT)

    def winner(self):
        self.write("You Won!", align="center", font=FONT)

    def clearwrite(self):
        self.clear()



