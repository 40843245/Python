from itertools import permutation

def tupleToNum(Tuple):
    return int(''.join(map(str,Tuple)))
    
def check(Tuple):
    return tupleToNum(Tuple)*Tuple[2]==tupleToNum(Tuple[2:]+Tuple[:2])
    
for p in permutations(range(1,10),6):
    if check(p):
        print(p)