from menu import Menu, MenuItem  # Importing the Menu and MenuItem classes for menu operations.
from coffee_maker import CoffeeMaker  # Importing the CoffeeMaker class to manage resources and coffee making.
from money_machine import MoneyMachine  # Importing the MoneyMachine class to handle payments.

# Create an instance of MoneyMachine to handle transactions.
money_machine = MoneyMachine()

# Create an instance of CoffeeMaker to manage coffee resources and preparation.
coffee_maker = CoffeeMaker()

# Create an instance of Menu to display available coffee options and get details about drinks.
menu = Menu()

# A flag to control the main loop of the coffee machine.
is_on = True

# Main loop to keep the coffee machine operational until turned off.
while is_on is True:
    # Get a string of available menu items (e.g., "latte/espresso/cappuccino").
    options = menu.get_items()

    # Prompt the user to choose a drink or perform an action (e.g., 'off', 'report').
    choice = input(f"What would you like? {options}: ")

    # Check if the user input is 'off', which turns off the machine.
    if choice == 'off':
        is_on = False  # Set the flag to False to exit the loop.

    # Check if the user input is 'report', which prints the status of the machine and money.
    elif choice == 'report':
        coffee_maker.report()  # Display the current resource levels (water, milk, coffee).
        money_machine.report()  # Display the current amount of money collected.

    # For all other inputs, treat them as drink choices.
    else:
        # Find the drink object corresponding to the user's choice.
        drink = menu.find_drink(choice)

        # Check if the machine has enough resources to make the chosen drink.
        if coffee_maker.is_resource_sufficient(drink):
            # Process the payment for the drink.
            if money_machine.make_payment(drink.cost) is True:
                # If payment is successful, make the coffee.
                coffee_maker.make_coffee(drink)
