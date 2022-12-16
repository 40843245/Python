def checkRepeated(l,elem):
    new_list=[]
    for i in range(l):
        for j in range(len(new_list)):
            if(new_list[j]==elem):
                return False
        new_list.append(l[i])
    return True
def checkConsecutive(l):
    new_list=[]
    maxi=max(l)
    mini=min(l)
    for i in range(mini,maxi+1):
        if(mini>=l[i] or l[i]>=maxi):
            return False
        if(l[i] is in new_list):
            return False
        new_list.append(l[i])
    return True