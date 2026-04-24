class Employee_rda:
    def __init__(self_rda, name_rda):
        self_rda.__name = name_rda
        self_rda.__salary = 0

    def set_salary_rda(self_rda, salary_rda):
        if salary_rda > 0:
            self_rda.__salary = salary_rda

    def get_salary_rda(self_rda):
        return self_rda.__salary

emp_rda = Employee_rda("Ana")
emp_rda.set_salary_rda(30000)
print("Salary:", emp_rda.get_salary_rda())