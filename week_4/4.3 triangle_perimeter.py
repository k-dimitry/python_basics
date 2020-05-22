x1, y1, x2, y2, x3, y3 = (float(input()) for _ in range(6))


def distance(a1, b1, a2, b2):
    return ((a2 - a1) ** 2 + (b2 - b1) ** 2) ** 0.5


a = distance(x1, y1, x2, y2)
b = distance(x2, y3, x3, y2)
c = distance(x3, y1, x1, y3)

print(a + b + c)
