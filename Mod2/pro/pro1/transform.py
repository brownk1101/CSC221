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
    if who == "both":
        return (get_survivors(data, "females survived"),
                get_survivors(data, "males survived"))
    else:
        if who == "females survived":
            filter = "female"
        elif who == "males survived":
            filter = "male"
        else:
            raise ValueError("""'who' must be 'both', 'females survived', or
                                'males survived'""")
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
