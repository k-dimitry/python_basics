n, k = int(input()), int(input())


def c(n, k):
    if k == 1:
        return n
    elif k == 0:
        return 1
    elif n == k:
        return 1
    return c(n - 1, k - 1) + c(n - 1, k)


print(c(n, k))
