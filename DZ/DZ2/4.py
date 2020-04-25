def swap(lst_1, lst_2):
    global first
    global second
    first = lst_2
    second = lst_1


'''first = [1, 2, 3]
second = [4, 5, 6]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)'''
first = [1, 2, 3]
second = [4, 5, 6, 7]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)