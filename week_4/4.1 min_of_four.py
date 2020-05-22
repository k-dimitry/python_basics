a, b, c, d = (int(input()) for _ in range(4))


def min4(num1, num2, num3, num4):
    return min(num1, num2, num3, num4)


print(min4(a, b, c, d))
