n, m = int(input()), int(input())


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def ReduceFraction(n, m):
    num = gcd(n, m)
    return n // num, m // num


print(*ReduceFraction(n, m))
