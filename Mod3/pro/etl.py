"""Recipe extraction, transformation, and loading functions."""


import os
import pandas as pd

from recipe import DessertRecipe, MainCourseRecipe


def extract_recipes(file_name):
    """Extracts recipes from an excel sheet located in the current directory.

    Params
    ------
    file_name: str
        Name of the excel file to exctract from.

    Returns
    -------
    pd.DataFrame
        A dataframe of the extracted information.
    """
    file_path = os.path.join(os.getcwd(), file_name)
    # If the file doesn't exist in the current directory, raise an error.
    if not os.path.isfile(file_path):
        raise FileNotFoundError

    recipes = pd.read_excel(file_path)
    return recipes


def get_recipe_instances(recipe_dataframe):
    """Creates instances of recipes from a DataFrame.

    Params
    ------
    recipe_dataframe: pd.DataFrame
        A dataframe containing the recipe information.

    Returns
    -------
    list[DessertRecipe | MainCourseRecipe]
        A list of recipe instances from the dataframe.
    """
    recipes = []
    for _, series in recipe_dataframe.iterrows():
        try:
            if series["Type"] == "Dessert":
                recipe_type = "Dessert"
                column_name = "Sweetness_Level"
            elif series["Type"] == "Main Course":
                recipe_type = "Main Course"
                column_name = "Spice_Level"
            else:
                raise ValueError(series["Type"])
        except KeyError:
            print("Error: column 'Type' doesn't exist.")
            break
        except ValueError as e:
            print(f"Error: column 'Type' value {e} is an invalid recipe type")
        
        try:
            name = series["Name"]
        except KeyError:
            print("Error: column 'Name' doesn't exist.")
            break

        try:
            ingredients = [str(ing).strip() for ing in series["Ingredients"].split(",")]
        except KeyError:
            print("Error: column 'Ingredients' doesn't exist.")
            break

        try:
            steps = [str(step).strip() for step in series["Steps"].split(",")]
        except KeyError:
            print("Error: column 'Steps' doesn't exist.")
            break

        try:
            vegetarian = series["Is_Vegetarian"]
        except KeyError:
            print("Error: column 'Is_Vegetarian' doesn't exist.")
            break

        try:
            if recipe_type == "Dessert":
                level = int(series[column_name])
            elif recipe_type == "Main Course":
                level = int(series[column_name])
        except ValueError:
            print(f"Warning: No value found in column '{column_name}' for"
                  f" {name} recipe defaulting to 0.\n")
            level = 0
        except KeyError:
            print(f"Error: column '{column_name}' doesn't exist.")
            break


        # Create and append the instance.
        if recipe_type == "Dessert":
            recipes.append(DessertRecipe(name, ingredients, steps, vegetarian, level))
        elif recipe_type == "Main Course":
            recipes.append(MainCourseRecipe(name, ingredients, steps, vegetarian, level))

    return recipes
