lst = list(map(int, input().split()))

max1 = max2 = max3 = -1 * 10 ** 5
min1 = min2 = 1 * 10 ** 5

for n in lst:
    if n > max1:
        max1, max2, max3 = n, max1, max2
    elif n > max2:
        max2, max3 = n, max2
    elif n > max3:
        max3 = n
    if min1 > n:
        min1, min2 = n, min1
    elif min2 > n:
        min2 = n

if max1 * max2 * max3 > min1 * min2 * max1:
    print(max1, max2, max3)
else:
    print(min1, min2, max1)
