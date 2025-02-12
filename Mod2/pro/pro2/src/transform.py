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


def get_division_codes(data: pd.DataFrame) -> list[str]:
    """Extracts unique division codes from a DataFrame.

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame to read division codes from.

    Returns
    -------
    list[str]
        List of unique division codes.
    """
    unique_values = data["Sec Divisions"].dropna().unique()
    # Explicit conversion to list[str] so my lsp will stop yelling at me.
    return [str(x) for x in unique_values]


def get_division_frame(data: pd.DataFrame, name: str | None):
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
    return frame
