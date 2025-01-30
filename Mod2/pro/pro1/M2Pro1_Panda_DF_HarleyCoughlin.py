# This a menu driven program using DataFrames, exception handling, functions, and file processing
# 01/29/2025
# CSC221 M2Pro1-Panda DF
# Harley Coughlin

import menu

def main():
    choice: int = 0
    while choice != 8:
        menu.print_menu()
        choice = menu.get_menu_choice()


if __name__ == "__main__":
    main()
