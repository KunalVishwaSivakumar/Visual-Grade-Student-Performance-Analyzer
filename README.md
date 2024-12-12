---
title: 'Visual Grade: Student Performance Analyzer'
author: "Kunal Vishwa Sivakumar"
date: "2024-12-11"
output: html_document
---
Visual Grade: Student Performance Analyzer

### Project Overview

Visual Grade: Student Performance Analyzer is a Python-based application designed to manage and analyze student performance. 
The application allows users to input student names and their corresponding grades, calculate average grades, determine letter grades (A, B, C, D, F), and generate a visual representation of student performance. 
The program stores student data in a text file (students_input.txt) and outputs the results, including the calculated letter grades, in another text file (students_output.txt).

Additionally, unit tests are included to ensure the proper functioning of the Student class methods.

### Features
Student Management: Add, modify, and manage students and their grades.

Grade Calculation: Calculate average grades and assign letter grades based on predefined thresholds.

Visualization: Generate a bar chart to visually represent each student's average grade.

Data Storage: Save student data and performance analysis results to text files for future use.

Unit Testing: Validate the functionality of the Student class with automated unit tests.

### Prerequisites
Python: Version 3.6 or later.

Libraries: Install the required libraries using the following command:

```
pip install matplotlib
```
### Project Structure
visual_grade/


├── project.py            # Main program file for managing student grades and performance

├── student_unittest.py   # Unit tests for the Student class

├── students_input.txt    # Input file for storing student data

├── students_output.txt   # Output file displaying grade analysis

└── README.md             # Project documentation

### Execution Instructions
Ensure Python is installed on your system.

Open a terminal or command prompt.

Navigate to the project folder:
```
cd "#File Directory"
```

Run the main program by executing:
```
python project.py
```

Running Unit Tests
To verify the correctness of the Student class methods, you can run the unit tests provided in student_unittest.py:

Open a terminal or command prompt.
Navigate to the project folder.

Run the following command to execute the tests:
```
python student_unittest.py
```

If all tests pass, you will see the following output:
```
Ran 4 tests in 0.016s
OK
```

### Conclusion

The Visual Grade: Student Performance Analyzer program is an easy-to-use tool for managing and analyzing student grades. It can be customized for various educational environments, and the visual output provides valuable insights into student performance. The unit tests ensure that the core functionality works correctly, making the program reliable and robust.

