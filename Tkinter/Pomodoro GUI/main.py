from tkinter import *  # Import all classes and functions from tkinter for GUI development
import math  # Import math module for mathematical operations

# Constants for theming and timer settings
PINK = "#e2979c"  # Color for short break
RED = "#e7305b"  # Color for long break
GREEN = "#9bdeac"  # Color for work timer
YELLOW = "#f7f5dd"  # Background color
WORK_TIME = 25  # Work time in minutes
SHORT_BREAK = 5  # Short break time in minutes
LONG_BREAK = 20  # Long break time in minutes
timer = ""  # Variable to store the timer ID for `after` method
number = 0  # Number of completed sessions
tick_mark = ""  # String to store tick marks for completed work sessions

# Function to start the Pomodoro timer
def start_timer():
    """
    Starts the Pomodoro timer. Alternates between work and break periods.
    Updates the timer label and countdown duration based on the session type.
    """
    global number
    number += 1  # Increment session counter
    if number % 8 == 0:  # Every 8th session, it's a long break
        time = LONG_BREAK
        title_label.config(text="Break", fg=RED)  # Update label text and color for long break
    elif number % 2 == 0:  # Every even session (except 8th), it's a short break
        time = SHORT_BREAK
        title_label.config(text="Break", fg=PINK)  # Update label text and color for short break
    else:  # Odd sessions are work sessions
        time = WORK_TIME
        title_label.config(text="Work", fg=GREEN)  # Update label text and color for work session
    count_down(time * 60)  # Start the countdown in seconds

# Function to reset the timer
def reset_timer():
    """
    Resets the timer and all associated settings.
    Cancels the current timer, resets the label, canvas, and tick marks.
    """
    global number
    window.after_cancel(timer)  # Cancel the active timer
    canvas.itemconfig(timer_text, text="00:00")  # Reset timer text on the canvas
    title_label.config(text="Timer")  # Reset label text
    tick_mark_label.config(text="")  # Clear tick marks
    number = 0  # Reset session counter

# Function to handle countdown logic
def count_down(count):
    """
    Updates the countdown timer on the canvas. Handles the transition between sessions.
    """
    global number
    global tick_mark
    count_min = math.floor(count / 60)  # Calculate minutes from the countdown seconds
    count_sec = count % 60  # Calculate remaining seconds
    if count_sec < 10:  # Add leading zero for single-digit seconds
        count_sec = f"0{count_sec}"

    # Update the timer text on the canvas
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # If the timer hasn't finished, call count_down again after 1 second
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # When the timer finishes, start the next session
        start_timer()
        if number % 2 == 0:  # After every work session, update the tick marks
            tick_mark += "✔"  # Add a tick mark for completed work sessions
            tick_mark_label.config(text=tick_mark)  # Update the tick marks on the label

# Create the main application window
window = Tk()
window.title("Pomodoro")  # Set the window title
window.config(padx=100, pady=50, bg=YELLOW)  # Add padding and set the background color

# Create and configure the title label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Courier", 35))
title_label.grid(column=1, row=0)  # Position the label at the top center

# Create a canvas to display the timer and an image
canvas = Canvas(width=400, height=424, bg=YELLOW, highlightthickness=0)  # No border highlight
tomato_img = PhotoImage(file="tomato.png")  # Load the tomato image
canvas.create_image(200, 212, image=tomato_img)  # Place the image at the center of the canvas
timer_text = canvas.create_text(200, 230, text="00:00", fill="white", font=("Courier", 35, "bold"))  # Timer text
canvas.grid(column=1, row=1)  # Place the canvas in the grid

# Create a label to display tick marks for completed sessions
tick_mark_label = Label(fg=GREEN, bg=YELLOW, font=("Courier", 35))
tick_mark_label.grid(column=1, row=3)  # Place it below the canvas

# Create the start button and bind it to the start_timer function
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)  # Position it to the left of the canvas

# Create the reset button and bind it to the reset_timer function
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)  # Position it to the right of the canvas

# Start the main event loop for the application
window.mainloop()
