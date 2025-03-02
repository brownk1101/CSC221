# This program creates spreadsheets of information on classes offered by FTCC
# 02/09/2025
# CSC221 M2Pro2 - FTE
# Harley Coughlin

import pandas as pd
import extract
import menu
import options
import transform


def main():
    # Control flow booleans
    error = False
    keep_going = True

    df = pd.DataFrame()
    filename = "deansDailyCsar.csv"

    print(f"Trying to extract from {filename}.")
    try:
        df = extract.extract_csv(filename=filename)
    except FileNotFoundError as e:
        print(f"""Unable to find the {filename}. Please make sure it exists in
                the current directory.""")
        print(f"Technical details: {e}")
        error = True
    except pd.errors.EmptyDataError as e:
        print(f"The input file {filename} is empty. Please check the file contents.")
        print(f"Technical details: {e}")
        error = True

    if not df.empty:
        print("Data extraction complete.")
        print("Sorting...")
        df = transform.sort_dataframe(df)
        print("Sorted.")
    else:
        print("Data failed to load.")
        error = True

    while not error and keep_going:
        menu.print_main_menu()
        option = menu.get_main_menu_choice()
        if option == 1:
            options.option1(df)
        elif option == 2:
            options.course_enrollment_percentage(df)
        elif option == 3:
            options.fte_per_division(df)
        elif option == 4:
            options.fte_per_faculty(df)
        elif option == 5:
            options.fte_per_course(df)
        elif option == 6:
            print("Thanks for playing.")
            keep_going = False
        else:
            print("You shouldn't be here.")
            keep_going = False


if __name__ == "__main__":
    main()
