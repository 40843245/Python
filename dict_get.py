#dict_get.py
#show that how to get the value of dict with a key

dict1={"well":"bad","good":"bad","better":"worse","increase":"decrease"}
msg="404 not found"
def my_dict(s):
    #print(dict1[s])#If your key is not in dict , it will occur (KeyError:'key')
    print(dict1.get(s,msg))
while True:
    s1=input("enter a string:")
    my_dict(s1)
