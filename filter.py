#filter.py

#filter(func,iterable onbject)
#when an element (called E) in iterable object satisfys the func (i.e. when func(E) return True) , 
#this element (E) will be added into a new iterable object (called new_iter)
#then new_iter will be returned.
#P.S.
#version:
#filter will return iterable object when the version of python compiler is after version 2.7
#filter will return list when the version of python compiler is before or same as version 2.7
def is_odd(n):
    return n % 2 == 1
#because of this version 3.9 , type of newList is iterable object
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#output:<filter object at 0x0433E8B0>
print(newlist)
#output:[1,3,5,7,9]
print(list(newlist))

new_iter=newlist.__iter__
print(new_iter)
next_iter=newlist.__next__
next_iter2=newlist.__next__
print(next_iter)
print(next_iter2)