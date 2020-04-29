def bracket_check(st):
    lst_of_sym = ['(', ')', '{' '}', '[', ']']
    lst_of_brackets = []
    for i in st:
        if i in lst_of_sym:
            lst_of_brackets.append(i)
    count = 0
    for i in range(len(lst_of_brackets)):
        if lst_of_brackets[i] == '(':
            for j in lst_of_brackets[i::]:
                if j == ')':
                    count += 2
                    break
        elif lst_of_brackets[i] == '{':
            for j in lst_of_brackets[i::]:
                if j == '}':
                    count += 2
                    break
        elif lst_of_brackets[i] == '[':
            for j in lst_of_brackets[i::]:
                if j == ']':
                    count += 2
                    break

    if count == len(lst_of_brackets):
        print('Yes')
    else:
        print('No')

# Вот пример, когда не то. Попробуйте воспользоваться идеей со стеком
# т.е. если скобка открывается, то кладем в стек, если закрывается, то
# смотрим в стек, если там пусто или скобка не того же типа, то ошибка,
# иначе продолжаем
bracket_check('{[(2+3)*(6-3)]/{{5}()((}))')