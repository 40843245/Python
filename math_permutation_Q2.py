from itertools import permutations

def tupleToFloat(Tuple):
    return Tuple[0]/(Tuple[1]*10+Tuple[2])
    
def check(Tuple):
    a = tupleToFloat(Tuple[0:3])
    b = tupleToFloat(Tuple[3:6])
    c = tupleToFloat(Tuple[6:9])
    return abs(a+b+c-1) <= 0.000001 #避免浮點數計算有誤差，只要a+b+c與1是接近的就當做是1
    
for p in permutations(range(1,10),9):
    if check(p):
        print(p)