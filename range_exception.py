#range_exception.py
"""
#output:ValueError: range() arg 3 must not be zero
for i in range(0,0,0):
    print(i)
"""
"""
#output:ValueError: range() arg 3 must not be zero
for i in range(0,10,0):
    print(i)
"""
#output nothing
for i in range(10,0,1):
    print(i)