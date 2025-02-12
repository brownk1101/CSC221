"""Menu Functions"""

from util import clear_screen

def print_main_menu() -> None:
    """Clear the screen, then print the main menu"""
    clear_screen()
    print(f"{'Main Menu':-^35}")
    print("1. Enter \"Sec Divisions\" code")
    print("2. Get Course Enrollment Percentage")
    print("3. FTE by Division")
    print("4. FTE per Instructor")
    print("5. FTE per course")
    print("6. Exit")


def get_main_menu_choice() -> int:
    """Prompt user for main menu choice and validate against main menu options

    Returns
    -------
    int
        User's menu choice.
    """
    choice = 0
    while choice < 1 or choice > 6:
        try:
            choice = int(input("Enter an option between 1 and 6: "))
        except ValueError:
            print("Invalid: please enter a valid integer.")
            continue

    return choice


def print_submenu(header: str, options: list[str]) -> None:
    """Clear the screen, then print formatted submenu

    Parameters
    ----------
    header: str
        Submenu header
    options: list[str]
        Submenu options
    """
    clear_screen()
    # Get the amount of digits in the length of options (e.g. 15 = 2 digits).
    length_digits = len(str(len(options)))
    # Add 2 to account for the '. ' in the print loop.
    length_formatting = length_digits + 2
    # Get the length of the longest option for formatting.
    max_length = max([len(op) + length_formatting for op in options])
    if max_length < len(header):
        max_length = len(header) + length_digits 

    print(f"{header:-^{max_length}}")
    for i, option in enumerate(options):
        print(f"{i + 1:>{length_digits}}. {option}")


def get_submenu_choice(options: list[str]) -> int:
    """Prompts user for choice, validates, returns choice.

    Parameters
    ----------
    options: list[str]
        List of options.

    Returns
    -------
    int
        User choice
    """
    user_input = 0
    while user_input not in range(1, len(options)):
        try:
            user_input = int(input(f"Enter a number between 1 and {len(options)}: "))
        except ValueError:
            # Ignoring anything other than a number in the correct range
            ...
    return user_input
