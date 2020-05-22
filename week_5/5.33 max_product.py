lst = [int(n) for n in input().split()]

max1 = max2 = min1 = min2 = lst[0]

for i in lst:
    if max2 < i > max1:
        max2 = max1
        max1 = i
    elif i > max2:
        max2 = i
    if min2 > i < min1:
        min2 = min1
        min1 = i
    elif min2 > i:
        min2 = i

if max1 * max2 > min1 * min2:
    print(max2, max1)
else:
    print(min1, min2)
