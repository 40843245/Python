import time
def measureTime(func):
    def inner(*args): 
        tStart = time.time() #計時開始
        res = func(*args)
        tEnd = time.time() #計時結束
        print(f"{func.__name__} runs {(tEnd - tStart):.4f}秒")
        return res
    return inner

@measureTime
def isPrime_V1(n):
    return n>=2 and len([i for i in range(1,int(n**0.5)+1) if n%i==0])==1

@measureTime
def isPrime_V2(n):
    return n>=2 and not any(n%i==0 for i in range(2,int(n**0.5+1)))

@measureTime
def isPrime_V3(n):
    return n==2 or (n > 2 and n%2 and all(n%x for x in range(3,int(n**.5)+1,2)))

print(isPrime_V1(2**31-1))
print(isPrime_V2(2**31-1))
print(isPrime_V3(2**31-1))