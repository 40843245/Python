#class_polymorphism.py
class Dog():
    def __init__(self,name):
        self._name=name
    def showname(self):
        return self._name
    def sound(self):
        return "bark"
class Cat():
    def __init__(self,name):
        self._name=name
    def showname(self):
        return self._name
    def sound(self):
        return "mow"
class Bird():
    def __init__(self,name):
        self._name=name
    def showname(self):
        return self._name
    def sound(self):
        return "chirp"
#morphism
def talk(obj):
    print(obj.showname(),"is ",obj.sound()+"ing.")

b=Bird("bi")
d=Dog("di")
c=Cat("ci")

talk(b)
talk(c)
talk(d)