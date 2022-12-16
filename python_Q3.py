L = [1]
x = 1
def f():
    L.append(2)
    return L

def g():
    x += 2
    return x

print(f())
print(g())

#ans:
"""
[1, 2]
UnboundLocalError:
local variable 'x' referenced before assignment
"""
#sol:
#when you use '=' sign which means to declare the var and assign the value to the var
#... , but youn cannot assign the value before declaration and you can not assign the global var in function.