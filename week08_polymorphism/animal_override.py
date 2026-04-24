class Animal_rda:
    def speak_rda(self_rda):
        print("Animal makes a sound")

class Dog_rda(Animal_rda):
    def speak_rda(self_rda):
        print("Dog barks")

class Cat_rda(Animal_rda):
    def speak_rda(self_rda):
        print("Cat meows")

animals_rda = [Dog_rda(), Cat_rda()]
for animal_rda in animals_rda:
    animal_rda.speak_rda()