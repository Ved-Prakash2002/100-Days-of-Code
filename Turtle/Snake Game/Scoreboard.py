from turtle import Turtle  # Import the Turtle class to create the scoreboard


class Scoreboard(Turtle):
    """
    A class to display and manage the score and high score in the snake game.
    Inherits from the Turtle class to use its drawing and positioning capabilities.
    """

    def __init__(self):
        """
        Initialize the scoreboard with default properties, current score, and high score.
        """
        super().__init__()  # Call the superclass (Turtle) initializer
        self.score = 0  # Initialize the current score to 0

        # Read the high score from a file named "data.txt"
        with open("data.txt", mode='r') as file:
            self.high_score = int(file.read())  # Convert the stored value to an integer

        self.color("white")  # Set the text color to white for visibility
        self.penup()  # Disable drawing when the turtle moves
        self.goto(0, 270)  # Position the scoreboard at the top center of the screen
        self.update_scoreboard()  # Display the initial score and high score
        self.hideturtle()  # Hide the turtle cursor

    def update_scoreboard(self):
        """
        Update the scoreboard display with the current score and high score.
        """
        self.clear()  # Clear any existing text on the screen
        # Write the current score and high score on the screen
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   move=False, align="center", font=("Courier", 24, "normal"))

    def reset_score(self):
        """
        Reset the score to zero and update the high score if the current score exceeds it.
        """
        # Check if the current score is greater than the recorded high score
        if self.score > int(self.high_score):
            self.high_score = self.score  # Update the high score
            # Write the new high score to the file
            with open("data.txt", mode='w') as file:
                file.write(str(self.score))

        self.score = 0  # Reset the current score to 0
        self.update_scoreboard()  # Update the scoreboard display

    # display a "GAME OVER" message
    def game_over(self):
         """
         Display a "GAME OVER" message on the screen.
         """
         self.goto(0, 0)  # Position the text at the center of the screen
         self.write("GAME OVER", move=False, align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        """
        Increment the current score by 1 and update the scoreboard display.
        """
        self.score += 1  # Increase the current score by 1
        self.clear()  # Clear the existing text
        self.update_scoreboard()  # Update the scoreboard display
