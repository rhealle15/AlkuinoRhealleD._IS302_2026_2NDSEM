class Person_rda:
    def __init__(self_rda, name_rda, age_rda):
        self_rda.name_rda = name_rda
        self_rda.age_rda = age_rda

class Student_rda(Person_rda):
    def __init__(self_rda, name_rda, age_rda, course_rda):
        super().__init__(name_rda, age_rda)
        self_rda.course_rda = course_rda

    def display_student_rda(self_rda):
        print("Name:", self_rda.name_rda)
        print("Age:", self_rda.age_rda)
        print("Course:", self_rda.course_rda)

student1_rda = Student_rda("Maria", 20, "BSIS")
student1_rda.display_student_rda()