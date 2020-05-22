lst = list(map(int, input().split()))

min_odd = lst[0]

for n in lst[1:]:
    if min_odd == 0 or min_odd % 2 == 0:
        min_odd = n
    if n % 2 and n < min_odd:
        min_odd = n

print(min_odd)
