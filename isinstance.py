#isinstance.py

print(isinstance(2,int))
print(isinstance(2,str))
print(isinstance(True,bool))
print(isinstance(0,bool))
print(isinstance(None,bool))

class myObj:
  name = "John"
class myObj2:
  name='josh'
y = myObj()
print(isinstance(y, myObj))
print(isinstance(y,myObj2))