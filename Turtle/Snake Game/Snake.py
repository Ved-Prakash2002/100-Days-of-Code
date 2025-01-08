from turtle import Turtle  # Import the Turtle class to create and manage the snake


class Snake:
    """
    A class to represent the snake in the snake game.
    Handles snake creation, movement, and interactions.
    """

    def __init__(self):
        """
        Initialize the snake with its starting position and properties.
        """
        self.x, self.y = 0, 0  # Starting position for the snake's head
        self.segments = []  # List to store all segments of the snake
        self.create_snake()  # Create the initial snake with three segments
        self.head = self.segments[0]  # Set the first segment as the head of the snake

    def create_snake(self):
        """
        Create the initial snake with three segments positioned in a row.
        """
        for position in range(3):  # Loop to create three segments
            self.add_segment(position)  # Add a segment for each position

    def add_segment(self, position):
        """
        Add a new segment to the snake at a specific position.

        Parameters:
        position (int): Index representing the position of the segment being created.
        """
        new_segment = Turtle()  # Create a new Turtle object for the segment
        new_segment.shape("square")  # Set the shape of the segment to a square
        new_segment.color("white")  # Set the color of the segment to white
        new_segment.penup()  # Disable drawing when the segment moves
        new_segment.goto(self.x, self.y)  # Position the segment at the current x, y coordinates
        self.segments.append(new_segment)  # Add the segment to the snake's segment list
        self.x -= 20  # Shift the x-coordinate to position the next segment

    def extend(self):
        """
        Extend the snake by adding a new segment at the position of the last segment.
        """
        self.add_segment(self.segments[-1].position())  # Add a segment at the position of the last segment

    def reset_snake(self):
        """
        Reset the snake to its initial state by moving all segments off-screen and recreating the initial snake.
        """
        for segment in self.segments:  # Loop through all segments of the snake
            segment.goto(1000, 1000)  # Move each segment off-screen
        self.segments.clear()  # Clear the list of segments
        self.create_snake()  # Recreate the snake with three initial segments
        self.head = self.segments[0]  # Set the head to the first segment of the new snake

    def move_snake(self):
        """
        Move the snake forward by shifting each segment to the position of the segment in front of it.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Loop through segments in reverse order
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the segment in front
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the segment in front
            self.segments[seg_num].goto(new_x, new_y)  # Move the current segment to that position
        self.segments[0].forward(20)  # Move the head forward by 20 units

    def up(self):
        """
        Change the snake's direction to up if it is not currently moving down.
        """
        if self.head.heading() != 270:  # Prevent reversing direction
            self.head.setheading(90)  # Set the direction to up

    def down(self):
        """
        Change the snake's direction to down if it is not currently moving up.
        """
        if self.head.heading() != 90:  # Prevent reversing direction
            self.head.setheading(270)  # Set the direction to down

    def left(self):
        """
        Change the snake's direction to left if it is not currently moving right.
        """
        if self.head.heading() != 0:  # Prevent reversing direction
            self.head.setheading(180)  # Set the direction to left

    def right(self):
        """
        Change the snake's direction to right if it is not currently moving left.
        """
        if self.head.heading() != 180:  # Prevent reversing direction
            self.head.setheading(0)  # Set the direction to right
