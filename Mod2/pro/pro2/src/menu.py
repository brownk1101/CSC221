"""Menu Functions"""

def print_main_menu() -> None:
    """Print the main menu"""
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
    choice: int = 0
    while choice < 1 or choice > 6:
        try:
            choice = int(input("Enter an option between 1 and 6: "))
        except ValueError:
            print("Invalid: please enter a valid integer.")
            continue

    return choice


def print_submenu(header: str, options: tuple[str]) -> None:
    """Print formatted submenus

    Parameters
    ----------
    header: str
        Submenu header
    options: tuple[str]
        Submenu options
    """
    # Get the length of the longest option for formatting
    max_length = max([len(op) for op in options])
    if max_length < len(header):
        max_length = len(header) + 2 

    print(f"{header:-^{max_length}}")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
