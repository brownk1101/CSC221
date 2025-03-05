"""Module containing program options."""


import load
import menu
import transform
import util


def print_option1_instructions():
    """Print Instructions for option 1"""
    print()
    print("Option 1 instructions:")
    print(f"{'':-^22}")
    print("To finish entering division codes, you must enter the option for "
          "'Finish entering codes'")
    print("Press any key to continue.")
    input()


def option1(data):
    """Prompts user for division codes to create excel sheets.

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame to create excel sheets from.
    """
    print_option1_instructions()
    unique_codes = transform.get_column_uniques(data, "Sec Divisions")
    header = "Sec Divisions"
    options = ["All"]
    options.extend(unique_codes)
    options.append("No code")
    options.append("Finish entering codes")
    options.append("Return to Main Menu")
    menu.print_menu(header, options)

    choice_list = []
    all = False
    keep_entering = True
    while keep_entering:
        choice = menu.get_menu_choice(len(options))
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


def course_enrollment_percentage(data):
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
        frame = transform.get_course_frame(data, choice, False).copy()

        # Calculate enrollment percentage
        enrollment_percentage = ((frame["FTE Count"] / frame["Capacity"]) * 100)
        enrollment_percentage = enrollment_percentage.round(1).astype(str)+"%"
        frame["Calculated Percentage"] = enrollment_percentage

        choice = choice.split("-")
        choice = choice[0].lower() + choice[1] + "_per"
        load.create_excel_sheets(frame, choice)


def fte_per_division(data):
    """Prompts user for division code and then creates an excel sheet with
       FTE information for the courses within that division

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame to extract information from
    """
    unique_divisions = transform.get_column_uniques(data, "Sec Divisions")
    header = "FTE by Division"
    unique_divisions.append("No code")
    unique_divisions.append("Return to Main Menu")
    menu.print_menu(header, unique_divisions)

    # Get the division
    choice = menu.get_menu_choice(len(unique_divisions))
    division_frame = transform.get_division_frame(data,
                                                  unique_divisions[choice])

    # Filter for the necessary columns
    columns_needed = ["Sec Name", "X Sec Delivery Method", "Meeting Times",
                      "Capacity", "FTE Count", "Total FTE", "Sec Faculty Info"]
    division_frame = division_frame[columns_needed]
    division_frame["Generated FTE"] = None

    # Get the courses in the division
    courses = transform.get_column_uniques(division_frame, "Sec Name")
    course_codes = sorted(util.get_course_codes(courses))

    load.create_fte_excel(data=division_frame, name=unique_divisions[choice],
                          course_codes=course_codes,
                          first_cell=unique_divisions[choice])


def fte_per_faculty(data):
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


def fte_per_course(data):
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
