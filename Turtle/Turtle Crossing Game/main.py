import time  # Importing time for adding delays in the game loop.
from turtle import Screen  # Importing the Screen class for setting up the game window.
from player import Player  # Importing the Player class for player-related functionalities.
from car_manager import CarManager  # Importing the CarManager class to handle car movement and creation.
from scoreboard import Scoreboard  # Importing the Scoreboard class to display game progress.

# Set up the game screen.
screen = Screen()
screen.setup(width=600, height=600)  # Set the screen size to 600x600 pixels.
screen.tracer(0)  # Turn off automatic screen updates to enable smooth animations.

# Create a player object.
player = Player()

# Set up key listeners for player controls.
screen.listen()  # Listen for key presses.
screen.onkeypress(player.up, "Up")  # Move the player up when the "Up" arrow key is pressed.

# Create a CarManager object to handle car creation and movement.
cars = CarManager()

# Create a Scoreboard object to track and display the game score.
scoreboard = Scoreboard()

# Main game loop.
game_is_on = True  # Flag to control the game loop.
while game_is_on:
    time.sleep(0.1)  # Pause for a short duration to control the game speed.
    screen.update()  # Update the screen to reflect the latest changes.

    # Create and move cars.
    cars.create_car()  # Generate new cars at random intervals.
    cars.move_car()  # Move all existing cars.

    # Check for collisions between the player and cars.
    for car in cars.cars:
        if car.distance(player) < 20:  # If the player is too close to a car:
            game_is_on = False  # End the game.
            scoreboard.game_over()  # Display the "Game Over" message.

    # Check if the player has reached the top of the screen.
    if player.ycor() == 280:
        player.win()  # Reset the player to the starting position.
        cars.increase_car_speed()  # Increase the speed of the cars.
        scoreboard.increase_level()  # Increment and display the current level.

# Keep the window open until the user closes it.
screen.mainloop()
