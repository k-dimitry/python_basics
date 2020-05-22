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


exec(stdin.read())
