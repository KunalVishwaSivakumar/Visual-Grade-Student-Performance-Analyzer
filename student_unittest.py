import unittest

from Project.project import Student


class TestStudentMethods(unittest.TestCase):

    # Test for calculate_average() method
    def test_calculate_average(self):
        student = Student("Alice", [90, 80, 85])
        self.assertEqual(student.calculate_average(), 85.0, "The average grade should be 85.0")

        student_empty = Student("Bob", [])
        self.assertEqual(student_empty.calculate_average(), 0,
                         "The average grade should be 0 when no grades are provided")

    # Test for get_grade_level() method
    def test_get_grade_level(self):
        student_A = Student("Alice", [95, 90, 92])
        self.assertEqual(student_A.get_grade_level(), "A", "The grade level should be 'A'")

        student_B = Student("Bob", [85, 80, 88])
        self.assertEqual(student_B.get_grade_level(), "B", "The grade level should be 'B'")

        student_F = Student("Charlie", [50, 45, 60])
        self.assertEqual(student_F.get_grade_level(), "F", "The grade level should be 'F'")

    # Test for add_grade() method
    def test_add_grade(self):
        student = Student("Alice", [90, 85])
        student.add_grade(95)
        self.assertIn(95, student.grades, "Grade 95 should be added to the student's grade list")

        # Test invalid grade
        try:
            student.add_grade(110)  # Invalid grade, should raise an error
        except ValueError:
            pass  # Expected error
        else:
            self.fail("ValueError not raised for invalid grade")

        try:
            student.add_grade(-10)  # Invalid grade, should raise an error
        except ValueError:
            pass  # Expected error
        else:
            self.fail("ValueError not raised for invalid grade")

    # Test for __repr__() method
    def test_repr(self):
        student = Student("Alice", [90, 80, 85])
        self.assertEqual(repr(student), "Student(name='Alice', grades=[90, 80, 85])",
                         "The repr() should match the expected format")


if __name__ == "__main__":
    unittest.main()
