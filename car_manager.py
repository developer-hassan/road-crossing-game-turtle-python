# Importing the random module for randomization and turtle class for its behavior
import random
from turtle import Turtle

# Defining some constants for a consistent design
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    """
    Responsible for creating cars and moving them on screen.
    """

    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.probability = 6
        self.cars = []

    def create_car(self):
        """
        Create a car as a turtle object with the probability of 1/6.
        """
        # Make a random choice for a probability of 1/6.
        random_chance = random.randint(1, self.probability)
        if random_chance == 1:
            # Create a new car (turtle object) and append it in the current cars
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_y = random.randint(-230, 230)
            new_car.setposition(300, new_y)
            self.cars.append(new_car)

    def move(self):
        """
        Move each car with the specified distance. Removes the car once its out of screen to maintain the space.
        """
        for car in self.cars:
            if car.xcor() < -280:
                car.hideturtle()
                car.clear()
                self.cars.remove(car)
            car.forward(self.move_distance)

    def increment_speed(self):
        """
        Increases the speed of car to make them move faster.
        """
        self.move_distance += MOVE_INCREMENT
        if self.probability > 2:
            self.probability -= 1
