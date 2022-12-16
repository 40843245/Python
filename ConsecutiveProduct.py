#ConsecutiveProduct.py
# Consecutive Product list
def ConsecutiveProduct(test):
    print ("The original list is : " + str(test))
    res = [test[i] * test[i + 1] for i in range(len(test)-1)]
    print ("The computed successive product list is : " + str(res))
    res = [i * j for i, j in zip(test[: -1], test[1 :])]
    print ("The computed successive product list is : " + str(res))    
test = [1, 4, 5, 3, 6]
ConsecutiveProduct(test)

