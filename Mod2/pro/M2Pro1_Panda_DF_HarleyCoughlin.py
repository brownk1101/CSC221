# This a menu driven program using DataFrames, exception handling, functions, and file processing
# 01/29/2025
# CSC221 M2Pro1-Panda DF
# Harley Coughlin

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
    """This function prompts the user for input, validates it, then returns the
    input

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


def main():
    choice: int = 0
    while choice != 8:
        print_menu()
        choice = get_menu_choice()


if __name__ == "__main__":
    main()
