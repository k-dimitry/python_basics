num = int(input())


def phib(n):
    if n in (1, 2):
        return 1
    else:
        return phib(n - 1) + phib(n - 2)


print(phib(num))
