from functools import reduce
def prod(x,y):
    return x*y
print(reduce(prod, [4,5,6]))