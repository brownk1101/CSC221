# This program reads recipes from spreadsheets.
# 02/26/2025
# CSC221 M3Pro - Recipes
# Harley Coughlin

from etl import extract_recipes
from recipe import Recipe


def main():

    recipes = None
    file_name = "recipe_data.xlsx"
    try:
        recipes = extract_recipes(file_name)
    except FileNotFoundError:
        print(f"""{file_name} not found in current directory, please ensure the
        file exists and has the correct name""")

    if recipes is None:
        print("Something went wrong")
    else:
        for _, item in recipes.iterrows():
            recipe = Recipe(item["Name"], [str(ing) for ing in item["Ingredients"].split(",")], [str(ing) for ing in item["Steps"].split(",")], item["Is_Vegetarian"])
            recipe.display_recipe()



if __name__ == "__main__":
    main()
