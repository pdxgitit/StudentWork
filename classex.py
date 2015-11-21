#Practicing making classes

class Animal(object):

    def __init__(self, species, diet, preditor_status, strength, smart):
        self.species = species
        self.diet = diet
        self.preditor_status = preditor_status
        self.strength = strength
        self.smart = smart

cat = Animal("cat", "cat food", "preditor", 50, 80)

dog = Animal("dog", "dog food", "preditor", 45, 40)

mouse = Animal("mouse", "seeds", "prey", 10, 90)

carp = Animal("fish", "fish food", "prey", 2, 20)

class Pet(Animal):

    
