n = int(input())
total_sum = 0

for num in range(1, n + 1):
    total_product = 1
    for i in range(1, num + 1):
        total_product *= i
    total_sum += total_product

print(total_sum)
