scores= [(9, 6, 11), (10, 9, 6), (13, 8, 14), (13, 8, 11), (14, 15, 8)]
print(sorted(scores,key= lambda x: x[0]*2+x[1]*3+x[2]))