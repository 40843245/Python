#dict_for.py
name={'Huang':'Jay','Stephen':'Curry','Kobe':'Kryant'}
print("my name item:")
print("1")
for first,last in name.items():
    print(first,last)
print("2")
for first in name.keys():
    print(first,name[first])
print("3")
for last in name.values():
    print(last)