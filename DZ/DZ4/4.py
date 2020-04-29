from itertools import permutations
dictionary = input().lower().split()
letter = input().lower().split()
lst = []
for i in letter:
    for j in dictionary:
        if sorted(i) == sorted(j) and i != j and sorted(list(permutations(i))) == sorted(list(permutations(j))):
            lst.append(i)
result = []
for i in letter:
    if i in lst:
        result.append('#' * len(i))
    else:
        result.append(i)
print(*result)

# OK