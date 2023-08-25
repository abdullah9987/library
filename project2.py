class Student:
    def __init__(self, student_id, name, courses=[]):
        self.student_id = student_id
        self.name = name
        self.courses = courses

    def enroll_course(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"Student ID: {self.student_id}\nName: {self.name}\nCourses: {', '.join(self.courses)}\n"



class Course:
    def __init__(self, course_id, name, instructor):
        self.course_id = course_id
        self.name = name
        self.instructor = instructor

    def __str__(self):
        return f"Course ID: {self.course_id}\nName: {self.name}\nInstructor: {self.instructor}\n"


class College:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def list_students(self):
        for student in self.students:
            print(student)

    def list_courses(self):
        for course in self.courses:
            print(course)


def main():
    college = College()

    while True:
        print("\nCollege Management System")
        print("1. Add Student")
        print("2. Add Course")
        print("3. List Students")
        print("4. List Courses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            student = Student(student_id, name)
            college.add_student(student)
            print("Student added successfully.")
        elif choice == "2":
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            instructor = input("Enter instructor name: ")
            course = Course(course_id, name, instructor)
            college.add_course(course)
            print("Course added successfully.")
        elif choice == "3":
            college.list_students()
        elif choice == "4":
            college.list_courses()
        elif choice == "5":
            print("Exiting the College Management System.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()