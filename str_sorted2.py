s=input()
L=sorted(s,key= lambda x: (x.isdigit() and int(x)%2==0, x.isdigit() and int(x)%2!=0 ,x.isupper() , x.islower() ))
print("".join(L))