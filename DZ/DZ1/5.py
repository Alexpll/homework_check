def eratosthenes_new(n):
    lst_of_num = [int(x) for x in range(1, n + 1)]
    result = []
    lst = []
    i = 2
    while i != lst_of_num[-1]:
        lst.clear()
        for elem in lst_of_num:
            if elem > 2:
                if elem != i and elem % i == 0:
                    if elem not in result:
                        result.append(elem)
        for j in lst_of_num:
            if j not in result:
                lst.append(j)
        lst = lst[i::]
        if len(lst) != 0:
            i = lst[0]
        else:
            break
    print(result)


eratosthenes_new(15)

# OK