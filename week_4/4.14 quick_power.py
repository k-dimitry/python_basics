a, n = float(input()), int(input())


def quick_power(a, n):
    if n % 2:
        return a * a ** (n - 1)
    else:
        return (a ** 2) ** (n / 2)


print(quick_power(a, n))
