a, b, c, d, e, f = (float(input()) for _ in range(6))
if a == 0:
    y = e / b
    x = (f - d * y) / c
else:
    y = (a * f - e * c) / (a * d - b * c)
    x = (e - b * y) / a
print(x, y)
