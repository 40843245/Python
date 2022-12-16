#poker_sorted.py

hands = ["3c", "Qc", "Js", "Kh", "2h", "5c", "As", "Jd"]
values={'K':13,'A':14,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'2':15}
suitable={'c':1,'d':2,'h':3,'s':4}

sorted_list=sorted(hands,key=lambda x: (values[x[0]],suitable[x[1]]))
print(sorted_list)