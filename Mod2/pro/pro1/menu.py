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


def print_submenu(header: str, options: tuple[str, ...]) -> None:
    """Print formatted submenu.

    Parameters
    ----------
    header: str
        Title for the menu.
    options: tuple[str, ...]
        Tuple of strings that contains: Header, opitions.
    """
    # Menu header
    print(header)
    # Menu options.
    for i in range(len(options)):
        print(options[i])


def get_submenu_choice(choices: tuple[str, ...]) -> str:
    """Prompts user to enter string, validates against submenu choices.

    Parameters
    ----------
    choices: tuple[str, ...]
        Tuple of strings with valid submenu choices.
    
    Returns
    -------
    choice: str
        Menu option entered by the user.
    """
    choice = ""

    choice = input("Please type your choice: ")
    choice = choice.strip().lower()

    while choice not in choices:
        choice = input("Invalid: Please type your choice: ")
        choice = choice.strip().lower()

    return choice
