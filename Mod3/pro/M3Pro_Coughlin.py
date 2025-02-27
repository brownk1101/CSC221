# This program reads recipes from spreadsheets.
# 02/26/2025
# CSC221 M3Pro - Recipes
# Harley Coughlin

from recipe import DessertRecipe, MainCourseRecipe
from etl import extract_recipes, get_recipe_instances
import menu


def main():

    recipes = None
    file_name = "recipe_data.xlsx"
    try:
        recipes = extract_recipes(file_name)
    except FileNotFoundError:
        print(f"""{file_name} not found in current directory, please ensure the
        file exists and has the correct name""")

    recipes = get_recipe_instances(recipes)

    choice = 0
    while choice != 4:
        menu.print_main_menu()
        choice = menu.get_menu_choice(4)

        if choice == 1:
            for recipe in recipes:
                recipe.display_recipe()

        elif choice == 2:
            recipe_name = menu.get_recipe_name()

            found = False
            for recipe in recipes:
                if recipe.get_name() == recipe_name:
                    found = True
                    recipe.display_recipe()

            if not found:
                print(f"Couldn't find {recipe_name} in the recipes. The recipe "
                      "may not exist or is misspelled.\n")

        elif choice == 3:
            dessert = 1
            main_course = 2
            menu.print_filter_menu()
            filter_by = menu.get_menu_choice(3)

            if filter_by == dessert:
                [recipe.display_recipe() for recipe in recipes if isinstance(recipe, DessertRecipe)]
            elif filter_by == main_course:
                [recipe.display_recipe() for recipe in recipes if isinstance(recipe, MainCourseRecipe)]
            else:
                [recipe.display_recipe() for recipe in recipes if recipe.is_vegetarian()]

        elif choice == 4:
            print("Thanks for using the program.\n")


if __name__ == "__main__":
    main()
