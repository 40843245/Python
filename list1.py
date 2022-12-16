#list2.pyttt
list1=['3','5',"wer",2,8,5]

#list1 [x:y:z]
#x:starter . default is 0
#y:destination . default is at end
#z: how many steps . default is 1

#P.S.
#element [x,y) i.e. including x , not including y

#if x is greater than or equal to len(list1), error will ocurred.
#value error: out of range will be raised

#if x is less than 0 , it will count counterclockwise (let be cnt)
#and then cnt will assigned to x , finally starting get elements

#print all elements of list
print(list1)

print("type [x:y]")
print(list1[2:4])
print(list1[2:6])
print(list1[2:7])
print(list1[-5:5])#same as [1:5]
print(list1[-3:7])#same as [3:6] output:[2,8,5]
print(list1[-3:-2])#same as [3:4] output:[2]

print(list1[5:5])#output:[]
print(list1[0:0])#output:[]

#because x(5) is larger than y(4) and z is 1
print(list1[5:4])#output:[]
#because x(5) is larger than y(1) and z is 1
print(list1[5:-4])#same as [5:1]

print(list1[-2:-4])
print(list1[8:5])
print(list1[8:-2])

print("type [x]")
print(list1[1])#not same as [1:7]
print(list1[-1])#not same as [6:6] 
#print(list1[8])#IndexError: list index out of range

print("type [x:]")
print(list1[2:])#same as [2:7]

print("type [:y]")
print(list1[:4])#same as [0:4]

print("type [x:y:z]")
print(list1[1:4:1])#same as [1:4]
print(list1[1:4:2])#output:['5',2]
print(list1[2:4:2])#output:['wer']
print(list1[-1:5:-1])#same as [6:5:-1] output:[5]
print(list1[1:-1:-1])#output:[]

print("type [x::z]")
print(list1[2::-1])#same as [2:0:-1] output:['wer','5','3']

#reversely print
print(list1[-1::-1])#same as [6:0:-1] output:[5, 8, 2, 'wer', '5', '3']

print("type [::z]")
print(list1[::1])#same as [0:6]
print(list1[::2])#same as [0:6:2] [0],[2],[4]
#reversely print
print(list1[::-1])#same as [0:6:-1] [5],[4],[3],[2],[1],[0]
print(list1[::-3])#same as [0:6:-3] [5],[2]
print(list1[::-8])#output:[5]

print("type [:y:z]")
print(list1[:3:1])#same as [0:3:1] 
print(list1[:4:2])#same as [0:4:2] 
print(list1[:5:-1])#same as [0:5:-1] output:[]
print(list1[:8:-1])#same as [0:8:-1] output:[]
"""
print("type []")
#print(list1[])# SyntaxError: invalid syntax
"""
#list1: ['3', '5', 'wer', 2, 8, 5]
print("type [:]")
#print all elements
print(list1[:])#same as [0:6]

print("type [::]")
#print all elements
print(list1[::])#same as [0:6]