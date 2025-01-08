import random  # Importing the random module for generating random choices.


class PasswordGenerator:
    """
    A class to generate random secure passwords containing letters, numbers, and symbols.
    """

    def __init__(self):
        """
        Initializes the PasswordGenerator with predefined character sets:
        - Letters: Uppercase and lowercase alphabets.
        - Numbers: Digits from 0 to 9.
        - Symbols: Common special characters.
        """
        self.letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]  # List of uppercase and lowercase alphabets.
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # List of digits.
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']  # List of special characters.

    def generate_password(self):
        """
        Generates a random password with a mix of letters, symbols, and numbers.

        Returns:
        - A string representing the randomly generated password.
        """
        # Generate a random number of letters (between 8 and 10).
        letters_list = [random.choice(self.letters) for _ in range(random.randint(8, 10))]

        # Generate a random number of symbols (between 2 and 4).
        symbols_list = [random.choice(self.symbols) for _ in range(random.randint(2, 4))]

        # Generate a random number of numbers (between 2 and 4).
        numbers_list = [random.choice(self.numbers) for _ in range(random.randint(2, 4))]

        # Combine all characters into a single list.
        password_list = letters_list + symbols_list + numbers_list

        # Shuffle the combined list to randomize the order.
        random.shuffle(password_list)

        # Join the characters to form the final password string.
        password = "".join(password_list)

        return password  # Return the generated password.
