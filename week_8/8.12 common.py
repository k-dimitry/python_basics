# And this is how my story ends
from copy import deepcopy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix(object):
    def __init__(self, matrix):
        self.m = deepcopy(matrix)

    def __str__(self):
        tmp_matrix = []
        for row in range(len(self.m)):
            sub_matrix = []
            for col in range(len(self.m[0])):
                sub_matrix.append(str(self.m[row][col]))
            tmp_matrix.append("\t".join(sub_matrix))
        return "\n".join(tmp_matrix)

    def size(self):
        return len(self.m), len(self.m[0])

    def __add__(self, other):
        if len(self.m) != len(other.m) or len(self.m[0]) != len(other.m[0]):
            raise MatrixError(self, other)

        tmp_matrix = [[0 for _ in range(len(self.m[0]))]
                      for _ in range(len(self.m))]

        for row in range(len(self.m)):
            for col in range(len(self.m[0])):
                tmp_matrix[row][col] = self.m[row][col] + other.m[row][col]

        return Matrix(tmp_matrix)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            tmp_matrix = deepcopy(self.m)

            for row in range(len(self.m)):
                for col in range(len(self.m[0])):
                    tmp_matrix[row][col] *= other

            return Matrix(tmp_matrix)

        elif isinstance(other, Matrix):
            if len(self.m[0]) != len(other.m):
                raise MatrixError(self, other)

            new_matrix = [[0 for _ in range(len(other.m[0]))]
                          for _ in range(len(self.m))]

            for row in range(len(self.m)):
                for col in range(len(other.m[0])):
                    for k in range(len(self.m[0])):
                        new_matrix[row][col] += \
                            self.m[row][k] * other.m[k][col]

            return Matrix(new_matrix)

    __rmul__ = __mul__

    def transpose(self):
        self.m = [*map(list, zip(*self.m))]
        return self

    @staticmethod
    def transposed(matrix):
        tmp = deepcopy(matrix)
        return tmp.transpose()


exec(stdin.read())
