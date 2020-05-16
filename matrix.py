import random
from copy import deepcopy


class Matrix:
    def __init__(self, a, b=None):
        if b is not None:
            self.data = [[-100 + random.random() * 200 for j in range(b)] for i in range(a)]
            self.shape = a, b
        else:
            self.data = a.copy()
            self.shape = len(a), len(a[0])

    def check_shape_for_add(self, matrix):
        matr = Matrix(matrix)
        return self.shape == matr.shape

    def check_shape_for_mul(self, matrix):
        matr = Matrix(matrix)
        return self.shape[1] == matr.shape[0]

    def check_shape_square(self):
        return self.shape[0] == self.shape[1]

    def gauss_solution(self, b):
        matrix = deepcopy(self.data)
        rows, cols = self.shape
        if len(b) != rows or not self.check_shape_square():
            return "Недостаточно данных"
        if self.is_degenerate():
            return "Матрица вырожденная"
        b = b.copy()
        for col in range(cols):
            for row in range(col + 1, rows):
                new_row = [-val * (matrix[row][col]) / matrix[col][col] for val in matrix[col]]
                b[row] = b[row] - b[col] * matrix[row][col] / matrix[col][col]
                matrix[row] = [sum(x) for x in zip(matrix[row], new_row)]
        print(matrix, b)
        x = []
        for row in reversed(range(rows)):
            x_row = b[row]
            i = 1
            for col in range(rows - row - 1):
                x_row -= x[col] * matrix[row][0 - i]
                i += 1
            x_row /= matrix[row][row]
            x.append(x_row)
        x = x[::-1]
        return x

    @staticmethod
    def __det(matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            res = 0
            for i in range(len(matrix)):
                sub_data = []
                for row in range(1, len(matrix)):
                    sub_row = []
                    for col in range(len(matrix)):
                        if col == i:
                            continue
                        sub_row.append(matrix[row][col])
                    sub_data.append(sub_row)
                submatrix = Matrix(sub_data)
                if i % 2 == 0:
                    res += matrix[0][i] * submatrix.determinant()
                else:
                    res -= matrix[0][i] * submatrix.determinant()
            return res

    def determinant(self, a=False):
        if a:
            if self.check_shape_square():
                return self.__det(a)
            else:
                return "Матрица не квадратная"
        matrix = self.data.copy()
        if self.check_shape_square():
            return self.__det(matrix)
        else:
            return "Матрица не квадратная"

    def __add__(self, other):
        matrix_2 = other
        result_matrix = []
        if self.check_shape_for_add(matrix_2):
            for i in range(len(matrix_2)):
                lst = []
                for j in range(len(matrix_2[0])):
                    lst.append(matrix_2[i][j] + self.data[i][j])
                result_matrix.append(lst)
            return result_matrix
        else:
            print("Неправильные размеры матрицы, попробуйте ещё раз")

    def __iadd__(self, other):
        matrix_2 = other
        if self.check_shape_for_add(matrix_2):
            self.data = self.__add__(matrix_2)
            return Matrix(self.data)
        else:
            print("Неправильные размеры матрицы, попробуйте ещё раз")
            return Matrix(self.data)

    def __sub__(self, other):
        matrix_2 = other
        result_matrix = []
        if self.check_shape_for_add(matrix_2):
            for i in range(len(matrix_2)):
                lst = []
                for j in range(len(matrix_2[0])):
                    lst.append(self.data[i][j] - matrix_2[i][j])
                result_matrix.append(lst)
            return result_matrix
        else:
            print("Неправильные размеры матрицы, попробуйте ещё раз")

    def __isub__(self, other):
        matrix_2 = other
        if self.check_shape_for_add(matrix_2):
            self.data = self.__sub__(matrix_2)
            return Matrix(self.data)
        else:
            print("Неправильные размеры матрицы, попробуйте ещё раз")
            return Matrix(self.data)

    def __mul__(self, other):
        matrix_2 = other
        result_matrix = []
        if str(matrix_2).isdigit():
            for i in range(len(self.data)):
                lst = []
                for j in range(len(self.data[0])):
                    lst.append(self.data[i][j] * matrix_2)
                result_matrix.append(lst)
            return result_matrix
        if self.check_shape_for_mul(matrix_2):
            for i in range(len(self.data)):
                lst = []
                for j in range(len(matrix_2[0])):
                    res = 0
                    for k in range(len(self.data[0])):
                        res += self.data[i][k] * matrix_2[k][j]
                    lst.append(res)
                result_matrix.append(lst)
            return result_matrix
        else:
            print("Неправильные размеры матрицы, попробуйте ещё раз")

    def __imul__(self, other):
        matrix_2 = other
        if str(matrix_2).isdigit():
            self.data = self.__mul__(matrix_2)
            return Matrix(self.data)
        if self.check_shape_for_mul(matrix_2):
            self.data = self.__mul__(matrix_2)
            return Matrix(self.data)
        else:
            print("Неправильные размеры матрицы, попробуйте ещё раз")
            return Matrix(self.data)

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return f"Matrix{self.data}"

    def __setitem__(self, key, value):
        if type(key) == int and type(value) == list:
            if len(self.data) <= key:
                self.data.append(value)
            else:
                self.data[key] = value
        else:
            print("Неправильный формат ввода")

    def __getitem__(self, item):
        if type(item) == int:
            if len(self.data) > item:
                return self.data[item]
            else:
                return "Значение отсутствует"
        else:
            return "Неправильный формат ввода"

    def is_degenerate(self):
        if self.determinant() == 0:
            return True
        else:
            return False

    def kramer_solution(self, b):
        matrix = deepcopy(self.data)
        rows, cols = self.shape
        if len(b) != rows or not self.check_shape_square():
            return "Недостаточно данных"
        if self.is_degenerate():
            return "Матрица вырожденная"
        b = b.copy()
        det = self.determinant()
        x = []
        for i in range(len(matrix)):
            k = 0
            for j in b:
                matrix[k][i] = j
                k += 1
            det_1 = self.determinant(matrix)
            x.append(det_1 / det)
            print(matrix)
            matrix = deepcopy(self.data)
        return x

    def inverse(self):
        matrix = deepcopy(self.data)
        if not self.check_shape_square():
            return "Неквадратная матрица"
        if self.is_degenerate():
            return "Матрица вырожденная"
        ed_matrix = [[0 for x in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            ed_matrix[i][i] = 1
        list_of_x = []
        for j in range(len(matrix)):
            lst = self.gauss_solution(ed_matrix[j])
            list_of_x.append(lst)
        list_of_x = [list(i) for i in zip(*list_of_x)]
        return list_of_x


a = Matrix([[1, 3, 7], [2, 3, 3], [5, 0, 2]])
print(a.gauss_solution([3, 7, 0]))
print(a.kramer_solution([3, 7, 0]))
print(a.determinant())

aa = Matrix([[1, 2, 3, 4, 5], [3, 4, 5, 6, 7], [2, 4, 5, 7, 8], [3, 2, 3, 1, 1], [4, 5, 2, 1, 3]])
print(aa.gauss_solution([4, 3, 1, 2, 3]))
print(aa.determinant())

aaa = Matrix([[1, 2], [3, 4]])
print(aaa.gauss_solution([1, 2]))

b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 3]])
b.gauss_solution([1, 2, 3])

