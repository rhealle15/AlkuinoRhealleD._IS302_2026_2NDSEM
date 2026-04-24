print("----- GRADE LIST ANALYZER -----")
grades_rda = []

# Ask user to enter 5 grades
for i_rda in range(1, 6):
    grade_rda = float(input(f"Enter grade {i_rda}: "))
    grades_rda.append(grade_rda)

# Compute statistics
average_grade_rda = sum(grades_rda) / len(grades_rda)
highest_grade_rda = max(grades_rda)
lowest_grade_rda = min(grades_rda)

# Display results
print("\n----- RESULTS -----")
print("Grades:", grades_rda)
print("Average Grade:", round(average_grade_rda, 1))
print("Highest Grade:", highest_grade_rda)
print("Lowest Grade:", lowest_grade_rda)
