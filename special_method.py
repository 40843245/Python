#special_method.py
#ALU

#comparison
#'__eq__' = '=='
#'__ne__' = '!='
#'__gt__' = '>'
#'__ge__' = '>='
#'__lt__' = '<'
#'__le__' = ',='

#operation
#'__add__' = '+'
#'__sub__' = '-'
#'__mul__' = '*'
#'__truediv__' = '/'
#'__floordiv__' = '//'
#'__mod__' = '%'
#'__pow__' = '**'
#'__lshift__' = '<<'
#'__rshit__' = '>>'
#'__and__' = '&'
#'__or__' = '|'
#'__xor__' = '^'

class Animal():
    def __init__(self,name):
        self.__name=name
    def showname(self):
        return self.__name
    def __eq__(self,other):
        return self.showname()==other.showname()
    def eq(self,other):
        return self.showname()==other.showname()
k=Animal("Kelly")
j=Animal("Jerry")
print(k.__eq__(j))
print(k==j) 
        