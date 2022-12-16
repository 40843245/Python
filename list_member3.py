list1=["jay","is","handsome"]
list2=["curry","is","nba","basketball","player"]

list1.extend(list2)#list2 was not changed 
print(list1)#output:['jay', 'is', 'handsome', ['curry', 'is', 'nba', 'basketball', 'player']]
print(list2)#output:['curry', 'is', 'nba', 'basketball', 'player']