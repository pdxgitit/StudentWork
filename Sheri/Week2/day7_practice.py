#Classes!
class Dog:

    kind = "canine" #ask "does this variable make sense for everything in this class to have?"
#    tricks = [] #mistaken use of a class variable - don't do this! we don't want every instance of dog to have the same tricks!


    def __init__(self, name):
        self.name = name

    def add_trick(self, trick): #This is how tricks should be instanciated
        self.tricks.append(trick)

d = Dog('Cujo')
d.add_trick('sit')
