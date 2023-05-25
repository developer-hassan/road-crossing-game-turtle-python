# Use the turtle module for its functionality
from turtle import Turtle

# Defining a constant for consistent display
FONT = ("Courier", 22, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # Create a scoreboard object with specific properties and behaviors
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clears the screen and writes the current score on the screen.
        """
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        """
        Increments the level of user and call the update_scoreboard method to display the updated score.
        """
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """
        Resets the position of turtle to its starting position and display the "Game Over" message to the user.
        """
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
