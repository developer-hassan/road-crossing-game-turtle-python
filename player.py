# Using the turtle module for creating a player
from turtle import Turtle

# Defining some constants for consistent design
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    Responsible for generating a Turtle as a player to move on the road.
    """

    def __init__(self):
        super().__init__()
        # Create a turtle with specific properties and behaviors
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move_forward(self):
        """
        Moves the turtle forwards by the distance provided as an argument.
        """
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        """
        Move the turtle back to the (0, 0) coordinate.
        """
        self.goto(STARTING_POSITION)
