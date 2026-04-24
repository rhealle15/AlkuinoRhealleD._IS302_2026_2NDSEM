class Person_rda:
    def __init__(self_rda, name_rda, age_rda):
        self_rda.__name = name_rda
        self_rda.__age = age_rda

    def get_name_rda(self_rda):
        return self_rda.__name

    def get_age_rda(self_rda):
        return self_rda.__age

p1_rda = Person_rda("Maria", 20)
print("Name:", p1_rda.get_name_rda())
print("Age:", p1_rda.get_age_rda())