class MenuItem:
    """Models each Menu Item."""

    def __init__(self, name, water, milk, coffee, cost):
        """
        Initializes a MenuItem object with its name, required ingredients, and cost.

        Parameters:
        - name: The name of the menu item (e.g., "latte").
        - water: The amount of water required in milliliters.
        - milk: The amount of milk required in milliliters.
        - coffee: The amount of coffee required in grams.
        - cost: The price of the menu item in dollars.
        """
        self.name = name  # Name of the menu item.
        self.cost = cost  # Cost of the menu item.
        # Ingredients dictionary containing the amounts of water, milk, and coffee required.
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""

    def __init__(self):
        """
        Initializes the Menu object with a predefined list of MenuItem objects.
        Each MenuItem represents a drink available on the menu.
        """
        self.menu = [
            # Add predefined MenuItem objects to the menu list.
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """
        Returns a string of all the available menu items separated by slashes.
        This is used to display options to the user.

        Returns:
        - A string containing all menu item names separated by '/' (e.g., "latte/espresso/cappuccino/").
        """
        options = ""  # Initialize an empty string to store item names.
        for item in self.menu:  # Loop through each MenuItem in the menu.
            options += f"{item.name}/"  # Append the item's name followed by a '/'.
        return options  # Return the formatted string of item names.

    def find_drink(self, order_name):
        """
        Searches the menu for a specific drink by its name.

        Parameters:
        - order_name: The name of the drink to search for.

        Returns:
        - The MenuItem object if the drink is found.
        - None if the drink is not available.
        """
        for item in self.menu:  # Loop through each MenuItem in the menu.
            if item.name == order_name:  # Check if the item's name matches the order name.
                return item  # Return the MenuItem object if found.
        print("Sorry that item is not available.")  # Print a message if the item is not found.
