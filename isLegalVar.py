#isLegalVar.py

#check the var in programming language is legal or not
#Legal Var has 3 property:
#1:Only consist of alphabet , digit or '_'.
#2:It contains at least 1 alphabet. 
#3:Before the first alphabet occurs , digit can not be occur.
#illegal var:
#'123','a@1','a b' ,'','1c' or '___','_12b' is not accepted.
#legal var:
#a1b , _a , _a2 , a____,well_3

#way 1:
def isLegalVar(s):
    if s=='':
        return False
    if s[0].isupper() or s[0].islower() or s[0]=='_':
        idx=0
        while s[idx]=='_':
            idx+=1
            if idx>=len(s):
                return False
        if s[idx].isupper() or s[idx].islower():
            for i in range(idx,len(s)):
                if(s[i].isalnum() or s[i]=='_'):
                    pass
                else:
                    return False
            return True
        else:
            return False
    else:
        return False

#driver code
print("way1:")
example_list=['123','ab1','___','a#$2','','1abc','a1_1','_ee','__ee','__1e','__e1']
for l in example_list:
    print(l,"is",isLegalVar(l))
    
#way 2:
def isLegalVar(s):
    s1=s.replace('_','')
    if s1=='':
        return False
    elif s1[0].isdigit()==True:
        return False
    else:
        for i in range(1,len(s1)):
            if(s1[i].isalpha()==False and s1[i].isdigit()==False):
                return False
    return True  
#driver code
print("way2:")
example_list=['123','ab1','___','a#$2','','1abc','a1_1','_ee','__ee','__1e','__e1']
for l in example_list:
    print(l,"is",isLegalVar(l))

#way 3:
def isLegalVar(s):
    s1=(s.replace('_',''))
    if s1=='' or s1[0].isdigit():
        return False
    return [x for x in list(s1) if x.isdigit()==True or x.isalpha()==True]==list(s1)
#driver code
print("way3:")
example_list=['123','ab1','___','a#$2','','1abc','a1_1','_ee','__ee','__1e','__e1']
for l in example_list:
    print(l,"is",isLegalVar(l))