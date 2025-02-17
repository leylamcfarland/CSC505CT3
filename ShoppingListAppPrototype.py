class ShoppingListAppPrototype:
    def __init__(self):
        # Define the screens in the app and their respective page count
        self.screens = {
            "Splash Screen": 1,
            "Home Screen": 1,
            "Add Item Screen": 1,
            "View List Screen": 1,
            "Settings Screen": 1
        }

        # Define the flow/sequence of pages
        self.flow = [
            "Splash Screen -> Home Screen",
            "Home Screen -> Add Item Screen",
            "Home Screen -> View List Screen",
            "Home Screen -> Settings Screen",
            "View List Screen -> Home Screen",
            "Add Item Screen -> Home Screen",
            "Settings Screen -> Home Screen"
        ]

    def print_prototype_info(self):
        # Print the screens and their page count
        print("Screens and their number of pages:")
        for screen, pages in self.screens.items():
            print(f"{screen}: {pages} page(s)")

        # Print the flow/sequence of pages
        print("\nSequence of pages:")
        for transition in self.flow:
            print(transition)


if __name__ == "__main__":
    # Instantiate the ShoppingListAppPrototype class
    app_prototype = ShoppingListAppPrototype()

    # Print the prototype information
    app_prototype.print_prototype_info()