from math import gcd
from functools import reduce
data = []
a = input()
while a != '':
    data.append(int(a))
    a = input()

print(reduce(gcd, data))

# OK