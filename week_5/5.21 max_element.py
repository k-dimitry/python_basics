lst = list(map(int, input().split()))

max_n = lst[0]
max_i = 0

for i in range(1, len(lst)):
    if lst[i] > max_n:
        max_n = lst[i]
        max_i = i

print(max_n, max_i)
