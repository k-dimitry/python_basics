n = int(input())


def MinDivisor(n):
    for i in range(2, n + 1):
        if i > n ** 0.5:
            return n
        if n % i == 0:
            return i


print(MinDivisor(n))
