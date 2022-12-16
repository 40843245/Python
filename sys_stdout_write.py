#sys_stdout_write.py
#sys.stdout.write
import sys

def writefunc(sth):
    sys.stdout.write(sth)    

rep=sys.stdout

list1=['1','2','3','4','5','6']
for i in list1:
    rep.write(i)
    rep.write('\n')
    
for i in list1:
    writefunc(i)
    writefunc('\n')
    
for i in list1:
    writefunc(i+'\n')
#they are same
    


