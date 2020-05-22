a, b = float(input()), float(input())


def IsPointInSquare(x, y):
    return abs(x) + abs(y) <= 1


print("YES" if IsPointInSquare(a, b) else "NO")
