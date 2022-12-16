#static_method.py
#ex8-1-11.py

#illustrate that comparison of staticmethod and classmethod

#classmethod and staticmethod are instance method, they can be used before the object was created.
#In classmethod , every func except __init__ requires 1 argument.
#In staticmethod, every func except __init__ requires 0 argument.
class Say():
    @staticmethod
    def hello():
        print("Hello")
    
    """
    #TypeError: hello() missing 1 required positional argument: 'sm'
    def hello(sm):
        print("Hello")
    """
Say.hello()

class Speak():
    @classmethod
    def hello(cls):
        print("Speak")

Speak.hello()