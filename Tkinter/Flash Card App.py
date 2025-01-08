from tkinter import *  # Import all Tkinter classes for GUI creation.
import pandas  # Import pandas for data manipulation and file handling.
import random  # Import random for selecting a random flashcard.

# Constants
BACKGROUND_COLOR = "#B1DDC6"  # Background color for the app.
to_learn = {}  # Dictionary to store words the user needs to learn.
current_card = {}  # Dictionary to store the current flashcard details.

# Load the data
try:
    # Try to load the "words_to_learn.csv" file if it exists.
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    # If the file does not exist, load the original "french_words.csv" file.
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")  # Convert the data to a list of dictionaries.
else:
    to_learn = data.to_dict(orient="records")  # Convert the data to a list of dictionaries.

# Functions
def next_card():
    """
    Displays the next flashcard with a random French word.
    Resets the timer for flipping the card to show the English translation.
    """
    global current_card, flip_timer  # Use global variables to update the current card and timer.
    window.after_cancel(flip_timer)  # Cancel the previous flip timer.
    current_card = random.choice(to_learn)  # Select a random word from the "to_learn" list.
    # Update the canvas to show the French word on the front side of the card.
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    # Start a timer to flip the card after 3 seconds.
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    """
    Flips the flashcard to show the English translation of the current word.
    Updates the canvas to display the back side of the card.
    """
    # Update the canvas to show the English word on the back side of the card.
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    """
    Marks the current word as known by removing it from the "to_learn" list.
    Saves the updated list to "words_to_learn.csv" and moves to the next card.
    """
    to_learn.remove(current_card)  # Remove the current card from the "to_learn" list.
    # Save the updated "to_learn" list to a CSV file.
    data_to_learn = pandas.DataFrame(to_learn)
    data_to_learn.to_csv("words_to_learn.csv", index=False)
    next_card()  # Show the next card.

# GUI Setup
window = Tk()  # Create the main application window.
window.title("Flashy")  # Set the window title.
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Configure padding and background color.

flip_timer = window.after(3000, func=flip_card)  # Set a timer to flip the card after 3 seconds.

# Canvas for Flashcards
canvas = Canvas(width=800, height=526)  # Create a canvas for displaying flashcards.
card_front_image = PhotoImage(file="card_front.png")  # Load the front card image.
card_back_image = PhotoImage(file="card_back.png")  # Load the back card image.
card_background = canvas.create_image(400, 263, image=card_front_image)  # Display the front image on the canvas.
# Add text elements to the canvas for the card title and word.
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)  # Remove the border around the canvas.
canvas.grid(row=0, column=0, columnspan=2)  # Place the canvas in the grid layout.

# Buttons
# Button for marking a word as unknown (cross button).
cross_image = PhotoImage(file="wrong.png")  # Load the cross button image.
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)  # Place the button in the grid layout.

# Button for marking a word as known (check button).
check_image = PhotoImage(file="right.png")  # Load the check button image.
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)  # Place the button in the grid layout.

# Start with the first card.
next_card()

# Start the Tkinter event loop.
window.mainloop()
