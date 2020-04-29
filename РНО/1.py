import sys


def median(lst_check):
    if len(lst_check) == 0:
        print(-1)
    elif len(lst_check) % 2 == 0:
        print((lst_check[len(lst_check) // 2 - 1] + lst_check[len(lst_check) // 2]) / 2)
    else:
        print(lst_check[(len(lst_check) - 1) // 2])


x = int(input())
lst = []

for line in sys.stdin:
    lst.append(line.split())

for i in lst:
    data = sorted(filter(lambda a: a % x == 0, map(int, i)))
    median(data)


# OK