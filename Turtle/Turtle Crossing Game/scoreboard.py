from turtle import Turtle  # Import the Turtle class for creating the scoreboard.

# Font style for the scoreboard text.
FONT = ("Courier", 24, "normal")  # Set the font to "Courier", size 24, and "normal" style.

class Scoreboard(Turtle):
    """
    Manages the display of the game's scoreboard, including the current level and game-over message.
    """

    def __init__(self):
        """
        Initializes the Scoreboard object.
        - Inherits from the Turtle class.
        - Sets the initial level to 1 and positions the scoreboard at the top-left corner of the screen.
        """
        super().__init__()  # Call the parent class (Turtle) initializer.
        self.level = 1  # Initialize the game level to 1.
        self.hideturtle()  # Hide the turtle cursor for a clean display.
        self.penup()  # Lift the pen to avoid drawing lines when moving.
        self.goto(-280, 250)  # Position the scoreboard at the top-left corner of the screen.
        self.update_scoreboard()  # Display the initial scoreboard.

    def update_scoreboard(self):
        """
        Updates the scoreboard to display the current level.
        - Clears the previous text before writing the new level.
        """
        self.clear()  # Clear the previous text from the scoreboard.
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Display the current level.

    def increase_level(self):
        """
        Increases the player's level by 1 and updates the scoreboard.
        """
        self.level += 1  # Increment the level by 1.
        self.update_scoreboard()  # Refresh the scoreboard with the new level.

    def game_over(self):
        """
        Displays the "GAME OVER" message at the center of the screen.
        """
        self.goto(0, 0)  # Move to the center of the screen.
        self.write("GAME OVER", align="center", font=FONT)  # Display the game-over message.
