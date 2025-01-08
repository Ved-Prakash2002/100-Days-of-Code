from turtle import Turtle  # Import the Turtle class for creating car objects.
import random  # Import random for generating random positions and colors.

# Constants for car properties and movement.
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]  # List of car colors.
STARTING_MOVE_DISTANCE = 5  # Initial speed of the cars.
MOVE_INCREMENT = 10  # Speed increment when the level increases.

class CarManager(Turtle):
    """
    Manages the creation, movement, and speed of cars in the game.
    """

    def __init__(self):
        """
        Initializes the CarManager object.
        - Inherits from the Turtle class for consistency but primarily manages a list of cars.
        - Sets up an empty list to store cars and initializes the starting speed.
        """
        super().__init__()  # Call the parent class (Turtle) initializer.
        self.cars = []  # List to store all car objects.
        self.car_speed = STARTING_MOVE_DISTANCE  # Initialize car speed to the starting value.

    def create_car(self):
        """
        Creates a new car at random intervals.
        - A car is only created when a randomly generated number equals 1 (1 in 6 chance).
        - Cars are positioned at the right edge of the screen with a random vertical position.
        """
        random_chance = random.randint(1, 6)  # Generate a random number between 1 and 6.
        if random_chance == 1:  # Create a car only if the number is 1.
            new_car = Turtle("square")  # Create a new car object as a square.
            new_car.shape("square")  # Set the car shape.
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Stretch the shape to form a rectangle.
            new_car.penup()  # Lift the pen to avoid drawing lines when moving.
            new_car.color(random.choice(COLORS))  # Assign a random color to the car.
            new_car.goto(300, random.randint(-250, 250))  # Position the car at the right edge with a random vertical position.
            self.cars.append(new_car)  # Add the new car to the list of cars.

    def move_car(self):
        """
        Moves all cars in the `cars` list from right to left across the screen.
        - The movement distance is determined by the current `car_speed`.
        """
        for car in self.cars:  # Loop through all car objects.
            car.backward(self.car_speed)  # Move each car backward by the current speed.

    def increase_car_speed(self):
        """
        Increases the speed of the cars by a predefined increment.
        - This method is called when the player advances to the next level.
        """
        self.car_speed += MOVE_INCREMENT  # Increase the car speed by the increment value.
