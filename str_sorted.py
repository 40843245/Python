

s = input()
L = sorted(s, key= lambda x: (int(x)%2==0, int(x)))
print(''.join(L))