"""Module containing program options."""


import pandas as pd
import load
import menu
import transform
import util


def print_option1_instructions() -> None:
    """Print Instructions for option 1"""
    print()
    print("Option 1 instructions:")
    print(f"{'':-^22}")
    print("Enter the number of the option you'd like to do, then press return.")
    print("""You can enter multiple values before typing the number for 'Finish
           entering codes'""")
    print("""If you choose the 'All' option at any point, the program will create
           excel sheets for all divisions regardless of other input.""")
    print("""If you choose 'Return to Main Menu', the program will ignore all
           previous input and return to the Main Menu.""")
    print("Press enter to continue")
    input()


def option1(data: pd.DataFrame):
    """Prompts user for division codes to create excel sheets.

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame to create excel sheets from.
    """
    print_option1_instructions()
    unique_codes = transform.get_column_uniques(data, "Sec Divisions")
    header = "Sec Divisions"
    options = { 0: "All" }
    for i, code in enumerate(unique_codes):
        options[i + 1] = code
    options[len(options)] = "No code"
    options[len(options)] = "Finish entering codes"
    options[len(options)] = "Return to Main Menu"
    menu.print_submenu(header, options)

    choice_list: list[int] = []
    all = False
    keep_entering = True
    while keep_entering:
        choice = menu.get_submenu_choice(len(options))
        if choice == 0:
            all = True
            keep_entering = False
        elif options[choice].startswith("Finish"):
            keep_entering = False
        elif options[choice].startswith("Return"):
            keep_entering = False
            choice_list = []
        else:
            choice_list.append(choice)

    if all:
        for code in unique_codes:
            frame = transform.get_division_frame(data, code)
            load.create_excel_sheets(frame, code.casefold())
        frame = transform.get_division_frame(data, None)
        load.create_excel_sheets(frame, "no_division")

    elif len(choice_list) > 0:
        for choice in choice_list:
            frame = transform.get_division_frame(data, options[choice])
            if options[choice] == "No code":
                load.create_excel_sheets(frame, "no_division")
            else:
                load.create_excel_sheets(frame, options[choice].casefold())


def option2(data: pd.DataFrame) -> None:
    """Prompts user for course name and then creates an excel sheet with
       pertinent information for that course.

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame to extract course information from.
    """
    # This get ALL of the variations of each course, all the sections we
    # don't need.
    courses = transform.get_column_uniques(data, "Sec Name")
    # We cut it down to just the unique courses here
    course_codes = util.get_course_codes(courses)

    choice = menu.submenu_option2(course_codes)
    if choice is not None:
        frame = transform.get_course_frame(data, choice)

        # Calculate enrollment percentage
        frame["Calculated Percentage"] = \
        ((frame["FTE Count"] / frame["Capacity"]) * 100).round(1).astype(str)+"%"

        choice = choice.split("-")
        choice = choice[0].lower() + choice[1] + "_per"
        load.create_excel_sheets(frame, choice)


def option3(data: pd.DataFrame) -> None:
    """Prompts user for division code and then creates an excel sheet with
       FTE information for the courses within that division

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame to extract information from
    """
    unique_divisions = transform.get_column_uniques(data, "Sec Divisions")
    header = "Sec Divisions"
    options: dict[int, str] = {}
    for i, division in enumerate(unique_divisions):
        options[i] = division
    options[len(options)] = "No code"
    options[len(options)] = "Return to Main Menu"
    menu.print_submenu(header, options)

    # Get the division
    choice = menu.get_submenu_choice(len(options))
    division_frame = transform.get_division_frame(data, options[choice])

    # Filter for the necessary columns
    columns_needed = ["Sec Name", "X Sec Delivery Method", "Meeting Times",
                      "Capacity", "FTE Count", "Total FTE", "Sec Faculty Info"]
    division_frame = division_frame[columns_needed]
    division_frame = pd.DataFrame(division_frame) # To convince my linter that this is in fact a dataframe

    #Get the courses in the division
    courses = transform.get_column_uniques(division_frame, "Sec Name")
    course_codes = sorted(util.get_course_codes(courses))

    headers = columns_needed
    headers.insert(0, options[choice])
    headers.insert(1, "Course Code")
    headers.append("Generated FTE")

    load.create_option3_sheet(division_frame, options[choice], course_codes, headers)
