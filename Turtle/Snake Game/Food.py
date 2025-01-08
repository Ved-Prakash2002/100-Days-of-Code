from turtle import Turtle  # Import the Turtle class to create the food object
import random  # Import the random module to generate random positions for the food

class Food(Turtle):
    """
    A class to represent the food in the snake game.
    Inherits from the Turtle class to use its properties and methods.
    """
    def __init__(self):
        """
        Initialize the food object with specific properties.
        """
        super().__init__()  # Call the superclass (Turtle) initializer
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Disable drawing when the food moves
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the speed to the fastest for instant movement
        self.refresh()  # Place the food at a random location initially

    def refresh(self):
        """
        Move the food to a new random position on the screen.
        """
        # Generate random x and y coordinates within the game area and move the food there
        self.goto(random.randint(-200, 200), random.randint(-200, 200))
