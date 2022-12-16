#class_uncess.py
class Animal():
    def __init__(self,name):
        self.__name=name
    def showname(self):
        return self.__name
    
a=Animal("jerry")

#print(a.__name)
print(a.showname())