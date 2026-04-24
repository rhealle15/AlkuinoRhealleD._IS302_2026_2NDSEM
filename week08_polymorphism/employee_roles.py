class Employee_rda:
    def work_rda(self_rda):
        print("Employee performs tasks")

class Programmer_rda(Employee_rda):
    def work_rda(self_rda):
        print("Programmer writes code")

class Designer_rda(Employee_rda):
    def work_rda(self_rda):
        print("Designer creates UI designs")

employees_rda = [Programmer_rda(), Designer_rda()]
for emp_rda in employees_rda:
    emp_rda.work_rda()