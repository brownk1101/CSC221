'''This module contains functions for interacting with student data'''

def calculate_average(grades: list[int]) -> float:
    # Calculate the average of grades
    # Handles 0 length grades by just returning a 0
    total = 0.0
    if len(grades) > 0:
        for grade in grades:
            total += grade
        average = total / len(grades)
    else:
        average = 0

    return average

def determine_status(average: float, threshold: int = 50) -> str:
    # Determine if the student passed or failed
    if average >= threshold:
        status = "Pass"
    else:
        status = "Fail"

    return status

def add_student(students: dict[str, list[int]], name: str) -> None:
    # Convert all names to lower-case for comparison
    if name.lower() in [student.lower() for student in students.keys()]:
        print("Error: Student already exists.")
    else:
        students[name] = []
        print(f"Student {name} added successfully!")

def update_grades(students: dict[str, list[int]], name: str, grades: list[int]) -> None:
    # Convert all names to lower-case for comparison
    if name.lower() not in [student.lower() for student in students.keys()]:
        print("Error: Student not found.")
    else:
        # Grades are validated on input
        students[name] = grades
        print(f"Grades for {name} updated successfully!")

def get_grades() -> list[int]:
    grades: list[int] = []
    user_input = input("Enter grades as comma-separated values: ").split(",")
    for grade in user_input:
        try:
            grade = int(grade)
            if grade < 0 or grade > 100:
                raise RuntimeError
            grades.append(grade)
        except ValueError:
            print(f'{grade} cannot be converted to an int. Skipping.')
            continue
        except RuntimeError:
            print(f'{grade} cannot be less than 0 or greater than 100. Skipping.')

    return grades

def display_results(students: dict[str, list[int]]) -> None:
    for name, grades in students.items():
        average = calculate_average(grades)
        status = determine_status(average)
        print(f"Student: {name}, Average: {average:.2f}, Status: {status}")

def display_class_average(students: dict[str, list[int]]) -> None:
    total_sum = 0
    total_count = 0

    for grades in students.values():
        # Students should all have grades but if they don't, don't process them
        if grades:
            total_sum += sum(grades)
            total_count += len(grades)

    # Avoid division by zero
    if total_count > 0:
        class_average = total_sum / total_count
        print(f"Class Average: {class_average:.2f}")
    else:
        print("No grades available to calculate class average.")
