def calculate_average(grade1_rda, grade2_rda, grade3_rda):
    """Calculate the average of three grades"""
    return (grade1_rda + grade2_rda+ grade3_rda) / 3

def get_remark(average_rda):
    """Return the remark based on the average grade"""
    if average_rda >= 90:
        return "Excellent"
    elif average_rda >= 85:
        return "Very Good"
    elif average_rda >= 80:
        return "Good"
    elif average_rda >= 75:
        return "Fair"
    else:
        return "Failed"

# Main program
print("----- STUDENT GRADE PROCESSOR -----")
student_name_rda = input("Enter student name: ")
grade1_rda = float(input("Enter first grade: "))
grade2_rda = float(input("Enter second grade: "))
grade3_rda = float(input("Enter third grade: "))

# Calculate average and get remark
average_rda = calculate_average(grade1_rda, grade2_rda, grade3_rda)
remark_rda = get_remark(average_rda)

# Display results
print("\n----- RESULTS -----")
print("Student Name:", student_name_rda)
print("Grade 1:", grade1_rda)
print("Grade 2:", grade2_rda)
print("Grade 3:", grade3_rda)
print("Average:", round(average_rda, 2))
print("Remark:", remark_rda)
