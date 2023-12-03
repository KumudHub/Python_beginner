# now we  are going to create new class persons which will be owning the robot made earlier

class person:
    def __init__(self,n,p,i):
        self.name = n
        self.personality = p
        self.is_sitting = i

    def is_down(self):
        is_sitting = True
    
    def is_standup(self):
        is_sitting = False

        # now we will objectify the person as p1 and p2

p1 = person("Alice" ,"Agresive",False)
p2 = person("Berkley","Talkative",True)
        


# the same class made in the last lesson "robot"
class Robot:
    def __init__(self,name,color,weight):  # this is the constructor
        self.name = name
        self.color = color
        self.weight = weight

    def introduceself(self):
        print("My name is " + self.name)



r1 = Robot("Tom","Red",30)
r2 = Robot("Jerry","Blue",40)


  # now we will add an attrribute of owning the robot to the respective persons

p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduceself()
p2.robot_owned.introduceself()
