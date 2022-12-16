#ex8-1-1.py
#class_inherit.py

#eg show that how a class was inherited by other class 
#class Animal inherits nothing , i.e. it did not inherit
class Animal():
    def __init__(self,name):
        self.name=name
    def sound():
        return None
#class Dog inherits the class Animal
class Dog(Animal):
    def __init__(self,name,leg):
        super().__init__('dog '+name)
        self.leg=leg
    #overriding , func sound of class animal 
    def sound(self):
        return "bark"
    def attack(self):
        #pay attention to the order of output
        print("hello nothing")
        return ("bites sb")
a=Animal('jerry')
d=Dog('jelly',4)
print("I have an animal named:",a.name)
print("I have an dog named:",d.name)
print("my dog can ", d.sound())
print("my dog also can ",d.attack(),"named steff")