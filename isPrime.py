def isPrime(n):
    return n>=2 and not any(n%i==0 for i in range(2,int(n**0.5)+1))
#driver code
list1=[i for i in range(1,115)]
for l in list1:
    print(l,"is",'a prime' if isPrime(l) else 'not a prime')