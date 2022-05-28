import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score = Scoreboard()
car_manager = CarManager()
player = Player()
screen.listen()
screen.onkey(player.turtle_up,"Up")
#screen.onkey(player.turtle_down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with cars

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False
    
    # Detect Sucessfull crossing
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        score.increase_level()

screen.exitonclick()
