#check_ans.py

#check how many ans is wrong.

#way 1:
def check(answer,wenwen):
    n=0
    for i in range(len(answer)):
        if(answer[i]!=wenwen[i]):
            n+=1
    return n
#driver code
print("way1")
answer = ['A', 'B', 'B', 'E', 'D', 'C']
wenwen = ['B', 'B', 'B', 'E', 'A', 'C']
print(check(answer,wenwen))

#way 2:
def check(answer,wenwen):
  l=([1 for i in range(len(answer)) if answer[i]!=wenwen[i]])
  return len(l)
#driver code
print("way2")
answer = ['A', 'B', 'B', 'E', 'D', 'C']
wenwen = ['B', 'B', 'B', 'E', 'A', 'C']
print(check(answer,wenwen))
#way 3:
def check(answer, wenwen):
    return len([1 for x, y in zip(answer, wenwen) if x != y])

#driver code
print("way3")
answer = ['A', 'B', 'B', 'E', 'D', 'C']
wenwen = ['B', 'B', 'B', 'E', 'A', 'C']
print(check(answer,wenwen))