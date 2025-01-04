class CoffeeMaker:
    """Models the machine that makes the coffee."""

    def __init__(self):
        """
        Initializes the CoffeeMaker with default resource quantities.
        The machine starts with predefined amounts of water, milk, and coffee.
        """
        self.resources = {
            "water": 300,  # Initial amount of water in milliliters.
            "milk": 200,  # Initial amount of milk in milliliters.
            "coffee": 100,  # Initial amount of coffee in grams.
        }

    def report(self):
        """
        Prints a report of all current resources in the machine.
        This method displays the quantities of water, milk, and coffee available.
        """
        print(f"Water: {self.resources['water']}ml")  # Print the amount of water remaining.
        print(f"Milk: {self.resources['milk']}ml")  # Print the amount of milk remaining.
        print(f"Coffee: {self.resources['coffee']}g")  # Print the amount of coffee remaining.

    def is_resource_sufficient(self, drink):
        """
        Checks if there are enough resources to make the selected drink.

        Parameters:
        - drink: An object representing the drink to be made (contains required ingredients).

        Returns:
        - True if there are sufficient resources to make the drink.
        - False if any ingredient is insufficient, and prints a message indicating the shortage.
        """
        can_make = True  # Assume the drink can be made initially.
        # Loop through the ingredients required for the drink.
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:  # Check if the required amount exceeds available.
                print(f"Sorry there is not enough {item}.")  # Inform the user of the shortage.
                can_make = False  # Set can_make to False if any resource is insufficient.
        return can_make  # Return the result of the check.

    def make_coffee(self, order):
        """
        Deducts the required ingredients for the drink from the machine's resources
        and serves the coffee.

        Parameters:
        - order: An object representing the drink to be made (contains required ingredients).
        """
        # Deduct each ingredient's quantity from the available resources.
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]

        # Print a message to indicate the coffee is ready.
        print(f"Here is your {order.name} ☕️. Enjoy!")
