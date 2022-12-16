#print_Parameter.py
"""
learn the Parameter of print function
object: sth you wanna to print
end   : after print function is finished, then print the value of Parameter end. Default '\n'.
sep   : after print every object, then print the value of Parameter sep. Default, ' '.
file  : an object with a write method. Default is sys.stdout.
flush : A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False.
"""
import sys
str1="handsome"
str2="and"
str3="beautiful"

print("Let's print sth")
print("the flush is false by default")
print(str1,str2,str3)
print("2th")
print(str1,str2,str3,sep="---")
print("3th")
print(str1,str2,str3,end="---")
print("4th")
print(str1,str2,str3,file=sys.stdout)
print("5th")
print(str1,str2,str3,flush="false")
print("6th")
print(str1,str2,str3,flush="true")
print("")
print()