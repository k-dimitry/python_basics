a, b = int(input()), int(input())


def xor(x, y):
    return x != y


print(1 if xor(a, b) else 0)
