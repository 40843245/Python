#list_show.py
#eg show that l1=l2 means l1 points to l2
#i.e. l1 and l2 points at the same place
#wanna understand how to copy , see list_copy,py
list1=["jay","is","handsome"]
backup=list1
print(list1)
print(backup)
list1[2]="shoot"
print(list1)
print(backup)
list1=list(backup)
print(list1)
print(backup)