lst = []

for _ in range(8):
    lst.append(list(map(int, input().split())))

index = 0
okey = True
for _ in range(8):
    new_lst = lst.copy()
    new_lst.pop(index)
    x1, y1 = lst[index]
    for item in new_lst:
        x2, y2 = item
        if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            okey = False
            break
    index += 1

print("NO" if okey else "YES")
