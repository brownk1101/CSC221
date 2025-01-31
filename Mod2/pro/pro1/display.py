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


def survivor_amounts(people, who: str = "All") -> None:
    """Prints the amount of survivors vs dead for a given group of people.

    Parameters
    ----------
    data: tuple[int, int] | tuple[tuple[int, int], tuple[int, int]]
        The survivor amounts to display.
    who: str
        The group of passengers to print information about.
        Options: "All", "Both", "Females Survived", "Males Survived"
    """
    print()
    match who:
        case "All":
            survivors = people[0][0] + people[1][0]
            dead = people[0][1] + people[1][1]
            print(f"Survivors: {survivors}, Dead: {dead}")
        case "Both":
            print(f" Female Survivors: {people[0][0]}, Female  Dead: {people[0][1]}")
            print(f" Male Survivors: {people[1][0]}, Male  Dead: {people[1][1]}")
        case "Females Survived":
            print(f" Female Survivors: {people[0][0]}, Female  Dead: {people[0][1]}")
        case "Males Survived":
            print(f" Male Survivors: {people[0][0]}, Male  Dead: {people[0][1]}")

    print()
