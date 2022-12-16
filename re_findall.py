import re
def sort_poker(john, uncle):
    txt = re.findall(r'([A-Z])(\d+|[AJQK])', john)
    txt = list(map(''.join, txt))
    values= {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return ''.join(sorted(txt, key= lambda c: (uncle.index(c[0]), values[c[1:]])))