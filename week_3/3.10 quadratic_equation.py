a, b, c = (float(input()) for _ in range(3))
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(min(x1, x2), max(x1, x2))
elif d == 0:
    print((-b + d ** 0.5) / (2 * a))
