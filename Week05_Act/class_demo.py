class Person_rda:
    def __init__(self_rda, name_rda, age_rda):
        self_rda.name_rda = name_rda
        self_rda.age_rda = age_rda
    
    def display_info_rda(self_rda):
        print("Name:", self_rda.name_rda)
        print("Age:", self_rda.age_rda)

p1_rda = Person_rda("Juan", 20)
p1_rda.display_info_rda()
