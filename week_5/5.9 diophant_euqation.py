a, b, c, d, e = (int(input()) for _ in range(5))
counter = 0

for x in range(0, 1001):
    if x - e == 0:
        continue
    if (a * x ** 3 + b * x ** 2 + c * x + d) / (x - e) == 0:
        counter += 1

print(counter)
