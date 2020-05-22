n = int(input())
total_sum = (n * (n + 1)) // 2

for _ in range(n - 1):
    total_sum -= int(input())

print(total_sum)
