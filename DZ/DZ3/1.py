def find_farthest_orbit(list_of_orbits):
    area = 0
    result = 'Вы не ввели данные'
    for i in list_of_orbits:
        area1 = 3.14 * i[0] * i[1]
        if area1 > area:
            result = i
            area = area1
    return result


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))