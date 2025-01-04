import turtle  # Importing the turtle module for graphics.
import pandas  # Importing pandas for handling CSV data.

# Setting up the screen and loading the background image of the U.S. map.
screen = turtle.Screen()
screen.title("U.S. States Game")  # Setting the title of the game window.
image = "blank_states_img.gif"  # Path to the map image file.
screen.addshape(image)  # Adding the image as a new shape for the turtle.
turtle.shape(image)  # Setting the image as the turtle's shape.

# Loading the CSV file containing state names and their coordinates.
states_file = pandas.read_csv("50_states.csv")
states_list = states_file.state.to_list()  # Converting the "state" column to a list for easier comparison.
correct_states = []  # List to track states guessed correctly by the user.

score = 0  # Variable to keep track of the score.
no_of_guesses = 1  # Counter for the number of guesses.

# Check if the user has guessed all 50 states correctly.
if score == 50:
    game_is_on = False
    print("Congratulations!! You have guessed all the states")

# Main game loop that allows up to 50 guesses.
while no_of_guesses <= 50:
    # Prompting the user to guess a state name.
    answer_state = screen.textinput(title=f"Guess the State ({score}/50)", prompt="What's the state's name?")

    # Converting the user's input to title case to match the state names.
    answer_state_title_case = answer_state.title()
    no_of_guesses += 1  # Incrementing the guess counter.

    # Exit the game if the user types "Exit".
    if answer_state == 'Exit':
        break

    # Check if the guessed state is in the list of U.S. states.
    if answer_state_title_case in states_list:
        correct_states.append(answer_state_title_case)  # Add the correct state to the list.

        # Retrieve the coordinates of the guessed state from the CSV file.
        state_data = states_file[states_file.state == answer_state_title_case]
        x_cor = int(state_data.x.values[0])  # X-coordinate of the state.
        y_cor = int(state_data.y.values[0])  # Y-coordinate of the state.

        # Create a new turtle to write the state name on the map.
        text_turtle = turtle.Turtle()
        text_turtle.penup()  # Lift the pen to avoid drawing lines.
        text_turtle.hideturtle()  # Hide the turtle for cleaner output.
        text_turtle.goto(x_cor, y_cor)  # Move the turtle to the state's coordinates.
        text_turtle.pendown()  # Place the pen down to write the text.

        # Write the state name on the map.
        text_turtle.write(answer_state_title_case, align='center', font=("Arial", 9, "normal"))
        score += 1  # Increment the score for a correct guess.

# Create a list of states that the user did not guess.
states_to_learn = [state for state in states_list if state not in correct_states]

# Alternative way to create the `states_to_learn` list:
# for state in states_list:
#    if state not in correct_states:
#        states_to_learn.append(state)

# Convert the list of unguessed states into a dictionary.
states_to_learn_dict = {"States": states_to_learn}

# Create a DataFrame from the dictionary and save it as a CSV file.
df = pandas.DataFrame(states_to_learn_dict)
df.to_csv("states_to_learn.csv")  # Save the CSV file with states to learn.

# Keep the turtle graphics window open until the user closes it.
turtle.mainloop()
