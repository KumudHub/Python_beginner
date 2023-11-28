# we will just go through the concept of classes and objects
class robot:
    def introduceself(self):
        print("My name is " + self.name)


r1 = robot()
r1.name  = "Tom"
r1.color = "Red"
r1.weight = 30


r2 = robot()
r2.name = "Jerry"
r2.color = "blue"
r2.weight = 40


r1.introduceself()
r2.introduceself()