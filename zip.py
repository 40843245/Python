#zip.py
t1 = ("John", "Charles", "Mike")
t2 = ("Jenny", "Christy", "Monica", "Vicky")
tz = zip(t1, t2)
l1=[1,2,3]
l2=[4,5,6]
lz=zip(l1,l2)

#use the tuple() function to display a readable version of the result:
print(tuple(tz))
tunz1=zip(*tuple(tz))
print(tunz1)
tunz3=tuple(tunz1)
print(tunz3)
print(tz)

print(list(lz))
print(list(zip(* list(lz))))
print(lz)

lz=list(lz)
lunz1,lunz2,lunz3=zip(*lz)
print(lunz1)
print(lunz2)