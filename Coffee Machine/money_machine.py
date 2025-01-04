class MoneyMachine:
    """
    Models the functionality of a payment system for a vending machine.
    Handles coin processing, payment validation, and tracking profits.
    """

    # Constant for the currency symbol.
    CURRENCY = "$"

    # Dictionary defining the values of different coin types.
    COIN_VALUES = {
        "quarters": 0.25,  # Value of a quarter in dollars.
        "dimes": 0.10,  # Value of a dime in dollars.
        "nickles": 0.05,  # Value of a nickel in dollars.
        "pennies": 0.01  # Value of a penny in dollars.
    }

    def __init__(self):
        """
        Initializes the MoneyMachine with a starting profit of 0 and no money received.
        """
        self.profit = 0  # Total profit collected by the machine.
        self.money_received = 0  # Total money received from the user during a transaction.

    def report(self):
        """
        Prints a report of the current total profit made by the machine.
        """
        print(f"Money: {self.CURRENCY}{self.profit}")  # Display the profit in the specified currency.

    def process_coins(self):
        """
        Prompts the user to insert coins and calculates the total amount inserted.

        Returns:
        - The total amount of money received (sum of all coin values entered).
        """
        print("Please insert coins.")  # Prompt the user to insert coins.
        for coin in self.COIN_VALUES:  # Loop through each coin type.
            # Ask the user how many of each coin type they are inserting.
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received  # Return the total money received.

    def make_payment(self, cost):
        """
        Validates the payment and determines if the user has inserted enough money.

        Parameters:
        - cost: The cost of the item being purchased.

        Returns:
        - True if payment is sufficient and accepted.
        - False if payment is insufficient, with a refund message.
        """
        # Process the coins inserted by the user.
        self.process_coins()

        # Check if the money received is sufficient to cover the cost.
        if self.money_received >= cost:
            # Calculate and return the change to the user.
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")  # Inform the user of their change.

            # Add the cost of the item to the machine's profit.
            self.profit += cost

            # Reset the money received for the next transaction.
            self.money_received = 0
            return True  # Indicate that the payment was successful.
        else:
            # Inform the user that the payment was insufficient and refund the money.
            print("Sorry that's not enough money. Money refunded.")

            # Reset the money received for the next transaction.
            self.money_received = 0
            return False  # Indicate that the payment was unsuccessful.
