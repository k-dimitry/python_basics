x1, y1, x2, y2 = (float(input()) for _ in range(4))


def distance(a1, b1, a2, b2):
    return ((a2 - a1) ** 2 + (b2 - b1) ** 2) ** 0.5


print(distance(x1, y1, x2, y2))
