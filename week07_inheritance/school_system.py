class Person_rda:
    def __init__(self_rda, name_rda, age_rda):
        self_rda.name_rda = name_rda
        self_rda.age_rda = age_rda

    def display_info_rda(self_rda):
        print("Name:", self_rda.name_rda)
        print("Age:", self_rda.age_rda)

class Student_rda(Person_rda):
    def __init__(self_rda, name_rda, age_rda, course_rda):
        super().__init__(name_rda, age_rda)
        self_rda.course_rda = course_rda

    def display_info_rda(self_rda):
        super().display_info_rda()
        print("Course:", self_rda.course_rda)

class Teacher_rda(Person_rda):
    def __init__(self_rda, name_rda, age_rda, subject_rda):
        super().__init__(name_rda, age_rda)
        self_rda.subject_rda = subject_rda

    def display_info_rda(self_rda):
        super().display_info_rda()
        print("Subject:", self_rda.subject_rda)

# Example usage
student_rda = Student_rda("Maria", 20, "BSIS")
teacher_rda = Teacher_rda("Mr. Smith", 45, "Mathematics")

print("Student Info:")
student_rda.display_info_rda()
print("\nTeacher Info:")
teacher_rda.display_info_rda()