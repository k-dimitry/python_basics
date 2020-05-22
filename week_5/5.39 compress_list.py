lst = list(map(int, input().split()))
zero_count = 0

for i in lst:
    if i != 0:
        print(i, end=" ")
    else:
        zero_count += 1
        continue
print(*[0] * zero_count)
