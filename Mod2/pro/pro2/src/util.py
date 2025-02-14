"""Utility functions."""

import os
import re
import subprocess

def clear_screen() -> None:
    """OS sensitive clear command."""
    clear = "clear" if os.name == "posix" else "cls"
    subprocess.run(clear)


def get_course_codes(courses: list[str]) -> set[str]:
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
    course_codes: set[str] = set()
    for code in courses:
        course_code = re.match(course_code_pattern, code)
        if course_code is not None:
            course_codes.add(course_code[1])

    return course_codes
