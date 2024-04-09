import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SPAWN_RATE = 30

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy Turtle")
screen.tracer(0)

# Initialize Player character
player = Player()

# Initialize Car Manager
car_manager = CarManager()

# Initialize Scoreboard
scoreboard = Scoreboard()

# Initialize event listeners
screen.listen()
screen.onkeypress(fun=player.move, key="w")

cooldown = SPAWN_RATE

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    if cooldown <= 0:
        car_manager.create_car()
        cooldown = SPAWN_RATE
    else:
        cooldown -= 1

    car_manager.move_all_cars()

    if player.is_at_finish_line():
        player.reset_pos()
        scoreboard.increase_level()
        car_manager.clear_all_cars()
        car_manager.level_up_car_speed()

    if car_manager.check_car_collision(player):
        player.set_dead()
        scoreboard.end_game_text()
        game_is_on = False

    screen.update()

screen.exitonclick()