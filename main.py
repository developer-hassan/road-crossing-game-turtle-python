# Importing necessary libraries for the program execution
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creating and setting up a screen for game
screen = Screen()
screen.title("Street Crossing Race")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Creating a player, CarManager, and Scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Move the turtle forward on pressing the "Up" Arrow key
screen.onkeypress(player.move_forward, "Up")

# Start the game
game_is_on = True
# While the game is running
while game_is_on:
    # Update the screen with appropriate time delay
    screen.update()
    time.sleep(0.1)

    # Move the cars on screen and create cars
    car_manager.move()
    car_manager.create_car()

    # Check the collision of turtle with the car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect whether the player has reached the top head
    if player.ycor() > 280:
        # Move the turtle back to the starting position
        player.reset_position()
        # Increment the level of the game
        scoreboard.level_up()
        # Increment the speed with which the cars are moving
        car_manager.increment_speed()

# Exit the screen on click
screen.exitonclick()
