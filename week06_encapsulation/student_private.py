class Student_rda:
    def __init__(self_rda, name_rda, student_id_rda, gpa_rda):
        self_rda.__name = name_rda
        self_rda.__student_id = student_id_rda
        self_rda.__gpa = gpa_rda

    def get_student_info_rda(self_rda):
        print("Name:", self_rda.__name)
        print("Student ID:", self_rda.__student_id)
        print("GPA:", self_rda.__gpa)

student1_rda = Student_rda("Juan", "2023-001", 1.75)
student1_rda.get_student_info_rda()