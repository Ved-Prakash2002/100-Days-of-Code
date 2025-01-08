import time  # Importing time for adding delays in the game loop.
import turtle  # Importing turtle for creating the game screen and graphical elements.
from Paddle import Paddle  # Importing the Paddle class for paddle movement and control.
from Ball import Ball  # Importing the Ball class for ball movement and collision handling.
from Scoreboard import Scoreboard  # Importing the Scoreboard class for tracking and displaying the score.

# Set up the game screen.
screen = turtle.Screen()
screen.setup(width=800, height=600)  # Set the screen size to 800x600 pixels.
screen.bgcolor("black")  # Set the background color to black.
screen.title("Pong")  # Set the title of the window.

# Create paddle objects.
left_paddle = Paddle(350, 0)  # Create the left paddle at x=350 (right side of the screen).
right_paddle = Paddle(-350, 0)  # Create the right paddle at x=-350 (left side of the screen).

# Configure key listeners for paddle movement.
screen.listen()  # Listen for key presses.
screen.onkeypress(left_paddle.up, "Up")  # Move the left paddle up when the "Up" arrow key is pressed.
screen.onkeypress(left_paddle.down, "Down")  # Move the left paddle down when the "Down" arrow key is pressed.
screen.onkeypress(right_paddle.up, "w")  # Move the right paddle up when the "W" key is pressed.
screen.onkeypress(right_paddle.down, "s")  # Move the right paddle down when the "S" key is pressed.

# Create the ball object.
ball = Ball()

# Create the scoreboard object.
score = Scoreboard()

# Main game loop.
game_is_on = True  # Flag to control the game loop.
while game_is_on:
    time.sleep(ball.speed_increment)  # Adjust the game loop speed based on the ball's speed increment.
    screen.update()  # Update the screen to reflect changes.
    ball.move()  # Move the ball.

    # Detect collision with the top and bottom walls.
    if ball.ycor() > 290 or ball.ycor() < -290:  # If the ball's y-coordinate exceeds the screen boundaries:
        ball.bounce_y()  # Reverse the ball's vertical direction.

    # Detect collision with paddles.
    if ball.distance(left_paddle) < 50 and ball.xcor() > 320 or ball.distance(right_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()  # Reverse the ball's horizontal direction.

    # Detect when the ball goes out of bounds on the right side.
    if ball.xcor() > 380:  # If the ball crosses the right boundary:
        ball.reset_position()  # Reset the ball to the center.
        score.l_point()  # Increment the score for the left player.

    # Detect when the ball goes out of bounds on the left side.
    if ball.xcor() < -380:  # If the ball crosses the left boundary:
        ball.reset_position()  # Reset the ball to the center.
        score.r_point()  # Increment the score for the right player.

# Keep the window open until manually closed.
screen.mainloop()
