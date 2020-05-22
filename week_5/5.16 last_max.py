lst = list(map(int, input().split()))

max_n = lst[0]
max_i = 0

for i, n in enumerate(lst):
    if n == max_n:
        max_i = i
    elif n > max_n:
        max_n, max_i = n, i

print(max_n, max_i)
