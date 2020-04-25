def add_friends(nameOfPerson, listOfFriends):
    global dict_of_friends
    dict_of_friends[nameOfPerson] = listOfFriends


def is_friends(nameOfPerson1, nameOfPerson2):
    flag = False
    for i in dict_of_friends.get(nameOfPerson1):
        if i == nameOfPerson2:
            flag = True
    return flag


def print_friends(nameOfPerson):
    print(sorted(dict_of_friends.get(nameOfPerson)))


dict_of_friends = {}
add_friends("Алла", ["Марина", "Иван"])
print(is_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(is_friends("Алла", "Мария"))