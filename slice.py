A = [0] * 30
print(A)
A[::3] = [1] * len(A[::3])
print(A)
A = [0] * 30
A[::5] = [1] * len(A[::5])
print(A)