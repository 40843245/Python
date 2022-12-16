#itertools.py
#show that how to use itertools  to solve the common math problem

from itertools import permutations
print(list(permutations("ABCD",2)))

from itertools import combinations
print(list(combinations("ABCD",2)))

from itertools import combinations_with_replacement
print(list(combinations_with_replacement("ABCD",2)))

from itertools import product
print(list(product('ABC', 'xyz')))
print(list(product('AB', 'xy','12')))