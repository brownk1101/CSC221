"""Utility functions."""

import os
import re
import subprocess


def clear_screen():
    """OS sensitive clear command."""
    clear = "clear" if os.name == "posix" else "cls"
    subprocess.run(clear)


def get_course_codes(courses):
    """Cuts the section portion out of course codes.

    Parameters
    ----------
    courses: list[str]
        List of courses with sections.

    Returns
    -------
    set[str]
        Set of course codes without sections.
    """
    course_code_pattern = r"^([A-Z]{3}-\d{3}[A-Z]?)"
    course_codes = set()
    for code in courses:
        course_code = re.match(course_code_pattern, code)
        if course_code is not None:
            course_codes.add(course_code[1])

    return course_codes


def find_faculty(search_for, to_search):
    """Searches faculty names for a match and returns None or the name in a
       list

    Parameters
    ----------
    search_for: str
        The name to search for.
    to_search: list[str]
        The names to search.

    Returns
    -------
    None | list[str]
        If not found returns None. Else, returns a list of all matches.
    """
    # Search for a full match
    name = [name for name in to_search if search_for == name]
    # Failing finding a match, try to split user input
    try:
        # If user entered first and last names, get the last name and check
        # against the last names from the list.
        if len(name) == 0:
            name = [name for name in to_search if
                    search_for.split()[1] == name.split()[1]]
    except IndexError:
        # If the user only entered first or last name, try them against the
        # last names of the list.
        name = [name for name in to_search if search_for == name.split()[1]]
        ...
    # Failing matching the last name, take the first initial of user input
    # and try to match it against the first initial from the list.
    if len(name) == 0:
        name = [name for name in to_search if search_for[0] == name[0]]
    # If we didn't find any matches at all, return None
    if len(name) == 0:
        name = None

    return name
