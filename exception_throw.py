#exception_throw.py

n=int(input("enter a number:"))
assert (n%2==0)," n must be divided by 2"

try:
    if n==0:
        raise my_error("n must be not equal to 0.")
except my_error:
    print(my_error)
    
    
