# This program creates spreadsheets of information on classes offered by FTCC
# 02/09/2025
# CSC221 M2Pro2 - FTE
# Harley Coughlin

import pandas as pd
import menu
import extract


def main():
    df = pd.DataFrame()
    filename = "deansDailyCsar.csv"
    try:
        df = extract.extract_csv(filename=filename)
    except FileNotFoundError as e:
        print(f"""Unable to find the {filename}. Please make sure it exists in
                 the results/input directory.""")
        print(f"Technical details: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"The input file {filename} is empty. Please check the file contents.")
        print(f"Technical details: {e}")
    print(df)


if __name__ == "__main__":
    main()
