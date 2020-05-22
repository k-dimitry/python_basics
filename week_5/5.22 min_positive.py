lst = [int(n) for n in input().split()]
min_pos = lst[0]

for n in lst[1:]:
    if n <= 0:
        continue
    if min_pos <= 0 < n:
        min_pos = n
    elif n < min_pos:
        min_pos = n

print(min_pos)
