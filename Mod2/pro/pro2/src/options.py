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


def course_enrollment_percentage(data: pd.DataFrame) -> None:
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

    choice = menu.submenu_course_code(course_codes)
    if choice is not None:
        frame = transform.get_course_frame(data, choice)

        # Calculate enrollment percentage
        frame["Calculated Percentage"] = \
        ((frame["FTE Count"] / frame["Capacity"]) * 100).round(1).astype(str)+"%"

        choice = choice.split("-")
        choice = choice[0].lower() + choice[1] + "_per"
        load.create_excel_sheets(frame, choice)


def fte_per_division(data: pd.DataFrame) -> None:
    """Prompts user for division code and then creates an excel sheet with
       FTE information for the courses within that division

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame to extract information from
    """
    unique_divisions = transform.get_column_uniques(data, "Sec Divisions")
    header = "FTE by Division"
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
    division_frame["Generated FTE"] = None
    division_frame = pd.DataFrame(division_frame) # Ensure dataframe type

    # Get the courses in the division
    courses = transform.get_column_uniques(division_frame, "Sec Name")
    course_codes = sorted(util.get_course_codes(courses))

    load.create_fte_excel(data=division_frame, name=options[choice],
                          course_codes=course_codes, first_cell=options[choice])


def fte_per_faculty(data: pd.DataFrame) -> None:
    """Prompts user for faculty name and then creates an excel sheet with
       FTE information for the courses for that faculty member

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame to extract information from
    """
    unique_faculty = transform.get_column_uniques(data, "Sec Faculty Info")
    faculty_member = menu.fte_faculty_submenu(unique_faculty)
    if faculty_member is not None:
        faculty_frame = transform.get_faculty_frame(data, faculty_member)
        # Filter columns
        columns_needed = ["Sec Name", "X Sec Delivery Method", "Meeting Times",
                        "Capacity", "FTE Count", "Total FTE"]
        faculty_frame = faculty_frame[columns_needed]
        faculty_frame["Generated FTE"] = None
        faculty_frame = pd.DataFrame(faculty_frame) # Ensure dataframe type

        # Get the Courses for the faculty member
        courses = transform.get_column_uniques(faculty_frame, "Sec Name")
        course_codes = sorted(util.get_course_codes(courses))

        # Get the last name and first initial for the filename
        file_name = faculty_member.split()[1] + faculty_member[0]
        load.create_fte_excel(data=faculty_frame, name=file_name,
                              course_codes=course_codes,
                              first_cell=faculty_member)
    else:
        print("No faculty member selected")
        input("Press enter to continue")


def fte_per_course(data: pd.DataFrame) -> None:
    """Prompts user for course name and then creates an excel sheet with FTE
       information for all sections for that course

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame to extract information from.
    """
    courses = transform.get_column_uniques(data, "Sec Name")
    course_codes = util.get_course_codes(courses)
    choice = menu.submenu_course_code(course_codes)
    if choice is not None:
        load.create_fte_excel(data=data, name=choice,
                              course_codes=[choice], filter=False)
