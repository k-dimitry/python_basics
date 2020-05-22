a, b = int(input()), int(input())


def sum(a, b):
    if b == 1:
        return a + 1
    elif b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a + 1, b - 1)


print(sum(a, b))
