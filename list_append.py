#list_append.py
#eg show that
#how to add an element at back
#list2 will be considered into an element

##P.S:
##append(list2) is not equivalent to extend(list2)
list1=["jay","is","handsome"]
list2=["curry","is","nba","basketball","player"]

list1.append(list2)#list2 was not changed 
print(list1)#output:['jay', 'is', 'handsome', ['curry', 'is', 'nba', 'basketball', 'player']]
print(list2)#output:['curry', 'is', 'nba', 'basketball', 'player']
