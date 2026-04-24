class Employee_rda:
    def __init__(self_rda, name_rda, salary_rda):
        self_rda.name_rda = name_rda
        self_rda.salary_rda = salary_rda

class Manager_rda(Employee_rda):
    def __init__(self_rda, name_rda, salary_rda, department_rda):
        super().__init__(name_rda, salary_rda)
        self_rda.department_rda = department_rda

    def display_manager_rda(self_rda):
        print("Name:", self_rda.name_rda)
        print("Salary:", self_rda.salary_rda)
        print("Department:", self_rda.department_rda)

manager1_rda = Manager_rda("John", 50000, "IT")
manager1_rda.display_manager_rda()