"""This module is for data extraction"""

import os
import pandas as pd

def extract_data(filename: str) -> pd.DataFrame:
    current_directory = os.getcwd()
    filepath = os.path.join(current_directory, filename)
    titanic = pd.read_excel(filepath)

    # If the read_excel fails to read anything
    if titanic.empty:
        raise RuntimeError(f"Failed to load data from {filename}")

    return titanic
