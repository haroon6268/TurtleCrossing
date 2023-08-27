import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
obstacle = CarManager()
score = Scoreboard()

score.welcome()
screen.update()
time.sleep(2)
score.clearwrite()
score.instructions()
screen.update()
time.sleep(4)
score.clear()
obstacle.difficulty()

screen.listen()
screen.onkeypress(player.move_forward, "w")
screen.onkeypress(player.move_backward, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    obstacle.create_car()
    obstacle.movement()
    for car in obstacle.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.loser()

    if player.ycor() > 290:
        score.winner()
        game_is_on = False

screen.exitonclick()