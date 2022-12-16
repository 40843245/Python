#raise1.py
def my_range(start,stop,step=1):
    if step==0:
        raise ValueError("step must not be equal to 0.")
    if start<stop:
        i=start
        if step<0:
            raise ValueError("When start < stop , step must not be less than 0")
        while i<stop:
            yield i
            i+=step
    else:
        i=start
        if step>0:
            raise ValueError("When start > stop , step must not be greater than 0")
        while i>stop:
            yield i
            i+=step

def my_output(x,y,z):
    gen1=my_range(x,y,z)
    print(gen1)
    print(type(gen1))
    for i in gen1:
        print(i)
        
my_output(10,12,1)
#output will be infite if step==0
#output: 10\n10\n10\n10\n10\n...
#my_output(31,121,0)

my_output(31,12,-1)

#my_output(11,12,-1)
#output will be infite if step<0 and start<stop
#output: 11\n10\n9\n...
my_output(13,12,2)
#output will be infite if step>0 and start>stop
#output: 13\n15\n17\n19\n...

