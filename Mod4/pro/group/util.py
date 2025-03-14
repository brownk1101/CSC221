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

    # Search for an exact faculty match
    name = [n for n in to_search if search_for == n]

    # If no exact match, attempt to match last names
    if not name:
        try:
            search_last = search_for.split()[1]  # Extract last name
            name = [n for n in to_search if n.split()[1] == search_last]
        except IndexError:
            # If user only provided one name, check against last names in the list
            name = [n for n in to_search if search_for == n.split()[1]]

    # If still no match, compare first initials
    if not name:
        name = [n for n in to_search if search_for[0] == n[0]]

    # Return None if no match found
    return name if name else None





