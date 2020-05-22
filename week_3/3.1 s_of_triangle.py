a, b, c = (float(input()) for _ in range(3))
p = 1 / 2 * (a + b + c)
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(s)
