
#List Comprehensions (列表生成式)
#ans for prc

def soldier(m,n):
    l=[ x for x in range(m,n) if (x%(3*5*7)==23)]
    if(len(l)==0):
        return "no soldier."
    else:
        return l

if __name__=='__main__':
    print(soldier(2,24))
    print(soldier(2,23))
    print(soldier(2,129))
    print(soldier(128,224))
    print(soldier(2,128))