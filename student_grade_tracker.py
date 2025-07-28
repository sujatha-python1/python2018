def calculate_grade(score):
    """Assigns a letter grade based on a numerical score."""
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

def student_grade_tracker():
    """Tracks student grades and provides basic analysis."""
    students = {} # Dictionary to store student names and their grades

    while True:
        print("\nStudent Grade Tracker Menu:")
        print("1. Add Student and Grades")
        print("2. View Student Grades")
        print("3. Calculate Average Grade for a Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            grades_str = input("Enter grades (comma-separated, e.g., 85,92,78): ")
            try:
                grades = [float(g.strip()) for g in grades_str.split(',')]
                students[name] = grades
                print(f"Grades for {name} added successfully.")
            except ValueError:
                print("Invalid grade input. Please enter numbers.")

        elif choice == '2':
            if not students:
                print("No students added yet.")
            else:
                print("\n--- Student Grades ---")
                for name, grades in students.items():
                    print(f"Student: {name}, Grades: {grades}")

        elif choice == '3':
            name = input("Enter student name to calculate average: ")
            if name in students:
                grades = students[name]
                if grades:
                    average = sum(grades) / len(grades)
                    grade_letter = calculate_grade(average)
                    print(f"Average grade for {name}: {average:.2f} (Grade: {grade_letter})")
                else:
                    print(f"No grades entered for {name}.")
            else:
                print(f"Student {name} not found.")

        elif choice == '4':
            print("Exiting Student Grade Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    student_grade_tracker()