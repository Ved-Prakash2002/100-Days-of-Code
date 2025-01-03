import html  # Import the html module to handle HTML entities in question text


class QuizBrain:
    """
    A class that manages the quiz logic, including tracking the question number,
    score, and verifying answers.
    """

    def __init__(self, q_list):
        """
        Initialize the QuizBrain with a list of questions.

        Parameters:
        q_list (list): A list of Question objects.
        """
        self.question_number = 0  # Initialize the current question number
        self.score = 0  # Initialize the user's score
        self.question_list = q_list  # Store the list of questions
        self.current_question = None  # Initialize the current question as None

    def still_has_questions(self):
        """
        Check if there are more questions left in the quiz.

        Returns:
        bool: True if there are questions remaining, False otherwise.
        """
        return self.question_number < len(self.question_list)  # Compare current question index with total questions

    def next_question(self):
        """
        Fetch the next question from the question list and update the question number.

        Returns:
        str: The formatted question text, decoded of any HTML entities.
        """
        self.current_question = self.question_list[self.question_number]  # Get the current question object
        self.question_number += 1  # Increment the question number
        q_text = html.unescape(self.current_question.text)  # Decode HTML entities in the question text
        return f"Q.{self.question_number}: {q_text} (True/False): "  # Format the question text for display

    def check_answer(self, user_answer):
        """
        Check if the user's answer is correct and update the score.

        Parameters:
        user_answer (str): The answer provided by the user.

        Returns:
        bool: True if the answer is correct, False otherwise.
        """
        correct_answer = self.current_question.answer  # Get the correct answer for the current question
        if user_answer.lower() == correct_answer.lower():  # Compare user's answer with the correct answer (case-insensitive)
            self.score += 1  # Increment the score for a correct answer
            return True  # Return True for a correct answer
        else:
            return False  # Return False for an incorrect answer
