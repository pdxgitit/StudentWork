# coding: utf-8
​
# In[100]:
​
class Person:
​
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
​
    def full_name(self):
        return self.firstname + " " + self.lastname
​
    def introduce(self):
        print("Hello, my name is {}".format(self.full_name()))
​
​
# In[94]:
​
p = Person("Oliver", "Bradley")
​
​
# In[ ]:
​
​
​
​
# In[71]:
​
p.full_name()
​
​
# In[68]:
​
p.introduce()
​
​
# In[78]:
​
class Employee(Person):
​
    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum
​
    def get_employee(self):
        return self.full_name() + ", " +  str(self.staffnumber)
​
​
# In[79]:
​
e = Employee("Oliver", "Bradley", 101)
​
​
# In[80]:
​
e.get_employee()
​
​
# In[ ]:
​
​
​
​
# In[ ]:
​
​
​
​
# In[84]:
​
class Pet:
​
    def __init__(self, name, species):
        self.name = name
        self.species = species
​
    def getName(self):
        return self.name
​
    def getSpecies(self):
        return self.species
​
    def __str__(self):
        return "{} is a {}".format(self.name, self.species)
​
​
# In[85]:
​
dog = Pet("Fido", "canine")
​
print(dog)
# In[86]:
​
print(dog)
​
​
# In[ ]:
​
​
​
​
# In[87]:
​
# subclass of the class Pet
class Dog(Pet):
​
    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats
​
    def chasesCats(self):
        return self.chases_cats
​
​
# In[88]:
​
fido = Dog("Fido", True)
​
​
# In[89]:
​
print(fido)
​
​
# In[90]:
​
fido.species
​
​
#
​
# In[91]:
​
fido.name
​
​
# In[92]:
​
fido.chasesCats()
​
​
# In[ ]:
​
