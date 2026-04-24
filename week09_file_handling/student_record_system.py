name_rda = input("Enter student name: ")
course_rda = input("Enter course: ")
with open("students.txt", "a") as file_rda:
    file_rda.write(name_rda + "," + course_rda + "\n")

print("\nStudent Records")
with open("students.txt", "r") as file_rda:
    for line_rda in file_rda:
        print(line_rda.strip())
