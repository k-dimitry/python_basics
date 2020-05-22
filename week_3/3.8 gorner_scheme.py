n = int(input())
x = float(input())
total = 0
for _ in range(n + 1):
    total += float(input()) * x ** n
    n -= 1

print(total)
