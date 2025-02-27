"""Menu functions"""


def print_main_menu():
    """Prints the main menu."""
    print(f"{'Main Menu': ^40}")
    print(f"{'':->40}")
    print("1. View all recipes")
    print("2. Search for a recipe by name")
    print("3. Filter recipes by type (Dessert, Main Course, Vegetarian)")
    print("4. Exit the program")
    print()


def get_menu_choice(num):
    """Prompts user for input and returns an int.

    Prompts user for a number between 1 and num.

    Params
    ------
    num: int
        Max number to match.
    """
    valid = False
    while not valid:
        try:
            choice = int(input("Choose an option: "))
            if choice < 1 or choice > num:
                raise ValueError
            print()
        except ValueError:
            print(f"Please enter a valid integer between 1 and {num}")
            print()
        else:
            valid = True

    return choice


def get_recipe_name():
    """Prompts a user for input and returns a string.

    Returns
    -------
    str
        user entered string formatted with title().
    """
    user_input = input("Enter recipe name: ")
    return user_input.title()


def print_filter_menu():
    print("Filter options:")
    print("1. Dessert")
    print("2. Main Course")
    print("3. Vegetarian")
