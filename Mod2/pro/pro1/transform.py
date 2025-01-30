"""This module is for data transformation."""

import pandas as pd


def get_survivors(data: pd.DataFrame, who: str = "Both") -> tuple[int, int]:
    """Extracts information on survived vs dead for a given group of passengers

    Prameters
    ---------
    data: pd.DataFrame
        The DataFrame to extract information from.
    who: str (default = "Both")
        The group of passengers to extract information about.
    """
    to_return: pd.DataFrame = pd.DataFrame()
    amount_survived = 0
    amount_dead = 0
    match who:
        case "Both":
            raise NotImplementedError
        case "Females Survived":
            raise NotImplementedError
        case "Males Survived":
            raise NotImplementedError
