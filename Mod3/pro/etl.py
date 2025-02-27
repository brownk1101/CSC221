"""Recipe extraction function"""


import os
import pandas as pd


def extract_recipes(file_name):
    """Extracts recipes from an excel sheet located in the current directory.

    Params:
    file_name: str
        Name of the excel file to exctract from.
    """
    file_path = os.path.join(os.getcwd(), file_name)
    # If the file doesn't exist in the current directory, raise an error.
    if not os.path.isfile(file_path):
        raise FileNotFoundError

    recipes = pd.read_excel(file_path)
    return recipes
