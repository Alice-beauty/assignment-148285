# Define the Student class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Assignment '{assignment_name}' with grade {grade} added for {self.name}.")

    def display_grades(self):
        print(f"Grades for {self.name} (ID: {self.student_id}):")
        for assignment, grade in self.assignments.items():
            print(f"{assignment}: {grade}")
        if not self.assignments:
            print("No assignments recorded yet.")

# Define the Instructor class
class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Student '{student.name}' (ID: {student.student_id}) added to course '{self.course_name}'.")
        else:
            print(f"Student '{student.name}' is already in the course.")

    def assign_grade(self, student_id, assignment_name, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment_name, grade)
                return
        print(f"Student with ID {student_id} not found in the course '{self.course_name}'.")

    def display_all_students_grades(self):
        print(f"\nGrades for course '{self.course_name}':")
        if not self.students:
            print("No students enrolled yet.")
            return
        for student in self.students:
            student.display_grades()
            print("-" * 20)

# Interactive code for instructors
def main():
    # Create an instructor
    instructor = Instructor("Prof. Smith", "Python Programming 101")

    # Adding students
    student1 = Student("Alice", "S001")
    student2 = Student("Bob", "S002")

    instructor.add_student(student1)
    instructor.add_student(student2)

    # Assign grades to students
    instructor.assign_grade("S001", "Assignment 1", 85)
    instructor.assign_grade("S002", "Assignment 1", 90)
    instructor.assign_grade("S001", "Assignment 2", 88)

    # Display all students' grades
    instructor.display_all_students_grades()

# Run the interactive code
main()
