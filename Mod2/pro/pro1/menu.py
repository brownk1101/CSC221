"""This module contains functions related to the menu of M2Pro1"""

def print_menu() -> None:
    """This function prints the menu"""
    print("M2Pro: Titanic")
    print("1. Display Dataset")
    print("2. Get the number of records(passengers) listed in the dataset.")
    print("3. Get the number of Survived vs Dead.")
    print("4. Get the number of Females and/or Males.")
    print("5. Get the number of passengers per class.")
    print("6. Get the number of passengers traveling alone(Survived vs Dead)")
    print("7. Get the number of Survived vs Dead by age group")
    print("8. Exit")


def get_menu_choice() -> int:
    """This function prompts the user for input, validates it, then returns the input.

    Returns
    -------
    choice: int
        Menu option entered by the user.
    """
    choice: int = 0
    while choice < 1 or choice > 8:
        try:
            choice = int(input("Enter an option between 1 and 8: "))
        except ValueError:
            print("Invalid: please enter a valid integer.")
            continue

    return choice


def print_submenu_option4():
    """Print menu option 4 submenu."""
    print()
    print("Option 4 submenu")
    print("Females Survived")
    print("Males Survived")
    print("Both")

def get_submenu_option4_choice() -> str:
    """Prompts user to enter string, validates against submenu options.
    
    Returns
    -------
    choice: str
        Menu option entered by the user.
    """
    choices = ["females survived", "males survived", "both"]
    choice = ""

    choice = input("Please type your choice: ")
    choice = choice.strip().lower()

    while choice not in choices:
        choice = input("Invalid: Please type your choice: ")
        choice = choice.strip().lower()

    return choice
