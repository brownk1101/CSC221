"""Menu Functions"""

from util import clear_screen, find_faculty

def print_main_menu():
    """Clear the screen, then print the main menu"""
    clear_screen()
    print(f"{'Main Menu':-^35}")
    print("1. Enter \"Sec Divisions\" code")
    print("2. Get Course Enrollment Percentage")
    print("3. FTE by Division")
    print("4. FTE per Instructor")
    print("5. FTE per course")
    print("6. Exit")


def get_main_menu_choice():
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


def print_submenu(header, options):
    """Clear the screen, then print formatted submenu

    Parameters
    ----------
    header: str
        Submenu header
    options: dict[int, str]
        Submenu options
    """
    clear_screen()
    # Get the amount of digits in the length of options (e.g. 15 = 2 digits).
    length_digits = len(str(len(options)))
    # Add 2 to account for the '. ' in the print loop.
    length_formatting = length_digits + 2
    # Get the length of the longest option for formatting.
    max_length = max([len(op) + length_formatting for _, op in options.items()])
    if max_length < len(header):
        max_length = len(header) + length_digits 

    print(f"{header:-^{max_length}}")
    for k, v in options.items():
        print(f"{k + 1:>{length_digits}}. {v}")


def get_submenu_choice(amount_options):
    """Prompts user for choice, validates, returns choice.

    Parameters
    ----------
    amount_options: int
        The amount of options presented to the end user.

    Returns
    -------
    int
        User choice
    """
    user_input = 0
    while user_input not in range(1, amount_options + 1):
        try:
            user_input = int(input(f"Enter a number between 1 and {amount_options}: "))
        except ValueError:
            # Ignoring anything other than a number in the correct range
            ...
    # Gotta remove the 1 added to the options when printed
    return user_input - 1


def submenu_course_code(courses):
    """Clear the screen, prompt the user for input, validate, and return it.

    Parameters
    ----------
    courses: list[str]
        List of valid course codes.

    Returns
    -------
    str
        Course code entered by the user.
    """
    clear_screen()
    print(f"{'Course Code':-^2}")

    choice = ""
    found = False
    keep_going = True
    while not found and keep_going:
        choice = input("Enter course code(or Q to quit): ")
        choice = choice.strip().upper()

        if choice == 'Q':
            keep_going = False
            choice = None
        elif choice in courses:
            found = True
        else:
            print(f"{choice} not found, please check spelling.")

    return choice


def fte_faculty_submenu(faculty):
    """Clear the screen, prompt the user for input, validate, and return it.

    Parameters
    ----------
    courses: list[str]
        List of valid course codes.

    Returns
    -------
    str
        The faculty member name.
    """
    choice = ""
    found = False
    keep_going = True
    found_name = None
    while not found and keep_going:
        clear_screen()
        print(f"{'FTE by Faculty':-^2}")
        print("Enter the first and/or last name of a faculty member,")
        print("or TBA for classes with no announced faculty.")
        choice = input("(Q to quit): ")
        choice = choice.strip().title()

        if choice == 'Q':
            keep_going = False
        elif choice == "Tba":
            found_name = "To be Announced"
            found = True
        elif found_name is None:
            found_name = find_faculty(choice, faculty)
            if isinstance(found_name, list):
                # If we found more than one name, prompt the user to choose
                # one of them or to search for a new name.
                if len(found_name) > 1:
                    options: dict[int, str] = {}
                    # Convert to a dict
                    for i, name in enumerate(found_name):
                        options[i] = name
                    options[len(options)] = "None of these"
                    # Present found options to user
                    print_submenu("Did you mean", options)
                    name_choice = get_submenu_choice(len(options))
                    if name_choice == len(options) - 1:
                        found_name = None
                    else:
                        found_name = options[name_choice]
                # If we find only one name, send it.
                else:
                    found_name = found_name[0]
                    found = True
        else:
            print(f"{choice} could not be found, please check spelling")
            print()

    return found_name
