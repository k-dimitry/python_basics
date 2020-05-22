import copy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix(object):
    def __init__(self, matrix):
        self.m = copy.deepcopy(matrix)

    def __str__(self):
        res_matrix = []

        for row in range(len(self.m)):
            sub_res = []
            for col in range(len(self.m[0])):
                sub_res.append(str(self.m[row][col]))
            res_matrix.append("\t".join(sub_res))

        return "\n".join(res_matrix)

    def size(self):
        return len(self.m), len(self.m[0])

    def __add__(self, other):
        if len(self.m) != len(other.m):
            raise MatrixError(self, other)
        for row1, row2 in zip(self.m, other.m):
            if len(row1) != len(row2):
                raise MatrixError(self, other)

        tmp_matrix = [[0 for _ in range(self.size()[1])]
                      for _ in range(self.size()[0])]

        for row in range(self.size()[0]):
            for col in range(self.size()[1]):
                tmp_matrix[row][col] = self.m[row][col] + other.m[row][col]

        return Matrix(tmp_matrix)

    def __mul__(self, other):
        tmp_matrix = copy.deepcopy(self.m)

        for row in range(len(tmp_matrix)):
            for col in range(len(tmp_matrix[0])):
                tmp_matrix[row][col] *= other

        return Matrix(tmp_matrix)

    __rmul__ = __mul__

    def transpose(self):
        self.m = [*map(list, zip(*self.m))]
        return self

    @staticmethod
    def transposed(matrix):
        tmp = copy.deepcopy(matrix)
        return tmp.transpose()


# exec(stdin.read())
