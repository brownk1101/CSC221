"""Data transformations"""

import pandas as pd


def sort_dataframe(data: pd.DataFrame, sort_by: list[str] =
                   ["Sec Divisions", "Sec Name", "Sec Faculty Info"]
                   ) -> pd.DataFrame:
    """Sorts a DataFrame by columns, in ascending order.

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame to sort.
    sort_by: list[str] (default = ["Sec Divisions", "Sec Name", "Sec Faculty Info"])
        Column name(s) to sort by.

    Returns
    -------
    pd.DataFrame
        Sorted DataFrame
    """
    return data.sort_values(by=sort_by)


def get_column_uniques(data: pd.DataFrame, name: str) -> list[str]:
    """Extracts unique values from a column within a DataFrame.

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame to read from.
    name: str
        Name of the column to extract unique values.

    Returns
    -------
    list[str]
        List of unique values.
    """
    unique_values = data[name].dropna().unique()
    # Explicit conversion to list[str] so my lsp will stop yelling at me.
    return [str(x) for x in unique_values]


def get_division_frame(data: pd.DataFrame, name: str | None) -> pd.DataFrame:
    """Extracts all rows associated to a specific division code

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame to extract rows from.
    name: str
        The division code to target.
    """
    # Get empty cells
    if name is None or name == "No code":
        frame = data[data["Sec Divisions"].isna() |
                (data["Sec Divisions"] == "")]
    else:
        frame = data[data["Sec Divisions"] == name]
    frame = pd.DataFrame(frame)
    return frame


def get_course_frame(data: pd.DataFrame, name: str) -> pd.DataFrame:
    """Extracts rows associated with a course code, excluding rows for 
    face-to-face sections that have INET in the meeting times column.

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame to extract rows from.
    name: str
        Course code to filter for.

    Returns:
    pd.DataFrame
        All rows associated to the Course Code without face-to-face classes
        with INET meeting times.
    """
    # Get the course rows, ensure type is DataFrame.
    frame = data[data["Sec Name"].str.contains(name)]
    frame = pd.DataFrame(frame)
    # Get all the face-to-face sections.
    zero_sections = frame["Sec Name"].str.contains(r"-\d0\d\d")
    zero_frame = frame[zero_sections]
    # Group them together and take only the first record for each group.
    zero_frame = zero_frame.groupby("Sec Name", as_index=False).first()
    # Get all the other sections.
    non_zero_frame = frame[~zero_sections]
    # Put both frames together and ensure DataFrame type.
    frame = pd.DataFrame(pd.concat([zero_frame, non_zero_frame]))

    return frame


def get_faculty_frame(data: pd.DataFrame, name: str) -> pd.DataFrame:
    """Extracts rows associated with a faculty member or ones not assigned yet.

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame to extract rows from
    name: str
        Faculty name to filter for. 'To be Announced' if looking for unassigned
        courses.

    Returns
    -------
    pd.DataFrame
        All rows associated to the given faculty member of no faculty member.
    """
    # Get faculty rows
    frame = data[data["Sec Faculty Info"] == name]
    frame = pd.DataFrame(frame) # Ensure type is DataFrame

    return frame
