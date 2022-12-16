from itertools import permutations

# 將元組轉整數，例如(1,2,3)-> 123
def tToN(Tuple):
    return int(''.join(map(str,Tuple)))
    
def check(Tuple):
    FORTY = tToN(Tuple[:5])
    TEN = tToN(Tuple[3:4]+Tuple[5:7])
    SIXTY = tToN(Tuple[-3:]+Tuple[3:5])
    return FORTY+TEN+TEN == SIXTY
    
for p in permutations(range(0,10),10):
    if check(p):
        FORTY = tToN(p[:5])
        TEN = tToN(p[3:4]+p[5:7])
        SIXTY = tToN(p[-3:]+p[3:5])
        print(f"{FORTY} + {TEN} + {TEN} = {SIXTY}")