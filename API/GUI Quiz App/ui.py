from tkinter import *  # Import all functions and classes from the tkinter module for creating a GUI
from quiz_brain import QuizBrain  # Import the QuizBrain class for quiz logic

# Constants for theming and layout
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
PADDING_X = 20
PADDING_Y = 20
HEIGHT = 250
WIDTH = 300

class QuizInterface:
    """
    GUI for the quiz application, built using tkinter.
    Handles user interactions and displays quiz content.
    """
    def __init__(self, quiz_brain: QuizBrain):
        # Initialize with a QuizBrain instance to handle quiz logic
        self.quiz = quiz_brain

        # Create the main window
        self.window = Tk()
        self.window.title("Quizzler")  # Set the title of the window
        self.window.config(padx=PADDING_X, pady=PADDING_Y, bg=THEME_COLOR)  # Set padding and background color

        # Create and configure the score label
        self.score_label = Label(self.window, text="Score: 0", bg=THEME_COLOR, fg="white", font=FONT)
        self.score_label.grid(row=0, column=1, sticky="e")  # Place it at the top right corner

        # Create a frame to hold the main content (question canvas)
        self.frame = Frame(self.window, bg=THEME_COLOR, height=HEIGHT, width=WIDTH)
        self.frame.grid(row=1, column=0, columnspan=2, pady=PADDING_Y)

        # Create a canvas for displaying the question text
        self.canvas = Canvas(self.frame, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=PADDING_Y)  # Center it within the frame
        self.question_text = self.canvas.create_text(
            WIDTH / 2,  # X-coordinate for text center
            HEIGHT / 2,  # Y-coordinate for text center
            width=WIDTH - 2 * PADDING_X,  # Wrap text to fit within the canvas
            text="Question Text",  # Placeholder text for the question
            fill=THEME_COLOR,  # Text color
            font=FONT  # Font styling
        )

        # Load the images for True and False buttons
        true_button_image = PhotoImage(file="true.png")  # Image for the "True" button
        false_button_image = PhotoImage(file="false.png")  # Image for the "False" button

        # Create the "True" button and bind it to the true_pressed method
        self.true_button = Button(self.window, image=true_button_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0, pady=PADDING_Y)  # Place it below the canvas on the left

        # Create the "False" button and bind it to the false_pressed method
        self.false_button = Button(self.window, image=false_button_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, pady=PADDING_Y)  # Place it below the canvas on the right

        # Keep a reference to the images to prevent them from being garbage collected
        self.true_button.image = true_button_image
        self.false_button.image = false_button_image

        # Load the first question
        self.get_next()

        # Start the tkinter main loop to display the GUI
        self.window.mainloop()

    def get_next(self):
        """
        Retrieve the next question from the QuizBrain instance and update the canvas.
        Disable buttons if the quiz is over.
        """
        self.canvas.config(bg="white")  # Reset the canvas background color
        if self.quiz.still_has_questions():  # Check if there are questions left in the quiz
            self.score_label.config(text=f"Score: {self.quiz.score}")  # Update the score display
            q_text = self.quiz.next_question()  # Get the next question text
            self.canvas.itemconfig(self.question_text, text=q_text)  # Display the question on the canvas
        else:
            # If no more questions, display an end message and disable buttons
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """
        Handle the "True" button press. Check if the answer is correct and provide feedback.
        """
        is_right = self.quiz.check_answer("True")  # Check the answer using QuizBrain
        self.give_feedback(is_right)  # Call feedback method based on correctness

    def false_pressed(self):
        """
        Handle the "False" button press. Check if the answer is correct and provide feedback.
        """
        is_right = self.quiz.check_answer("False")  # Check the answer using QuizBrain
        self.give_feedback(is_right)  # Call feedback method based on correctness

    def give_feedback(self, is_right):
        """
        Provide feedback to the user by changing the canvas background color.
        Green for correct answers, red for incorrect.
        """
        if is_right is True:
            self.canvas.config(bg="green")  # Set canvas to green for correct answers
        else:
            self.canvas.config(bg="red")  # Set canvas to red for incorrect answers
        self.window.after(1000, self.get_next)  # Wait for 1 second, then load the next question

# Create an instance of the QuizInterface class
# quiz_ui = QuizInterface()
