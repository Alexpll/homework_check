def squared():
    lst = []
    for i in range(11, 99):
        squar = i**2
        if squar % 10 == 0:
            continue
        if len(str(squar)) != 4:
            squar = str(squar) + ' '
        lst.append(squar)
        if len(lst) == 9:
            print(*lst)
            lst.clear()


def squared_new():
    lst = [x ** 2 for x in range(1, 100) if x % 10 != 0]
    for x in lst:
        if len(str(x)) == 1:
            print(f"{x}   ", end=' ')
        elif len(str(x)) == 2:
            print(f"{x}  ", end=' ')
        elif len(str(x)) == 3:
            if x == 625:
                print(f"{x} ")
            else:
                print(f"{x} ", end=' ')
        else:
            if x == 5776 or x == 2601:
                print(x)
            else:
                print(x, end=' ')


squared_new()