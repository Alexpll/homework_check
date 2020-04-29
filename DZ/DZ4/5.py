import sys
data = list(map(str.strip, sys.stdin))
lst = []
matrix = []
for i in data:
    lst.append(i.split())
for i in lst:
    i = list(map(int, i))
    matrix.append(i)

sum_of_st = sum(matrix[0])
if all([sum(x) == sum_of_st for x in matrix]) and all([sum(x) == sum_of_st for x in list(zip(*matrix))]):
    print('YES')
else:
    print('NO')
    
# OK