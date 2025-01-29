# This program demonstrates using Pandas DataFrames
# 01/28/2025
# CSC221 M2Lab-Panda DF
# Harley Coughlin

import pandas as pd

def stage_one(pathname:str) -> pd.DataFrame:
    """This function loads a CSV into a DataFrame, displays it, and returns the
    DataFrame.
    
    Parameters
    ----------
    pathname: str
        The csv file to be loaded.

    Returns
    -------
    djia: pd.DataFrame
        The DataFrame created from the csv.
    """
    print("Stage 1: Loading and getting information")
    print("Loading djia.csv")

    djia = pd.read_csv(pathname, index_col="Symbol")

    print("djia.csv loaded")
    print(djia)
    print()

    print("PD info:")
    djia.info()
    print()

    print(f"Length: {len(djia)}")
    print(f"Shape: {djia.shape}")
    print()

    print(f"First row: {djia.head(1)}")
    print(f"Last row: {djia.tail(1)}")

    return djia


def main():
    """Entry point to the program. Calls all other functions"""

    error = False
    done = False

    while not error and not done:
        try:
            stage_one("./djia.csv")
        except FileNotFoundError:
            print("Couldn't find djia.csv in the current directory")
            error = True


        done = True
    ...


if __name__ == "__main__":
    main()
