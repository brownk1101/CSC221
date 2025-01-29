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
    print(f"{'':~>80}")

    return djia

def stage_two(djia: pd.DataFrame) -> None:
    """Display specific data from within the DataFrame.

    Parameters
    ----------
    djia: pd.DataFrame
        DataFrame to display information from.
    """
    print("Stage 2: Accessing rows, columns, and cells")
    print("Displaying Company column:")
    print(djia.Company)
    print()

    print("Displaying Company and Industry:")
    columns_to_display: list[str] = ["Company", "Industry"]
    print(djia[columns_to_display])
    print()

    print("Displaying AAPL row:")
    print(djia.loc["AAPL"])
    print()

    print("Displaying AAPL Exchange:")
    print(djia["Exchange"]["AAPL"])
    print()
    print(f"{'':~>80}")


def main():
    """Entry point to the program. Calls all other functions"""

    error = False
    done = False
    djia: pd.DataFrame = pd.DataFrame()

    while not error and not done:
        try:
            djia = stage_one("./djia.csv")
        except FileNotFoundError:
            print("Couldn't find djia.csv in the current directory")
            error = True

        stage_two(djia)

        done = True


if __name__ == "__main__":
    main()
