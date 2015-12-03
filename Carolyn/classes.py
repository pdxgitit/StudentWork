class Puppy:

    def __init__(self, name, breed, activity):
        self.name = name
        self.breed = breed
        self.activity = activity

    def get_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def get_activity(self):
        return self.activity

    def __str__(self):
        return "{} is a {} who likes to {}.".format(self.name, self.breed, self.activity)


dog = Puppy("Doug", "mutt", "play frisbee")
puppy = Puppy("Adelaide", "Cockerdoodle", "hop")
print(dog)
print(puppy)

class Pet(Puppy):

    def __init__()
