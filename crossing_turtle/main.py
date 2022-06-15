import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "w")

cars = CarManager()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # Detect player hitting a car
    for car in cars.all_cars:
        if player.distance(car) < 15:
            game_is_on = False
            score.end_game()

    # Detect if player pass the level
    if player.ycor() > 260:
        score.increase_level()
        player.goto_start()
        cars.increase_speed()

screen.exitonclick()
