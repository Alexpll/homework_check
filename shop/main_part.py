from datetime import datetime


class Shop:
    def save_changes(self, file_name):
        text = open("shops.txt", "w")
        for i in dict_lines:
            st = ''
            for j in range(len(dict_lines[i])):
                if dict_lines[i][j][2] != 0:
                    st += str(dict_lines[i][j][0]) + ',' + str(dict_lines[i][j][1]) + ',' + str(dict_lines[i][j][2])
                    if j != len(dict_lines[i]) - 1:
                        st += ', '
            line = i + ':' + st + '\n'
            text.write(line)
        text.close()

    def load_data(self, file_name, rewrite=False):
        text = open(file_name, "a")
        text.write('')
        if rewrite:
            text.close()
            text = open(file_name, "w")
        count_shops = int(input('Сколько магазинов добавите: '))
        for j in range(count_shops):
            st = ''
            shop = input('Название магазина: ')
            num = int(input('Сколько продуктов добавите: '))
            for i in range(num):
                product = input('Название продукта: ')
                price = int(input('Цена продукта: '))
                count = int(input('Количество продукта: '))
                st += product + ',' + str(price) + ',' + str(count)
                if i != num - 1:
                    st += ', '
            line = shop + ':' + st + '\n'
            text.write(line)
        text.close()

    def user_buy(self, user_name, shop_name, product_name, count, save_check=False):
        global dict_lines
        if shop_name in dict_lines:
            if product_name in dict_lines[shop_name][0]:
                if dict_lines[shop_name][0][2] >= count:
                    dict_lines[shop_name][0][2] -= count
                    if save_check:
                        data = datetime.now()
                        data = str(data).split()
                        timer = data[1][:2] + '-' + data[1][3:5] + '-' + data[1][6:8]
                        user_file = open(f"{user_name}_{data[0]}_{timer}.txt", "w")
                        user_file.write(
                            f"{user_name} bought {product_name} in the store {shop_name} in the amount of {count} pieces"
                            f" {data[0]} at {timer}")
                        user_file.close()

    def find_product(self, product_name, count=-1):
        lst = []
        for i in dict_lines:
            for j in dict_lines[i]:
                if j[0] == product_name:
                    if count > 0:
                        if j[2] > count:
                            lst.append(i)
                    else:
                        lst.append(i)
        return lst

    def sort_shops_by_product_price(self, product):
        lst = []
        for i in dict_lines:
            for j in dict_lines[i]:
                if j[0] == product:
                    lst.append((i, j[1]))
        lst = sorted(lst, key=lambda price: price[1])
        return lst

    def sort_shops_by_product_count(self, product):
        lst = []
        for i in dict_lines:
            for j in dict_lines[i]:
                if j[0] == product:
                    lst.append((i, j[2]))
        lst = sorted(lst, key=lambda count: count[1])[::-1]
        return lst


dict_lines = {}
text = open("shops.txt")
count = 0
for line in text:
    new_list = []
    lst = line.split(':')
    lst[1] = lst[1].strip('\n').split(', ')
    for i in lst[1]:
        i = i.split(',')
        new_i = []
        for x in i:
            if x.isdigit():
                x = int(x)
                new_i.append(x)
            else:
                new_i.append(x)
        new_list.append(new_i)
    dict_lines[lst[0]] = new_list
text.close()

# print(dict_lines['Pyaterochka'][0][1])
s = Shop()
#s.load_data('shops.txt', True)
#s.load_data('shops.txt')
s.user_buy('Sashka', 'Pyaterochka', 'cheese', 4, True)
#s.save_changes('shops.txt')
s.user_buy('Sashka', 'Pyaterochka', 'flour', 2, True)
print(s.find_product('tomato', 19))
print(s.sort_shops_by_product_price('cheese'))
print(s.sort_shops_by_product_price('tomato'))
print(s.sort_shops_by_product_count('flour'))
s.save_changes('shops.txt')