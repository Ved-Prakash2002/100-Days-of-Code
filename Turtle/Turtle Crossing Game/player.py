from turtle import Turtle  # Import the Turtle class for creating the player object.
from car_manager import CarManager  # Import the CarManager class (though not used directly here).

# Constants for player properties and movement.
STARTING_POSITION = (0, -280)  # Initial position of the player (at the bottom center of the screen).
MOVE_DISTANCE = 10  # Distance the player moves with each key press.
FINISH_LINE_Y = 280  # Y-coordinate of the finish line (top of the screen).

class Player(Turtle):
    """
    Represents the player-controlled turtle in the game.
    Handles player movement and winning conditions.
    """

    def __init__(self):
        """
        Initializes the Player object.
        - Inherits from the Turtle class.
        - Sets the shape, initial position, and orientation of the player.
        """
        super().__init__()  # Call the parent class (Turtle) initializer.
        self.shape("turtle")  # Set the player's shape to "turtle".
        self.penup()  # Lift the pen to avoid drawing lines when moving.
        self.goto(STARTING_POSITION)  # Place the player at the starting position.
        self.setheading(90)  # Set the player's direction to face upward.

    def up(self):
        """
        Moves the player upward by a predefined distance.
        - Ensures the player does not move beyond the finish line.
        """
        if self.ycor() < FINISH_LINE_Y:  # Check if the player is below the finish line.
            self.forward(MOVE_DISTANCE)  # Move the player forward (upward).

    def win(self):
        """
        Resets the player to the starting position after reaching the finish line.
        """
        self.penup()  # Lift the pen to avoid drawing lines during the reset.
        self.goto(STARTING_POSITION)  # Move the player back to the starting position.
