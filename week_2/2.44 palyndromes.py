n = int(input())
counter = 0

for num in range(1, n + 1):
    if str(num) == str(num)[::-1]:
        counter += 1

print(counter)
