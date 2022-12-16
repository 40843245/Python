def isPrime(n):
    """
    函數功能: 判斷一個整數是不是質數
    example:
    >>> isPrime(0)
    False
    >>> isPrime(1)
    False
    >>> isPrime(2)
    True
    >>> isPrime(97)
    True
    >>> isPrime(121)
    False
    >>> isPrime(121)
    True
    """
    return n==2 or (n > 2 and n%2 and all(n%x for x in range(3,int(n**.5)+1,2)))
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