c = Matrix([[1, 2], [3, 4], [5, 6]])
print(c + [[-1, -2], [-31, -416], [-5, -6]])
print(c + [[2, 5, 3], [4, 4, 6], [5, 7, 8]])
c += [[-1, -2], [-31, -416], [-5, -6]]
c += [[5, 2], [3, 4], [5, 7]]
print(c)
print(c - [[0, 1], [2, 3], [4, 5]])
print(c - [[11, 2], [13, 14], [15, 16]])
c -= [[1, 2], [3, 4], [5, 6]]
c -= [[50, 25], [2, 35], [0, 2]]
print(c)

d = Matrix([[1, 2], [3, 4], [5, 6]])
print(d * [[2, 3, 4], [4, 5, 3]])
print(d * 5)
d *= [[2, 3, 4], [4, 5, 3]]
print(d)
d *= [[2, 3, 4]]
d *= 5
print(d)

e = Matrix([[1, 25], [6, 9], [5, 14]])
print(str(e))
print(repr(e))
ee = Matrix([[1, 35], [2, 5], [0, 6]])
print(str(ee))
print(repr(ee))

dd = Matrix([[1, 2], [3, 4]])
dd[2] = [5, 6]
print(dd[5])
ddd = Matrix([[5, 6], [9, 11]])
ddd[1] = [7, 2]
print(ddd[0])

f = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f.is_degenerate())
ff = Matrix([[1, 4, 17], [2, 15, 8], [13, 6, 9]])
print(ff.is_degenerate())

g = Matrix([[1, 4, 17], [2, 15, 8], [13, 6, 9]])
print(g.kramer_solution([5, 6, 9]))

h = Matrix([[1, 2, 3, 4, 5], [3, 4, 5, 6, 7], [2, 4, 5, 7, 8], [3, 2, 3, 1, 1], [4, 5, 2, 1, 3]])
print(h.inverse())
hh = Matrix([[1, 2], [3, 4]])
print(hh.inverse())