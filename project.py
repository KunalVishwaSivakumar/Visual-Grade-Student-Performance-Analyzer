"""
Kunal Vishwa Sivakumar
Class: CS 521 - Fall 2024
Date: 12/12/2024
Final Term Project
Description of Problem:
This project, 'Visual Grade,' is a Python-based tool for managing and analyzing student records.
It utilizes a Student class to calculate averages, classify grades, and add new entries.
The program includes features like data visualization using Matplotlib for performance insights.
File handling ensures seamless data persistence across sessions.
It showcases the integration of object-oriented programming, user interaction, and advanced data analysis.
"""
import matplotlib.pyplot as plt

# User-defined class for managing students
class Student:
    def __init__(self, name, grades):
        """Initialize the Student with a name and a list of grades"""
        self.__name = name  # Private attribute
        self.grades = grades  # Public attribute

    def __repr__(self):
        """String representation of the Student object"""
        return f"Student(name='{self.__name}', grades={self.grades})"

    def calculate_average(self):
        """Private method to calculate average grade"""
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_grade_level(self):
        """Public method to return grade classification"""
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def add_grade(self, grade):
        """Public method to add a grade to the student"""
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be a number between 0 and 100")


# Function to load students from an input file
def load_students(input_file):
    students = {}
    try:
        with open(input_file, 'r') as file:
            for line in file:
                name, grades = line.strip().split(':')
                grades = [float(g) for g in grades.split(',')] if grades else []
                students[name] = Student(name, grades)
    except FileNotFoundError:
        print(f"Input file {input_file} not found. Starting with an empty list of students.")
    return students


# Function to save students to a file
def save_students_to_file(file_path, students, is_input_format=True):
    with open(file_path, 'w') as file:
        for student_name, student in students.items():
            grades_str = ','.join(map(str, student.grades))
            if is_input_format:
                # Save in input file format
                file.write(f"{student_name}:{grades_str}\n")
            else:
                # Save in output file format
                avg = student.calculate_average()
                grade_level = student.get_grade_level()
                file.write(f"{student_name}: Grades: {grades_str}, Average: {avg:.2f}, Grade Level: {grade_level}\n")


# Function for advanced data analysis (visualization)
def visualize_student_performance(students):
    if not students:
        print("No students available for visualization.")
        return

    names = list(students.keys())
    averages = [student.calculate_average() for student in students.values()]

    # Bar graph for average grades
    plt.figure(figsize=(10, 6))
    plt.bar(names, averages, color='purple')
    plt.xlabel('Students')
    plt.ylabel('Average Grade')
    plt.title('Student Average Grades')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# Function to display all students
def display_students(students):
    if not students:
        print("No students available to display.")
        return

    print("\nStudent Records:")
    for name, student in students.items():
        avg = student.calculate_average()
        grade_level = student.get_grade_level()
        print(f"Name: {name}, Grades: {student.grades}, Average: {avg:.2f}, Grade Level: {grade_level}")


# Main function to interact with the system
def main():
    input_file = "students_input.txt"
    output_file = "students_output.txt"

    # Load students from input file
    students = load_students(input_file)

    while True:
        print("\nOptions: 1) Add Student  2) Add Grade  3) Display Students  4) Visualize Performance  5) Save & Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the student's name: ")
            if name in students:
                print(f"Student {name} already exists.")
            else:
                students[name] = Student(name, [])
                print(f"Student {name} added.")

        elif choice == '2':
            name = input("Enter the student's name: ")
            if name not in students:
                print(f"Student {name} does not exist.")
            else:
                try:
                    grade = float(input("Enter the grade: "))
                    students[name].add_grade(grade)
                    print(f"Grade {grade} added for {name}.")
                except ValueError as ve:
                    print(f"Error: {ve}")

        elif choice == '3':
            display_students(students)

        elif choice == '4':
            visualize_student_performance(students)

        elif choice == '5':
            # Save final changes to both files
            save_students_to_file(input_file, students, is_input_format=True)
            save_students_to_file(output_file, students, is_input_format=False)
            print(f"Data saved to {input_file} and {output_file}. Exiting.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
