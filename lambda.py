#ex6-6-1.py
#lambda.py
def mul(x,y):
    return x*y
f=lambda x,y:x*y
a=int(input("enter first numbers:"))
b=int(input("enter second numbers:"))
print("%d * %d = %d." %(a,b,mul(a,b)))
print("%d * %d = %d." %(a,b,f(a,b)))

def run(func,x,y):
    return func(x,y)
ret=run(f,10,20)
print("10 * 20 = %d " %(ret))