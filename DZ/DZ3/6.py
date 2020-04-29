def ask_password(login, password, success, failure):
    list_of_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    login = login.lower()
    password = password.lower()
    for x in password:
        for i in list_of_vowels:
            if x == i:
                count += 1
    login_without_vowels = ''.join(let for let in login if let not in list_of_vowels)
    password_without_vowels = ''.join(let for let in password if let not in list_of_vowels)
    if login_without_vowels != password_without_vowels and count != 3:
        failure(login, 'Everything is wrong')
        return (False, 'Everything is wrong')
    elif login_without_vowels == password_without_vowels and count == 3:
        success(login)
        return (True, '')
    elif login_without_vowels != password_without_vowels:
        failure(login, 'Wrong consonants')
        return (False, 'Wrong consonants')
    elif count != 3:
        failure(login, 'Wrong number of vowels')
        return (False, 'Wrong number of vowels')


def success(login):
    return


def failure(login, err=''):
    return


def main(login, password):
    flag, err = ask_password(login, password, success, failure)
    if flag:
        print(f'Привет, {login}')
    else:
        print(f'Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {err.upper()}.')


ask_password('color', 'clraaa', lambda login: print('super'), lambda login, err: print('bad'))
main('color', 'claaa')

# OK
