# we will go through the concept of constructor in a class

class Robot:
    def __init__(self,name,color,weight):  # this is the constructor
        self.name = name
        self.color = color
        self.weight = weight

    def introduceself(self):
        print("My name is " + self.name)

# now this constructor will make it easier to define the objects attributes

r1 = Robot("Tom","Red",30)
r2 = Robot("Jerry","Blue",40)

r1.introduceself()