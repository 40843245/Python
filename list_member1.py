#list_member1.py
#member:
#len()
#type()
#append()
#index()
#count()
#reverse()
#pop()
#remove()

#operator:
#+

##more details on list_member2.py
list1=["jay","is","handsome"]
backup=list1
print(list1)
print("len of list1 is",len(list1))
print("type of list1 is",type(list1))
list1.append(".")
list1.append(",isn't it?")
print(list1)
idx=list1.index("jay")
print("jay is at %d index." %(idx))
#idx=list1.index("ugly")#ValueError: 'ugly' is not in list
if "ugly" in list1:
    print("ugly is at %d index." %(list1.index("ugly")))
else:
    print("ugly is not in list1")
list2=list1+list1
print("duplicate of list1 is",list2)
list2=list1*2
print("duplicate of list1 is",list2)

print("list 1 hve jay word %d times." %(list1.count("jay")))

list1.reverse()
print("list1 after reversing is ",list1)

sth=list1.pop(list1.index("jay"))
print(list1)
##pop(int)
last_sth=list1.pop()
print(list1)
##remove(obj) obj is in list1
list1.remove(".")
print(list1)