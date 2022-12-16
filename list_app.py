#list_type.py
#self prc:how to translate 2D array into 1D  regular  array
#for eg:
#input :['jay', 'is', 'handsome', ['curry', 'is', 'nba', 'basketball', 'player'], ['hello', 'python'], ['I', 'like', 'to', 'play', 'basketball']]
#output:['jay', 'is', 'handsome', ['hello', 'python'], 'curry', 'is', 'nba', 'basketball', 'player', 'I', 'like', 'to', 'play', 'basketball']

#preprocess
list1=["jay","is","handsome"]
list2=["curry","is","nba","basketball","player"]
list3=["hello","python"]
list4=["I","like","to","play","basketball"]
print(list1)
print(list2)
print(list3)
print(list4)

list1.append(list2)#list2 was not changed
list1.append(list3)
list1.append(list4)
print(list1)

#meth 1:
#by splitting the inner list , then extend the inner list into the main list
"""
#wrong ans
cnt=0
for i in list1:
    if type(i) is type(list2):
        print(cnt)
        print(i)
        list_tmp=i
        list1.remove(i)
        print(list1)
        list1.extend(i)
        print(list1)
    cnt+=1
#ans:
print(list1)
"""

#wrong ans
cnt=0
for i in list1:
    if type(i) is type(list2):
        print(cnt)
        print(i)
        list_tmp=i
        list1.remove(i)
        print(list1)
        for j in i:
            list1.insert(cnt,j)
        print(list1)
    cnt+=1
#ans:
print("the final ans is:")
print(list1)