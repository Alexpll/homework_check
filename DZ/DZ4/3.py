from functools import reduce
import sys
data = list(map(str.strip, sys.stdin))

print(reduce(lambda x, y: x if x < y else y, data))
