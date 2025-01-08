from turtle import Screen  # Import the Screen class for creating the game window
from Snake import Snake  # Import the Snake class to manage the snake object and its behavior
from Food import Food  # Import the Food class to manage the food object
from Scoreboard import Scoreboard  # Import the Scoreboard class to manage the game score
import time  # Import the time module to add delays for smoother gameplay

# Create the game screen
screen = Screen()
snake = Snake()  # Create an instance of the Snake class
food = Food()  # Create an instance of the Food class
scoreboard = Scoreboard()  # Create an instance of the Scoreboard class

# Configure the game screen
screen.setup(width=600, height=600)  # Set the dimensions of the game screen
screen.bgcolor("black")  # Set the background color to black
screen.title("My Snake Game")  # Set the title of the game window
screen.tracer(0)  # Turn off automatic screen updates for smoother animations

# Flag to control the game loop
game_is_on = True

# Initialize the snake
snake.create_snake()  # Create the initial snake

# Set up event listeners for keyboard controls
screen.listen()  # Start listening for keyboard inputs
screen.onkey(snake.up, "Up")  # Bind the "Up" arrow key to the snake's upward movement
screen.onkey(snake.down, "Down")  # Bind the "Down" arrow key to the snake's downward movement
screen.onkey(snake.left, "Left")  # Bind the "Left" arrow key to the snake's leftward movement
screen.onkey(snake.right, "Right")  # Bind the "Right" arrow key to the snake's rightward movement

# Start the game loop
while game_is_on:
    screen.update()  # Update the screen to reflect changes
    time.sleep(0.1)  # Pause briefly to control the speed of the game
    snake.move_snake()  # Move the snake forward

    # Check for collision with food
    if snake.head.distance(food) < 15:  # If the snake's head is close to the food
        food.refresh()  # Move the food to a new random location
        snake.extend()  # Extend the snake by adding a new segment
        scoreboard.increase_score()  # Increase the score

    # Check for collision with walls
    if (snake.head.xcor() > 580 or snake.head.xcor() < -580 or
        snake.head.ycor() > 300 or snake.head.ycor() < -300):  # If the snake hits the wall
        scoreboard.reset_score()  # Reset the score to zero
        snake.reset_snake()  # Reset the snake to its initial state

    # Check for collision with its own body
    for segment in snake.segments[1:]:  # Iterate through all segments except the head
        if snake.head.distance(segment) < 10:  # If the head collides with a body segment
            scoreboard.reset_score()  # Reset the score to zero
            snake.reset_snake()  # Reset the snake to its initial state

# Keep the game window open
screen.mainloop()
