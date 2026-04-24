class Animal_rda:
    def __init__(self_rda, name_rda):
        self_rda.name_rda = name_rda

    def speak(self_rda):
        print(self_rda.name_rda, "makes a sound")

class Dog_rda(Animal_rda):
    def bark(self_rda):
        print(self_rda.name_rda, "barks")

dog1_rda = Dog_rda("Buddy")
dog1_rda.speak()
dog1_rda.bark()