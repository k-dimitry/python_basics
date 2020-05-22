x, y = float(input()), float(input())


def IsPointInArea(x, y):
    a = (x + 1)**2 + (y - 1)**2 <= 4 and y >= -x and y >= 2*x + 2
    b = (x + 1)**2 + (y - 1)**2 >= 4 and y <= -x and y <= 2*x + 2
    return a or b


print("YES" if IsPointInArea(x, y) else "NO")
