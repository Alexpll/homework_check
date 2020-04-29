import sys

lst = list(map(str.strip, sys.stdin))
comments = list(filter(lambda word: word[0] == '#', lst))
for i in range(len(comments)):
    print(f'Line {i + 1}: {comments[i][1::].strip()}')

# OK