x = 1
y = 2
l = [x, y]
print(l)
x += 5
print(l)

a = [1]
b = [2]
s = [a, b]
print(s)
a.append(5)
print(s)

#ans:
"""
[1, 2]
[1, 2]
[[1], [2]]
[[1, 5], [2]]
"""
#sol:
#list, dict, set is mutable.
#int, string, tuple  is immutable.
#mutable means can be replace in place.