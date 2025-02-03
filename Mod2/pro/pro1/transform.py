"""This module is for data transformation."""

import pandas as pd


def get_survivors(data: pd.DataFrame, who: str = "both"):
    """Extracts information on survived vs dead for a given group of passengers

    Prameters
    ---------
    data: pd.DataFrame
        The DataFrame to extract information from.
    who: str (default = "both")
        The group of passengers to extract information about.

    Returns
    -------
    tuple
        if who="both", returns a tuple of ((female_alive, female_dead),
        (male_alive, male_dead))
        Otherwise returns a tuple of (alive, dead)
    """
    people = data.groupby("gender")["survived"].value_counts().unstack()
    people.columns = ["dead", "survived"]

    if who == "females survived":
        people = people.loc["female"]
    elif who == "males survived":
        people = people.loc["male"]

    return people

def get_survivors_by_class(data: pd.DataFrame):
    """Retrieve information on survivors/dead based on passenger class.

    Prameters
    ---------
    data: pd.DataFrame
        DataFrame to extract information from.

    Returns
    -------
    pd.DataFrame
        DataFrame containing survival statistics for passenger classes.
    """
    survival_counts = data.groupby("pclass")["survived"].value_counts().unstack()
    survival_counts.columns = ["dead", "survived"]
    return survival_counts
