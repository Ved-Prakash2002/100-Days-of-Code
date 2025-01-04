import turtle  # Importing the turtle module for graphics.

# Screen setup
screen = turtle.Screen()  # Create the screen object.
screen.title("Breakout Game")  # Set the title of the game window.
screen.bgcolor("black")  # Set the background color of the game window.
screen.setup(width=600, height=600)  # Set the dimensions of the game window.
screen.tracer(0)  # Turn off automatic screen updates for smoother animations.

# Paddle setup
paddle = turtle.Turtle()  # Create the paddle object.
paddle.speed(0)  # Animation speed is set to the fastest.
paddle.shape("square")  # Shape of the paddle.
paddle.color("white")  # Color of the paddle.
paddle.shapesize(stretch_wid=1, stretch_len=5)  # Adjust the size of the paddle.
paddle.penup()  # Lift the pen to avoid drawing lines.
paddle.goto(0, -250)  # Position the paddle at the bottom of the screen.
paddle.dx = 0  # Initialize paddle movement speed.

# Ball setup
ball = turtle.Turtle()  # Create the ball object.
ball.speed(0)  # Animation speed is set to the fastest.
ball.shape("circle")  # Shape of the ball.
ball.color("white")  # Color of the ball.
ball.penup()  # Lift the pen to avoid drawing lines.
ball.goto(0, 0)  # Position the ball at the center of the screen.
ball.dx = 2  # Horizontal movement speed of the ball.
ball.dy = -2  # Vertical movement speed of the ball.

# Brick setup
bricks = []  # List to store brick objects.
brick_colors = {"red": 1, "orange": 2, "yellow": 3, "green": 4, "blue": 5}  # Scoring for each brick color.
color_list = list(brick_colors.keys())  # List of brick colors for cycling.

# Create a grid of bricks.
for i in range(6):  # Rows of bricks.
    for j in range(10):  # Columns of bricks.
        brick = turtle.Turtle()  # Create a brick object.
        brick.speed(0)  # Animation speed is set to the fastest.
        brick.shape("square")  # Shape of the brick.
        brick.color(color_list[i % len(color_list)])  # Cycle through colors.
        brick.shapesize(stretch_wid=1, stretch_len=2)  # Adjust the size of the brick.
        brick.penup()  # Lift the pen to avoid drawing lines.
        brick.goto(-250 + j * 50, 200 - i * 25)  # Position each brick in a grid pattern.
        bricks.append(brick)  # Add the brick to the list.

# Scoreboard setup
score = 0  # Initialize the score.
score_display = turtle.Turtle()  # Create a turtle object for displaying the score.
score_display.speed(0)  # Animation speed is set to the fastest.
score_display.color("white")  # Set the color of the text.
score_display.penup()  # Lift the pen to avoid drawing lines.
score_display.hideturtle()  # Hide the turtle for cleaner display.
score_display.goto(0, 260)  # Position the scoreboard at the top of the screen.
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))  # Display the initial score.

# Functions
def update_score(points):
    """
    Updates the score by adding the specified points and refreshes the scoreboard.
    """
    global score
    score += points  # Increment the score.
    score_display.clear()  # Clear the previous score.
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))  # Display the updated score.

def paddle_right():
    """Moves the paddle to the right."""
    paddle.dx = 10

def paddle_left():
    """Moves the paddle to the left."""
    paddle.dx = -10

def stop_paddle():
    """Stops the paddle movement."""
    paddle.dx = 0

# Keyboard bindings
screen.listen()  # Listen for keyboard input.
screen.onkeypress(paddle_right, "Right")  # Move the paddle right when the "Right" arrow key is pressed.
screen.onkeypress(paddle_left, "Left")  # Move the paddle left when the "Left" arrow key is pressed.
screen.onkeyrelease(stop_paddle, "Right")  # Stop the paddle when the "Right" key is released.
screen.onkeyrelease(stop_paddle, "Left")  # Stop the paddle when the "Left" key is released.

# Main game loop
game_on = True  # Game state flag.
while game_on:
    screen.update()  # Refresh the screen.

    # Move the paddle
    x = paddle.xcor() + paddle.dx  # Calculate the new x-coordinate of the paddle.
    if -250 < x < 250:  # Ensure the paddle stays within the screen bounds.
        paddle.setx(x)  # Update the paddle's position.

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # Update the ball's x-coordinate.
    ball.sety(ball.ycor() + ball.dy)  # Update the ball's y-coordinate.

    # Ball collision with top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverse the vertical direction of the ball.

    # Ball collision with side borders
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1  # Reverse the horizontal direction of the ball.

    # Ball misses paddle
    if ball.ycor() < -290:
        game_on = False  # End the game.
        score_display.goto(0, 0)
        score_display.write("Game Over", align="center", font=("Courier", 36, "normal"))  # Display game over message.

    # Paddle and ball collision
    if (-240 > ball.ycor() > -250) and \
            (paddle.xcor() + 50 > ball.xcor() > paddle.xcor() - 50):
        ball.dy *= -1  # Reverse the vertical direction of the ball.
        ball.dx *= 1.05  # Increment ball speed.
        ball.dy *= 1.05

    # Brick and ball collision
    for brick in bricks:
        if brick.isvisible() and (ball.distance(brick) < 30):  # Check collision with visible bricks.
            brick.hideturtle()  # Hide the brick.
            bricks.remove(brick)  # Remove the brick from the list.
            ball.dy *= -1  # Reverse the vertical direction of the ball.
            update_score(brick_colors[brick.color()[0]])  # Update the score based on brick color.
            break  # Avoid multiple collisions with the same brick.

    # Win condition
    if not bricks:  # If all bricks are destroyed.
        game_on = False  # End the game.
        score_display.goto(0, 0)
        score_display.write("You Win!", align="center", font=("Courier", 36, "normal"))  # Display win message.

# Keep the window open until manually closed.
screen.mainloop()
