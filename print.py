#print.py
#basic print and basic operation
a=3
b=5
c=a+b
print("a+b=",c)#a+b= 8
print("a+b=%d",c) #a+b=%d 8
#print("a+b=%d" c)#syntax error
print("the length of (%s) is %d" %('runoob',len('runoob')))#the length of (runoob) is 6
str="a+b=%d" %(c)
print(str)#a+b=8
nHex = 0xFF
print("nHex = %x,nDec = %d,nOct = %o" %(nHex,nHex,nHex))#nHex = ff,nDec = 255,nOct = 377
pi = 3.141592653
#width 10 , float precision 3
print('pi=%10.3f' % pi)#pi=     3.142
# '*' is replaced by '3'
print("pi=%.*f" % (3,pi))#pi=3.142
#fill 0
print('pi=%010.3f' % pi)#pi=000003.142
#show sign
print('pi=%+f' % pi)#+3.141593
#left 
print('pi=%-10.3f' % pi)#pi=3.142

i=2
print(i)
print(i, end=" ")
print(i)
print(i,end="a")
print(i)
"""
output:
2
2 2
2a2
"""

y=3
print("var(y)")