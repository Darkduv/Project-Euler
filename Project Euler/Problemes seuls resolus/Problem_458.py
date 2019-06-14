# %% Problem 458
from Tools import quick_expo


class Matrix:
    def __init__(self, mat):
        self.mat = mat
        self.dim = len(mat), len(mat[0])

    def __mul__(self, other):
        if type(other) == Matrix:
            n, p = self.dim
            r = other.dim[1]
            prod = [[0] * r for _ in range(n)]
            for k in range(n):
                for i in range(r):
                    prod_i = 0
                    for j in range(p):
                        prod_i += self.mat[k][j] * other.mat[j][i]
                    prod_i %= mod
                    prod[k][i] = prod_i
            return Matrix(prod)
        if type(other) == int:
            return Matrix([[el * other for el in l] for l in self.mat])

    def __rmul__(self, other):
        if type(other) == Matrix:
            n, p = self.dim
            r = other.dim[1]
            prod = [[0] * r for _ in range(r)]
            for k in range(n):
                for i in range(r):
                    prod_i = 0
                    for j in range(p):
                        prod_i += self.mat[k][j] * other.mat[j][i]
                    prod_i %= mod
                    prod[k][i] = prod_i
            return Matrix(prod)
        if type(other) == int:
            return Matrix([[el * other for el in l] for l in self.mat])

    def __rmod__(self, other):
        return Matrix([[el % other for el in l] for l in self.mat])

    def __mod__(self, other):
        return Matrix([[el % other for el in l] for l in self.mat])


mod = 10 ** 9


A = [[1, 6, 0, 0, 0, 0, 0],
     [1, 1, 5, 0, 0, 0, 0],
     [1, 1, 1, 4, 0, 0, 0],
     [1, 1, 1, 1, 3, 0, 0],
     [1, 1, 1, 1, 1, 2, 0],
     [1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 7]]

A = Matrix(A)

B = Matrix([[7, 0, 0, 0, 0, 0, 0]])
C = B * quick_expo(A, 10 ** 12 - 1)
print(sum(a for a in C.mat[0][:-1]) % 10 ** 9)  # 423341841
