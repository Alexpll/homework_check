class Sorted:
    def __init__(self):
        self.key = lambda x: -x

    def set_data(self, new_data):
        self.data = new_data

    def get_data(self):
        return self.data

    def set_key(self, new_key):
        self.key = new_key

    def my_sort(self):
        lst = []
        for d in self.data:
            d = sorted(d, key=self.key)
            lst.append(d)
        lst = sorted(lst, key=lambda x: self.key(x[-1]))
        return lst[::-1]


s = Sorted()
s.set_data([[1], [3, 2], [6, 5, 4]])
s.set_key(lambda x: x)
print(s.my_sort())
