"""Recipe class and subclasses."""


class Recipe:
    def __init__(self, name, ingredients, steps,
                 is_vegetarian):
        """Recipe class constructor.

        Params
        ------
        name: str
            Name of the recipe.
        ingredients: list[str]
            List of ingredients for the recipe.
        steps: list[str]
            Ordered list of steps to create the recipe.
        is_vegetarian: bool
            True if the recipe is a vegetarian recipe.
        """
        self.__name = name
        self.__ingredients = ingredients
        self.__steps = steps
        self.__is_vegetarian = is_vegetarian


    def get_name(self):
        """Returns the name of the recipe."""
        return self.__name


    def get_ingredients(self):
        """Returns the list ingredients of the recipe."""
        return self.__ingredients


    def get_steps(self):
        """Returns the list of steps in order."""
        return self.__steps


    def is_vegetarian(self):
        """Returns whether the recipe is vegetarian or not."""
        return self.__is_vegetarian


    def set_name(self, name):
        """Sets the name of the recipe."""
        self.__name = name

    
    def set_ingredients(self, ingredients):
        """Sets the list of ingredients for the recipe."""
        self.__ingredients = ingredients


    def set_steps(self, steps):
        """Sets the steps for the recipe."""
        self.__steps = steps


    def set_vegetarian(self, is_vegetarian):
        """Sets whether the recipe is vegetarian or not."""
        self.__is_vegetarian = is_vegetarian


    def display_recipe(self):
        """Prints formatted recipe."""
        print(f"{self.__name: ^40}")
        print(f"{'':-^40}")
        print("Ingredients:")
        for ingredient in self.__ingredients:
            print(f"- {ingredient}")
        print()
        for count, step in enumerate(self.__steps):
            print(f"Step #{count + 1}")
            print(f"{'': >4}{step}")


class DessertRecipe(Recipe):
    def __init__(self, name, ingredients, steps, is_vegetarian, sweetness_level):
        Recipe.__init__(self, name, ingredients, steps, is_vegetarian)
        self.__sweetness_level = sweetness_level


    def get_sweetness_level(self):
        """Returns the sweetness level."""
        return self.__sweetness_level


    def set_sweetness_level(self, sweetness_level):
        """Sets the sweetness level."""
        self.__sweetness_level = sweetness_level


    def display_recipe(self):
        """Prints formatted recipe."""
        print(f"{self.get_name(): ^40}")
        print(f"{'':-^40}")
        print(f"Sweetness: {self.__sweetness_level}")
        print("Ingredients:")
        for ingredient in self.get_ingredients():
            print(f"- {ingredient}")
        print()
        for count, step in enumerate(self.get_steps()):
            print(f"Step #{count + 1}")
            print(f"{'': >4}{step}")


class MainCourseRecipe(Recipe):
    def __init__(self, name, ingredients, steps, is_vegetarian, spice_level):
        Recipe.__init__(self, name, ingredients, steps, is_vegetarian)
        self.__spice_level = spice_level


    def get_spice_level(self):
        """Returns the spice level."""
        return self.__spice_level


    def set_spice_level(self, spice_level):
        """Sets the spice level."""
        self.__spice_level = spice_level


    def display_recipe(self):
        """Prints formatted recipe."""
        print(f"{self.get_name(): ^40}")
        print(f"{'':-^40}")
        print(f"Spice: {self.__spice_level}")
        print("Ingredients:")
        for ingredient in self.get_ingredients():
            print(f"- {ingredient}")
        print()
        for count, step in enumerate(self.get_steps()):
            print(f"Step #{count + 1}")
            print(f"{'': >4}{step}")
