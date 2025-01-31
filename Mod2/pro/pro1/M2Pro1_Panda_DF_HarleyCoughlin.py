# This a menu driven program using DataFrames, exception handling, functions, and file processing
# 01/29/2025
# CSC221 M2Pro1-Panda DF
# Harley Coughlin

import display
import extract
import menu
import transform
import pandas as pd


def main():
    choice = 0
    error = False
    filename = "Titanic.xlsx"
    titanic = pd.DataFrame()
    survivors = None

    try:
        titanic = extract.extract_data(filename=filename)
    except FileNotFoundError:
        print(f"File {filename} not found in current directory")
        print(f"""Please ensure {filename} is correctly named and within the
                  current directory""")
        error = True
    except RuntimeError as e:
        print(e)
        error = True

    while not error and choice != 8:
        menu.print_menu()
        choice = menu.get_menu_choice()
        match choice:
            case 1:
                display.first_fifteen(titanic)
            case 2:
                display.records_amount(titanic)
            case 3:
                try:
                    survivors = transform.get_survivors(titanic)
                    display.survivor_amounts(survivors)
                except ValueError as v:
                    print(v)
            case 4:
                menu.print_submenu_option4()
                submenu_choice = menu.get_submenu_option4_choice()
                try:
                    # There shouldn't be an error herer as validation occurs in
                    # menu.
                    survivors = transform.get_survivors(titanic, submenu_choice)
                    display.survivor_amounts(survivors, submenu_choice)
                except ValueError as v:
                    print(v)
            case 8:
                # TODO: Change this
                print("Thanks for stopping by.")


if __name__ == "__main__":
    main()
