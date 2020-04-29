st_of_words = input()
lst = []
while st_of_words != '':
    lst.append(st_of_words)
    st_of_words = input()

print(*sorted(lst, key=lambda x: sum([ord(i) - ord('A') + 1 for i in x.upper()])), sep='\n')

# OK