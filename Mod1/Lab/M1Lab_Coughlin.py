# This program is a menu driven application for recording and displaying student grades
# 01/14/2025
# CSC221 - Debugging
# Harley Coughlin

import Functions

def print_menu() -> None:
    print("\nStudent Grade Manager")
    print("1. Add Student")
    print("2. Update Grades")
    print("3. Display Results")
    print("4. Display Class Average")
    print("5. Exit")


def get_choice() -> int:
    """Returns an int between 1 and 5."""
    choice = 0
    while choice < 1 or choice > 5:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter an number between 1 and 5")
            continue
    return choice

# Data structure to store student grades
students = {
    "Alice": [85, 90, 88],
    "Bob": [70, 75, 65],
    "Charlie": [50, 45],
    "Diana": [],
}

def main():
    # Initialize choice to 0
    choice = 0

    # Main loop
    while choice != 5:
        print_menu()
        choice = get_choice()

        if choice == 1:
            name = input("Enter student name: ")
            Functions.add_student(students, name)

        elif choice == 2:
            name = input("Enter student name: ")
            grades = Functions.get_grades()
            Functions.update_grades(students, name, grades)

        elif choice == 3:
            Functions.display_results(students)

        elif choice == 4:
            Functions.display_class_average(students)

        elif choice == 5:
            print("Exiting program. Goodbye!")

        # Should actually never reach this since the validation is being done
        # in get_choice function
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
