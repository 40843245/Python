#tuple_list_to_dict.py
#eg:show that how a tuple or a list will be converted to dict
#4 ways
a=["cat","mow"]
b=["dog","bark"]
list1=[[a[0],a[1]],[b[0],b[1]]]
dict1=dict(list1)
print(dict1)
list2=((a[0],a[1]),(b[0],b[1]))
dict2=dict(list2)
print(dict2)
list3=[(a[0],a[1]),(b[0],b[1])]
dict3=dict(list3)
print(dict3)
list4=((a[0],a[1]),(b[0],b[1]))
dict4=dict(list4)
print(dict4)


