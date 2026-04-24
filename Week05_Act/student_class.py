class Student_rda:
    def __init__(self_rda, name_rda, student_id_rda, course_rda):
        self_rda.name_rda = name_rda
        self_rda.student_id_rda = student_id_rda
        self_rda.course_rda = course_rda
    
    def display_student_rda(self_rda):
        print("Name:", self_rda.name_rda)
        print("Student ID:", self_rda.student_id_rda)
        print("Course:", self_rda.course_rda)

student1_rda = Student_rda("Maria", "2023-001", "BSIS")
student1_rda.display_student_rda()
