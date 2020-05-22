import copy
from sys import stdin


class Matrix(object):
    def __init__(self, m):
        self.m = copy.deepcopy(m)

    def __str__(self):
        result = []
        for row in self.m:
            sub_res = []
            for num in row:
                sub_res.append(str(num))
            result.append("\t".join(sub_res))
        return "\n".join(result)

    def size(self):
        return len(self.m), len(self.m[0])

    def __add__(self, other):
        temp_m = [[0 for _ in range(self.size()[1])]
                  for _ in range(self.size()[0])]
        for row in range(len(temp_m)):
            for col in range(len(temp_m[0])):
                temp_m[row][col] = self.m[row][col] + other.m[row][col]
        return Matrix(temp_m)

    def __mul__(self, other):
        temp_m = copy.deepcopy(self.m)
        for row in range(len(self.m)):
            for col in range(len(self.m[0])):
                temp_m[row][col] *= other
        return Matrix(temp_m)

    __rmul__ = __mul__


exec(stdin.read())
