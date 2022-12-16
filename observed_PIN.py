import itertools

possibles={'0':'08', '1':'124','2':'1235','3':'236','4':'1457',\
           '5':'24568','6':'3569','7':'478','8':'57890','9':'689'}

def get_pins(observed):
    P= itertools.product(*map(lambda x: possibles[x],observed))
    return list(map(lambda x: ''.join(x),P))

list1=['1','12','123','1234']
for l in list1:
    print(get_pins(l))