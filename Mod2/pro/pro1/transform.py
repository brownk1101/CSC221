"""This module is for data transformation."""

import pandas as pd


def get_survivors(data: pd.DataFrame, who: str = "Both"):
    """Extracts information on survived vs dead for a given group of passengers

    Prameters
    ---------
    data: pd.DataFrame
        The DataFrame to extract information from.
    who: str (default = "Both")
        The group of passengers to extract information about.

    Returns
    -------
    tuple
        if who="Both", returns a tuple of ((female_alive, female_dead),
        (male_alive, male_dead))
        Otherwise returns a tuple of (alive, dead)
    """
    if who == "Both":
        return (get_survivors(data, "Females Survived"),
                get_survivors(data, "Males Survived"))
    else:
        if who == "Females Survived":
            filter = "female"
        elif who == "Males Survived":
            filter = "male"
        else:
            raise ValueError("""'who' must be 'Both', 'Females Survived', or
                                'Males Survived'""")
        people = data[data.gender == filter]["survived"]
        amount_alive = 0
        amount_dead = 0
        # Count survived(1) and dead(0)
        for person in people:
            if person == 1:
                amount_alive += 1
            else:
                amount_dead += 1

        return (amount_alive, amount_dead)
