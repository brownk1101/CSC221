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
    print()
    print(data.head(amount))
    print()


def records_amount(data: pd.DataFrame) -> None:
    """Prints the amount of records in the DataFrame, not including the header

    Parameters
    ----------
    data: DataFrame
        The DataFrame to display the amount of records
    """
    print()
    print(f"Amount of passengers: {len(data)}")
    print()


def survivor_amounts(people: pd.DataFrame | pd.Series , who: str = "all") -> None:
    """Prints the amount of survivors vs dead for a given group of people.

    Parameters
    ----------
    people: pd.DataFrame | pd.Series
        The survivor amounts to display.
    who: str
        The group of passengers to print information about.
        Options: "all", "both", "females survived", "males survived"
    """
    print()
    match who:
        case "all":
            print(f"Dead: {people.dead.sum():>7}")
            print(f"Survived: {people.survived.sum()}")
        case "both":
            print(people)
        case "females survived":
            print(people)
        case "males survived":
            print(people)
        case "class":
            print(people)
    print()


def survivor_amounts_by_travel(people: pd.DataFrame | pd.Series) -> None:
    """Prints information related to the statistics of people traveling alone vs in a group.

    Parameters
    ----------
    people: pd.DataFrame | pd.Series
        The survivor amounts to display.
    """
    print()
    print("Passenger amounts:")
    print(people.sum(axis=1).to_string(dtype=False))
    print(f"{'':~^21}")

    print("Survivorship by group:")
    print(people)
    print(f"{'':~^21}")

    print("Percentage of survivors by group:")
    passenger_totals = people.sum(axis=1)
    passenger_percentages = (people["survived"] / passenger_totals  * 100).round(2)
    print(passenger_percentages.to_string(dtype=False))
    print()
