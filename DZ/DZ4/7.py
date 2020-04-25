from itertools import product

suit = ['пик', 'треф', 'бубен', 'червей']
num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']

miss = input('Введите масть: ')
if miss not in suit:
    print("Вы ввели неправильно")
    exit()
suit.remove(miss)

for a, b in product(num, suit):
    print(f'{a} {b}')
