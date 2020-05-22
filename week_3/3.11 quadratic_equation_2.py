a, b, c = (float(input()) for _ in range(3))

if a == b == c == 0:
    print(3)
elif a != 0:
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(2, min(x1, x2), max(x1, x2))
    elif d == 0:
        print(1, (-b + d ** 0.5) / (2 * a))
    elif d < 0:
        print(0)
elif a == 0 and b != 0:
    print(1, -c / b)
else:
    print(0)
