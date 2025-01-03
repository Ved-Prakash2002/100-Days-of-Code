from question_model import Question  # Import the Question class to create question objects.
from data import question_data  # Import the question data (list of dictionaries with questions and answers).
from quiz_brain import QuizBrain  # Import the QuizBrain class to manage quiz logic.
from ui import QuizInterface  # Import the QuizInterface class to handle the graphical user interface.

# Initialize an empty list to store question objects.
question_bank = []

# Loop through each question in the imported question data.
for question in question_data:
    # Extract the question text and correct answer from the dictionary.
    question_text = question["question"]
    question_answer = question["correct_answer"]

    # Create a new Question object with the text and answer.
    new_question = Question(question_text, question_answer)

    # Add the newly created Question object to the question bank.
    question_bank.append(new_question)

# Create a QuizBrain object, passing the question bank as input.
quiz = QuizBrain(question_bank)

# Create a QuizInterface object, passing the QuizBrain object for managing the quiz flow.
quiz_ui = QuizInterface(quiz)

# Continue presenting questions while there are still questions left in the quiz.
while quiz.still_has_questions():
    quiz.next_question()  # Call the next_question method to display the next question.

# Print a message when the quiz is complete.
print("You've completed the quiz")

# Print the final score of the user out of the total number of questions.
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
