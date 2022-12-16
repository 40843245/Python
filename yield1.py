#ex6-7-1.py
#yield1.py
def my_range(start,stop,step=1):
    if start<stop:
        i=start
        while i<stop:
            yield i
            i+=step
    else:
        i=start
        while i>stop:
            yield i
            i+=step

gen1=my_range(1,2,3)
print(gen1)
print(type(gen1))
for i in gen1:
    print(i)
gen1=my_range(2,11,4)
print(gen1)
print(type(gen1))
for i in gen1:
    print(i)

#next
gen1=my_range(2,11,4)
print("use next to print a generator")
flag=True
while flag:
    try:
        #next(): return current elements and points the next one
        print(next(gen1))
    except StopIteration:
        print("error")
        flag=False
#output will be infite if step==0
#output: 10\n10\n10\n10\n10\n...
gen1=my_range(10,12,0)
print(gen1)
print(type(gen1))
for i in gen1:
    print(i)