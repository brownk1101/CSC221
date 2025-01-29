# This program demonstrates using Pandas DataFrames
# 01/28/2025
# CSC221 M2Lab-Panda DF
# Harley Coughlin

import pandas as pd


def main():
    """Entry point to the program. Calls all other functions"""

    error = False
    done = False

    while not error and not done:
        print("Stage 1: Loading and getting information")
        print("Loading djia.csv")

        # My LSP kept yelling at me that djia was possibly unbound.
        djia: pd.DataFrame = pd.DataFrame()

        try:
            djia = pd.read_csv("./djia.csv", index_col="Symbol")
        except FileNotFoundError:
            print("Couldn't find djia.csv in the current directory")
            error = True

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

        done = True
    ...


if __name__ == "__main__":
    main()
