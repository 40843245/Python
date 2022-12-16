#list_copy.py
#best eg to show that how to copy a list
#use deepcopy cmd in module <copy>
import copy
list1=[7894198,"frbyt"]
list2=list1
print(list1)
print(list2)
list1.append("rgtehryj")
print(list1)
print(list2)

list3=copy.deepcopy(list1)
list1.append("cat")

print(list1)
print(list3)