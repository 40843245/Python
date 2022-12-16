
def pefectShuffle(deck):
    n= len(deck)//2
    first = deck[:n]  #取出前n個數字當做第一副牌
    second = deck[n:] #取出後n個數字當做第二副牌
    nextIsFirst= True  #記錄下一張要發的牌是第一副牌還是第二副
    firstIdx=0        #記錄下一張要發的牌的index
    secondIdx=0       #記錄下一張要發的牌的index
    for i in range(2*n):
        if nextIsFirst:
            deck[i]=first[firstIdx]
            firstIdx+=1
        else:
            deck[i]=second[secondIdx]
            secondIdx+=1
        nextIsFirst= not nextIsFirst
deck=list(range(1,9)) #[1,2,3,4,5,6,7,8]
pefectShuffle(deck)
print(deck)

def pefectShuffle(deck):
    n= len(deck)//2
    deck[::2], deck[1::2]= deck[:n], deck[n:]
    
deck=list(range(1,9)) #[1,2,3,4,5,6,7,8]
pefectShuffle(deck)
print(deck)