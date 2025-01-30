"""This module is for displaying information."""

import pandas as pd

def first_fifteen(data: pd.DataFrame, amount: int = 15) -> None:
    """Prints an amount of rows from the top of a DataFrame.

    Parameters
    ----------
    data: DataFrame
        The DataFrame to display information from.
    amount: int (default 15)
        The amount of rows from the top to display.
    """
    print(data.head(amount))


def records_amount(data: pd.DataFrame) -> None:
    """Prints the amount of records in the DataFrame, not including the header

    Parameters
    ----------
    data: DataFrame
        The DataFrame to display the amount of records
    """
    print(f"Amount of passengers: {len(data)}")


def survivor_amounts(data: tuple[int], separate: bool = False) -> None:
    """Prints the amount of survivors vs dead for a given group of people.

    Parameters
    ----------
    data: tuple[int]
        The survivor amounts to display.
    separate: bool (default = False)
        Whether or not to separate the groups information.
    """
    raise NotImplementedError
