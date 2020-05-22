a, b = (float(input()) for _ in range(2))


def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


print("YES " if IsPointInSquare(a, b) else "NO")
